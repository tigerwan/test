resource "aws_dynamodb_table_item" "configuration_region" {
    table_name = "ops-prod-awsregions"
    hash_key = "accountId"
    item = <<ITEM
{
    "accountId": { "S": "1234567890" },
    "regions":  { "L": [{ "S": "ap-southeast-1" }]}
}
ITEM
}