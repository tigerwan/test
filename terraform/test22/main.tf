resource "aws_lambda_permission" "lambda_permission" {
  action        = "lambda:InvokeFunction"
  function_name = "daniel-terraform-lambda"
  principal     = "events.amazonaws.com"
  source_arn    = "arn:aws:events:ap-southeast-2:431525257644:rule/daniel-test-rule"
}

resource "aws_lambda_permission" "lambda_permission2" {
  action        = "lambda:InvokeFunction"
  function_name = "daniel-terraform-lambda"
  principal     = "events.amazonaws.com"
  source_arn    = "arn:aws:events:ap-southeast-2:431525257644:rule/daniel-test-rule2"
}
/*
resource "aws_lambda_permission" "lambda_permission" {
  action        = "lambda:InvokeFunction"
  function_name = "daniel-terraform-lambda"
  principal     = "events.amazonaws.com"
  statement_id  = "rule1"
  source_arn    = ["arn:aws:events:ap-southeast-2:431525257644:rule/daniel-test-rule", "arn:aws:events:ap-southeast-2:431525257644:rule/daniel-test-rule2"]
}
*/
