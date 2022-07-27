resource "aws_network_acl_rule" "test_nacl_rule" {
    network_acl_id = "acl-0e9c95fa1e96f3789"
    rule_number    = 2000
    egress         = false
    protocol       = -1
    rule_action    = "deny"
    cidr_block     = "172.17.10.0/28"
}

output nacl_id {
	value = aws_network_acl_rule.test_nacl_rule.id
}
