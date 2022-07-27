/*
data "aws_network_acl_rule" "aaaa" {
  //network_acl_id = aws_network_acl.r_networkacl_priv2.id
  rule_number    = 110
  egress         = true
  protocol       = -1
  rule_action    = "allow"
  cidr_block     = "0.0.0.0/0"
}*/

locals {
  roles = {
    role1 =  "role1"
    role2 =  "role2"
  }
}
resource "aws_iam_role" "sample_roles" {
      for_each = local.roles
      name = "sample_role_${each.value}"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

locals {
  local_roles = [for r in aws_iam_role.sample_roles : r.name]
}

output "local_roles" {
    value = local.local_roles
}

