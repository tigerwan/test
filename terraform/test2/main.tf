data "local_file" "tags" {
    filename = "${path.module}/tags.txt"
}

locals {
    tags = split("\n", data.local_file.tags.content)
}

resource "aws_iam_role" "sample_roles" {
    count = length(local.tags)
    name = "sample_roles-${count.index}"
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
  tags = {
    "test" = element(local.tags, count.index)
  }
}