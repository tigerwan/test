locals {
    myfile = file("${path.module}/test.txt")
    mylist = split("\n", local.myfile)
    data = split(";", join(" ", local.mylist))
}

resource "null_resource" "example1" {
  triggers = {
    always_run = timestamp()
  }
  count = length(local.data)
  provisioner "local-exec" {
    command = "echo ${local.data[count.index]}"
  }
}