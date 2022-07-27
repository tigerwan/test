locals {
    cmd = templatefile("./cmd.txt", {})

}
resource "null_resource" "example1" {
  triggers = {
    always_run = "${timestamp()}"
  }
  provisioner "local-exec" {
    command = "sh ${local.cmd}"
  }
}