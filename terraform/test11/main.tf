variable v_vpc_cidr {
	default = "10.28.224.0/22"
}
locals {

    l_vpc_netmask_number = 22
    l_private_netmask_number = 25
    l_public_netmask_number = 26
    l_protect_netmask_number = 26

	az_count = 3

	cidr_gaps = flatten([
		for i in range(local.az_count): [
			local.l_public_netmask_number - local.l_vpc_netmask_number,
			local.l_private_netmask_number - local.l_vpc_netmask_number,
			local.l_protect_netmask_number - local.l_vpc_netmask_number
		]
	])

	cidr_subnets = cidrsubnets(var.v_vpc_cidr, local.cidr_gaps...)
}
output cidr_gaps {
	value = local.cidr_gaps
}

output cidr_subnets {
	value = local.cidr_subnets
}
