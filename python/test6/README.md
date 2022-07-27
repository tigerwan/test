# Overview

AWS has no out of box function to deliver CloudWatch events across regions. To consolidate the CloudWatch events across regions to the master region of NDM account, this tool, forwarder, hook to the CloudWatch events of ASG/EC2/RDS in non-master region, write events to the master region of the same account. Afterward, the CloudWatch rule in master region streams the events to NDM account's master region, which trigger the lambda in NDM account to retrieve ASG/EC2/RDS latest details.


In the event transition, the lambda add the prefix "awsgo." to the event "source" field, e.g. the lambda receives a event which comes from the source of "aws.rds", lambda would duplicate the event to the master region but change the source to "awsgo.aws.rds" as AWS blocks using the reserved soruce name, such as "aws.rds".

At present, the lambda tied with the following CloudWatch events in the non-mater region

```
{
  "detail-type": [
    "EC2 Instance State-change Notification",
    "RDS DB Instance Event",
    "EC2 Instance Launch Successful",
    "EC2 Instance Terminate Successful",
    "EC2 Instance Launch Unsuccessful",
    "EC2 Instance Terminate Unsuccessful",
    "EC2 Instance-launch Lifecycle Action",
    "EC2 Instance-terminate Lifecycle Action"
  ],
  "source": [
    "aws.ec2",
    "aws.rds",
    "aws.autoscaling"
  ]
}
```

```
{
  "detail-type": [
    "Tag Change on Resource"
  ],
  "source": [
    "aws.tag"
  ],
  "detail": {
    "service": [
      "ec2",
      "rds"
    ],
    "resource-type": [
      "instance",
      "db"
    ]
  }
}
```

```
{
  "detail-type": [
    "AWS API Call via CloudTrail"
  ],
  "source": [
    "aws.rds",
    "aws.autoscaling"
  ],
  "detail": {
    "eventSource": [
      "autoscaling.amazonaws.com",
      "rds.amazonaws.com"
    ],
    "eventName": [
      "DeleteAutoScalingGroup",
      "DeleteDBInstance"
    ]
  }
}
```

In the master region, there is no lambda but CloudWatch event rules only. Apart from the above event rules, there is one more rule in the master region for receiving all AWSGo events from non-mater region


```
{
  "source": [
    "awsgo.aws.tag",
    "awsgo.aws.ec2",
    "awsgo.aws.rds",
    "awsgo.aws.autoscaling"
  ]
}
```

# Lambdas

* awsgo-cache-forwarder-prod-eventforwarder


# Library dependencies

* http://bitbucket.news.com.au/scm/automation/autolib_aws.git

* http://bitbucket.news.com.au/scm/automation/autolib_comm.git

* http://bitbucket.news.com.au/scm/automation/autolib_local_repo.git


In AWS, the above libraries have been built into lambda layers in NDM Account master region(ap-southeast-2) which is referenced by the AWSG lamabdas

* auutolib_aws

* autolib_comm

* autolib_local_repos


# Deployment

* If you would like to deloy to a single region, you may use serverless framework

    * Set the AWS credentail of the target account

    * If you have not installed [serverless framework](https://serverless.com/) on our desktop, install it.

    ```
    npm install -g serverless
    ```

    * roll out to Shared account

    ```
    sls deploy -s prod --region <region name>
    ```

* If you would like to deploy to massive accounts and regions, you may either run the above serverless framework one region after another one, or use Bamboo piepline url as follows.

    * http://bamboo.news.com.au/browse/AUTOMATION-AWSGOREFRESHER

    Please note this approach create a StackSet per region to deploy the lambda and CloudWatch event rules, which uses "ops-prod-regions" and "ops-stack-set" Dynamodb tables as deployment configuration store
