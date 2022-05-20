# python-lambda-ec2
This is a simple python serverless lambda function which would terminate all EC2 instances which don’t follow a tagging criteria. (A free tier AWS account would work). 

### Files intro.

``every-hour-call.py`` - This function would call every 1 hour using cloudWatch and remind the untagged instances with instance id by email.
``terminate.py`` - The terminate function run in every 6 hours using cloudWatch and terminate the instance which don't have Name, Env, Created_By tags.

### Setup in AWS
* Create the instance with a tag like a Name, Environment, and Created_by and without a tag(at least one)
* Setup IAM Roles to lambda function if you don't have(IAM->Access Management->Roles->create_role->lambda->choose lambdaBasicExecutionRole and              ec2fullaccess).    
* During creating lambda function choose to use an existing role from permission and create a function for every hour check. 
* Copy-paste ``every-hour-call.py`` inside this function save and deploy.
* Now you have to be set up the configure test event with an empty JSON payload (e.g { })
* For termination follows the 3, 4, and 5 steps as mentioned above.
* After successful setup of lambda function we have to schedule lambda function using Cloudwatch Event Rules to trigger Lambda for both functions.
    (CloudWatch->Events->Rules->Create Rule->Schedule->Add target(select lambda function)[Create two rules for both function,1 hours rule for every hour call and 6 hours rule for termination.]).
 * In the send_email function in both the files mention verified Amazon simple email service email address.
      [Change Source, ToAddresses email address from send_email function accordingly to your AWS verified email address.]
