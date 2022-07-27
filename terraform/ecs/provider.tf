
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}
provider "aws" {

  region = "ap-southeast-2"
  default_tags {
    tags = {
      company     = "nct"
      owner       = "daniel.wan@news.com.au"
      environment = "dev"
      business    = "nie"
      product     = "poc"
    }
  }
}
