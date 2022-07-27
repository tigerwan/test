variable event_rule {
	/*
	default = [
	{
		"name": "test-rule-1",
		"description" : "test rule 1",
		"schedule_expression" : "cron(0 1 * * ? *)",
		"is_enabled": false,
		"input": {
			"k1" : "v1"
			"k2" : "v2"
		}
	},
	{
		"name": "test-rule-2",
		"description" : "test rule 2",
		"schedule_expression" : "cron(0 2 * * ? *)",
		"is_enabled": false,
	}
	]
	*/
	default = 	{
		"name": "test-rule-1",
		"description" : "test rule 1",
		"schedule_expression" : "cron(0 1 * * ? *)",
		"is_enabled": false,
		"input": {
			"k1" : "v1"
			"k2" : "v2"
		}
	}
}

locals {
	lambda_function_arn = "arn:aws:lambda:ap-southeast-2:431525257644:function:event-test"
	lambda_function_name = "event-test"
	/*
	new_event_rules = [for index in range(length(local.event_rules)): lookup(local.event_rules[index], "name", null) == null ? merge(local.event_rules[index], {"name": "hehe-event-rule-${index}"}) : local.event_rules[index]]
	*/
	/*
	new_event_rules = [for rule in local.event_rules: lookup(rule, "name", null) == null ? merge(rule, {"name": "hehe-event-rule-${index(local.event_rules, rule) + 1}"}) : rule]
	*/
}

module "cw_rule" {
	source = "./modules/aws_lambda_cloudwatch_event_trigger"
	lambda_function_arn = local.lambda_function_arn
	lambda_function_name = local.lambda_function_name
	event_rule = var.event_rule
}

/*
output new_event_rules {
	value = local.new_event_rules
}
*/