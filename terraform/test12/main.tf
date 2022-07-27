data "aws_subnet" "test_subnet" {
  tags = {
    Name = "subnet2_vpc2"
  }
}

data "aws_vpc" "test_vpc" {
    id = data.aws_subnet.test_subnet.vpc_id
}

resource "aws_network_acl" "test_nacl" {
    vpc_id = data.aws_subnet.test_subnet.vpc_id

    subnet_ids = [data.aws_subnet.test_subnet.id]

}

resource "aws_network_acl_rule" "test_nacl_rule" {
    network_acl_id = aws_network_acl.test_nacl.id
    rule_number    = 1200
    egress         = false
    protocol       = -1
    rule_action    = "allow"
    cidr_block     = data.aws_vpc.test_vpc.cidr_block
}

resource "aws_network_acl_rule" "test_nacl_rule2" {
    network_acl_id = aws_network_acl.test_nacl.id
    rule_number    = 1500
    egress         = false
    protocol       = -1
    rule_action    = "allow"
    cidr_block     = data.aws_vpc.test_vpc.cidr_block
}

output subnet_id {
	value = data.aws_subnet.test_subnet.id
}
