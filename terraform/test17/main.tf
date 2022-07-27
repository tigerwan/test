locals {
/*
	x = ["a", "b", "c"]
	y = format("this is [%s]", tostring(local.x))
*/
/*
    az_build              = {
      ap-southeast-2a = {
          private_subnet_cidr    = "172.29.2.0/24"
          protect_subnet_cidr    = "172.29.6.0/25"
          public_subnet_cidr     = "172.29.0.0/25"
        }
      ap-southeast-2b = {
          private_subnet_cidr    = "172.29.3.0/24"
          protect_subnet_cidr    = "172.29.6.128/25"
          public_subnet_cidr     = "172.29.0.128/25"
        }
      ap-southeast-2c = {
          private_subnet_cidr    = "172.29.4.0/24"
          protect_subnet_cidr    = "172.29.7.0/25"
          public_subnet_cidr     = "172.29.1.0/25"
        }
    }

    y = [for k,v in local.az_build: v.private_subnet_cidr]

	m = [
		{ a="a", b="b"},
		{ c="c", d="d"}
	]
	n = toset(local.m)
  */

  /*
  m = 1
  n = 2
  y = local.m == 1 && local.n == 2? 10:0
  */
  /*
  y = [1] * 3
  */
}
data "aws_iam_role" "example" {
  name = "an_example_role_name"
}
locals {
	y = data.aws_iam_role.example.arn
}
