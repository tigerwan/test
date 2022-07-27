import boto3
import logging



logging.getLogger().setLevel(logging.DEBUG)
s3=boto3.client('s3')
try:
	buckets = s3.list_buckets()
	f1()
except Exception as error:
	logging.getLogger().exception(error)
	logging.info("logging done")
	#logging.getLogger().error(error)

