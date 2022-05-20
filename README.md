# python-lambda-ec2
This is a simple python serverless lambda function which would terminate all EC2 instances which don’t follow a tagging criteria. (A free tier AWS account would work). 

## Files intro.

``every-hour-call.py`` - This function would call every 1 hour using cloudWatch and remind the untagged instances with instance id by email.
``terminate.py`` - The terminate function run in every 6 hours using cloudWatch and terminate the instance which don't have Name, Env, Created_By tags.

