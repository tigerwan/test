locals {
	vpc_netmask_number = tonumber(regex(".*/(\\d+)", var.vpc_cidr)[0])
	private_netmask_number = tonumber(regex(".*/(\\d+)", var.private_netmask)[0])
	public_netmask_number = tonumber(regex(".*/(\\d+)", var.public_netmask)[0])
	protect_netmask_number = tonumber(regex(".*/(\\d+)", var.protect_netmask)[0])
	az_list = ["a", "b", "c"]

	/* compute private subnet block*/
	private_netmask = {
		newbits = local.private_netmask_number - local.vpc_netmask_number
		block_base = 0
	}

	/* allocate the spare block that private did not use to to public subnet */
	public_netmask = {
		newbits = local.public_netmask_number - local.vpc_netmask_number
		block_base = (local.private_netmask.block_base + var.az_counts) * pow(2, local.public_netmask_number - local.private_netmask_number)
	}

	/* allocate the spare block that public did not use to protect subnet */
	protect_netmask = {
		newbits = local.protect_netmask_number - local.vpc_netmask_number
		block_base = (local.public_netmask.block_base + var.az_counts) * pow(2, local.protect_netmask_number - local.public_netmask_number)
	}

}

resource "null_resource" "private_netmask_range" {
  count = var.az_counts

  triggers = {
	/*
	vpc_cidr 	= var.vpc_cidr
    newbits     = local.private_netmask.newbits
	netnum	    = local.private_netmask.block_base + count.index
	*/
	block 		= cidrsubnet(var.vpc_cidr, local.private_netmask.newbits, local.private_netmask.block_base + count.index)
  }
}

locals {
	new_priv_map = { for i in range(var.az_counts): "az_${element(local.az_list, i)}" => cidrsubnet(var.vpc_cidr, local.private_netmask.newbits, local.private_netmask.block_base + i) }
}
output "new_priv_map" {
	value = local.new_priv_map
}
resource "null_resource" "public_netmask_range" {
	depends_on = [null_resource.private_netmask_range]
  count = var.az_counts

  triggers = {
	/*
	vpc_cidr 	= var.vpc_cidr
    newbits     = local.public_netmask.newbits
	pnetnum	    = local.public_netmask.block_base + count.index
	*/
	block 		= cidrsubnet(var.vpc_cidr, local.public_netmask.newbits, local.public_netmask.block_base + count.index)
  }
}

resource "null_resource" "protect_netmask_range" {

	depends_on = [null_resource.public_netmask_range]
  count = var.az_counts

  triggers = {
	/*
	vpc_cidr 	= var.vpc_cidr
    newbits     = local.protect_netmask.newbits
	pnetnum	    = local.protect_netmask.block_base + count.index
	*/
	block 		= cidrsubnet(var.vpc_cidr, local.protect_netmask.newbits, local.protect_netmask.block_base + count.index)
  }
}