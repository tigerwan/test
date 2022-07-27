output "private_range" {
    value = null_resource.private_netmask_range
}

output "public_subnet" {
    value = null_resource.public_netmask_range
}

output "protect_subnet" {
    value = null_resource.protect_netmask_range
}

