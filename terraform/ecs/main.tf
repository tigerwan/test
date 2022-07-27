
locals {
  vpc_id            = "vpc-0e27c47dd1f9c4fb9"
  subnets           = ["subnet-0b353a2494a717e10", "subnet-012ba337a6a326388", "subnet-0edc833fe02b3cbc5"]
  health_check_path = "/index.html"
}

/*
ECS Cluster
*/
resource "aws_cloudwatch_log_group" "cw_log" {
  name = "/ecs/test_ecs"
}


resource "aws_ecs_cluster" "cluster" {
  name = "test_ecs"
  configuration {
    execute_command_configuration {
      logging    = "OVERRIDE"
      log_configuration {
        cloud_watch_log_group_name = aws_cloudwatch_log_group.cw_log.name
      }
    }
  }
}


resource "aws_ecs_cluster_capacity_providers" "ecs_cluster_capacity_providers" {
  cluster_name = aws_ecs_cluster.cluster.name

  capacity_providers = ["FARGATE_SPOT"]

  default_capacity_provider_strategy {
    base              = 0
    weight            = 100
    capacity_provider = "FARGATE_SPOT"
  }

}
/*
IAM role
*/
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "test_ecs_task_execution_role"

  assume_role_policy = <<EOF
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Action": "sts:AssumeRole",
     "Principal": {
       "Service": "ecs-tasks.amazonaws.com"
     },
     "Effect": "Allow",
     "Sid": ""
   }
 ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "ecs-task-execution-role-policy-attachment" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_iam_role" "ecs_task_role" {
  name               = "test_ecs_task_role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

/* extra policy of the application permission
resource "aws_iam_policy" "dynamodb" {
  name        = "${var.name}-task-policy-dynamodb"
  description = "Policy that allows access to DynamoDB"

 policy = <<EOF
{
   "Version": "2012-10-17",
   "Statement": [
       {
           "Effect": "Allow",
           "Action": [
               "dynamodb:CreateTable",
               "dynamodb:UpdateTimeToLive",
               "dynamodb:PutItem",
               "dynamodb:DescribeTable",
               "dynamodb:ListTables",
               "dynamodb:DeleteItem",
               "dynamodb:GetItem",
               "dynamodb:Scan",
               "dynamodb:Query",
               "dynamodb:UpdateItem",
               "dynamodb:UpdateTable"
           ],
           "Resource": "*"
       }
   ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "ecs-task-role-policy-attachment" {
  role       = aws_iam_role.ecs_task_role.name
  policy_arn = aws_iam_policy.dynamodb.arn
}
*/
/*
ALB
*/
data "aws_vpc" "vpc" {
  id = local.vpc_id
}

resource "aws_security_group" "alb_sg" {
  name        = "test_ecs_alb_sg"
  description = "ALB SG"
  vpc_id      = local.vpc_id
}

resource "aws_security_group_rule" "alb_sg_rule_ingress_allow_vpc_cidr" { // allow all requests from VPC inside
  type              = "ingress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks       = [data.aws_vpc.vpc.cidr_block]
  security_group_id = aws_security_group.alb_sg.id
}

resource "aws_security_group_rule" "alb_sg_rule_ingress_allow_internal_all" { // allow all SG internal traffic
  type              = "ingress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  self              = true
  security_group_id = aws_security_group.alb_sg.id
}

resource "aws_security_group_rule" "alb_sg_rule_egress_allow_all" {
  type              = "egress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.alb_sg.id
}

resource "aws_lb" "test" {
  name               = "test"
  internal           = true
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb_sg.id]
  subnets            = local.subnets

  enable_deletion_protection = false
}

resource "aws_alb_target_group" "test" {
  name        = "test"
  port        = 80
  protocol    = "HTTP"
  vpc_id      = local.vpc_id
  target_type = "ip"

  health_check {
    healthy_threshold   = "3"
    interval            = "30"
    protocol            = "HTTP"
    matcher             = "200"
    timeout             = "3"
    path                = local.health_check_path
    unhealthy_threshold = "2"
    port                = 80
  }
}

resource "aws_alb_listener" "http" {
  load_balancer_arn = aws_lb.test.id
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_alb_target_group.test.arn
  }
}

/*
Service
*/

resource "aws_security_group" "container_sg" {
  name        = "test_ecs_container_sg"
  description = "Container SG"
  vpc_id      = local.vpc_id
}

resource "aws_security_group_rule" "container_sg_rule_ingress_allow_vpc_cidr" { // allow all requests from VPC inside
  type              = "ingress"
  from_port         = 80
  to_port           = 80
  protocol          = "-1"
  cidr_blocks       = [data.aws_vpc.vpc.cidr_block]
  security_group_id = aws_security_group.container_sg.id
}

resource "aws_security_group_rule" "container_sg_rule_ingress_allow_internal_all" { // allow all SG internal traffic
  type              = "ingress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  self              = true
  security_group_id = aws_security_group.container_sg.id
}

resource "aws_security_group_rule" "container_sg_rule_egress_allow_all" {
  type              = "egress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.container_sg.id
}

resource "aws_ecs_service" "service" {
  name                               = "test_service"
  cluster                            = aws_ecs_cluster.cluster.id
  task_definition                    = aws_ecs_task_definition.task_definition.arn
  desired_count                      = 2
  deployment_minimum_healthy_percent = 50
  deployment_maximum_percent         = 200
  launch_type                        = "FARGATE"
  /*
  https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html

  With Amazon ECS Exec, you can directly interact with containers without needing to first interact with the host container operating system, open inbound ports, or manage SSH keys. You can use ECS Exec to run commands in or get a shell to a container running on an Amazon EC2 instance or on AWS Fargate.
  */
  enable_execute_command = true
  /*
  https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html

  REPLICA—The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. For more information, see Replica.

  DAEMON—The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler evaluates the task placement constraints for running tasks and will stop tasks that do not meet the placement constraints. When using this strategy, there is no need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies. For more information, see Daemon.
  */
  scheduling_strategy = "REPLICA"

  network_configuration {
    security_groups  = [aws_security_group.container_sg.id]
    subnets          = local.subnets
    assign_public_ip = false
  }

  load_balancer {
    target_group_arn = aws_alb_target_group.test.arn
    container_name   = "sample-fargate-app"
    container_port   = 80
  }
}

/*
Task Definition
*/
resource "aws_ecs_task_definition" "task_definition" {
  family = "test_task_definition"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = 256
  memory                   = 512
  execution_role_arn       = aws_iam_role.ecs_task_role.arn
  task_role_arn            = aws_iam_role.ecs_task_execution_role.arn
  container_definitions    = <<DEFINITION
  [
      {
        "command": [
            "/bin/sh -c \"echo '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p> </div></body></html>' >  /usr/local/apache2/htdocs/index.html && httpd-foreground\""
        ],
        "entryPoint": [
            "sh",
            "-c"
        ],
        "essential": true,
        "image": "httpd:2.4",
        "logConfiguration": {
            "logDriver": "awslogs",
            "options": {
              "awslogs-create-group": "true",
              "awslogs-group" : "/ecs/fargate-task-definition",
              "awslogs-region": "ap-southeast-2",
              "awslogs-stream-prefix": "ecs"
            }
        },
        "name": "sample-fargate-app",
        "portMappings": [
            {
              "containerPort": 80,
              "hostPort": 80,
              "protocol": "tcp"
            }
        ]
      }
  ]
  DEFINITION
}
