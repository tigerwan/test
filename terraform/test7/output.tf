output "role_name" {
    value = [for r in aws_iam_role.sample_roles : r.name]
}



