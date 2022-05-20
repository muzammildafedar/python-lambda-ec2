import json
import boto3

def lambda_handler(event, context):
	ec2 = boto3.resource('ec2',"us-east-1")
	instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
	instanceDontHaveTag = []
	for instance in instances:
		if instance.tags == None:
		    instance.terminate()
		    instanceDontHaveTag.append(instance.id)
		else:
		    print("There is no instance without tag")
	if len(instanceDontHaveTag) > 0 :
			send_email(instanceDontHaveTag)
	
	
	
		    
def send_email(instanceId):
    ses = boto3.client('ses')
    body = """
	   The following the instance has been terminated 
    """ +str(instanceId)

    ses.send_email(
	    Source = '120cs15024@gmail.com',
	    Destination = {
		    'ToAddresses': [
			    '120cs15024@gmail.com'
		    ]
	    },
	    Message = {
		    'Subject': {
			    'Data': 'Alert',
			    'Charset': 'UTF-8'
		    },
		    'Body': {
			    'Text':{
				    'Data': body,
				    'Charset': 'UTF-8'
			    }
		    }
	    }
    )
    
