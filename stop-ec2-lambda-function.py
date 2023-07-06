import boto3
region = 'Aws-region'
instances = ['instances-id-1', 'instances-id-2']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('Instances stopped: ' + str(instances))
