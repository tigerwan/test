variable "vpc_cidr" {
  default = "172.29.0.0/21"
}

variable "az_counts" {
  default = 2
}

variable "private_netmask" {
  default = "/24"
}


variable "public_netmask" {
  default = "/25"
}

variable "protect_netmask" {
  default = "/25"
}