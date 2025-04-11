import aws
import from Iam changed from AWS
client=boto3.client('ec2')
response = client.terminate_instances(
    InstanceIds=[
        'i-08d6586bed5f5e9c4',
        KeyName= "devops"
    ],

)
