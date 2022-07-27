variable az {
  default = 2
}

locals {
  subnet_cidr = ["10.50.0.0/24", "10.50.1.0/24", "10.50.2.0/24"]
}

resource "null_resource" "az_list" {
  count = var.az

  triggers = {
	  cidr 		= local.subnet_cidr[count.index]
  }
}

resource "aws_subnet" "test_subnet" {
  for_each = toset(null_resource.az_list.*.triggers.cidr)
  vpc_id     = "vpc-3dbfc65a"
  cidr_block = each.value
}

/*
resource "aws_route_table" "test_rb" {
  vpc_id = "vpc-3dbfc65a"
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "igw-024ea667"
  }
  lifecycle {
    ignore_changes = all
  }
}

locals {
  subnets = toset([for s in aws_subnet.test_subnet: s.id])
}

resource "aws_route_table_association" "test_rb_assocaiate" {
  for_each = local.subnets
  subnet_id      = each.key
  route_table_id = aws_route_table.test_rb.id
}
*/
