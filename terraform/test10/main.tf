data "aws_availability_zones" "available" {
  state = "available"
}
locals {
	az_count = "${length(data.aws_availability_zones.available.names)}"
	az = data.aws_availability_zones.available.names
}
output az_count {
	value = local.az_count
}

output az {
	value = local.az
}
