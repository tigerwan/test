import boto3
import traceback
if __name__ == '__main__':
    try:
        print("ready!")
        s3 = boto3.client('s3')
        a = s3.get_a_bucket()
    except Exception as e:
        print("this is error: {}".format(e))
        print('this is exception: {}'.format(str(traceback.format_exc())))
    
