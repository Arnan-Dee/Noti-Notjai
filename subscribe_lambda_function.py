import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('sns')
    TopicArn = 'arn:aws:sns:ap-northeast-1:502983918849:Test-101'
    print(event)
    event = json.loads(event['body'])
    print(event)
    email = event['email']
    response = client.subscribe(
        TopicArn=TopicArn,
        Protocol='email',
        Endpoint=email
    )

    return {
        'statusCode': 200,
        'body': json.dumps(f'''{email} just subscribe to our JOKES. We just sent you an email confirmation to your inbox. Please check your email.Once you confirmed. You are all set. You can exit this application and wait for our JOKEs!''')
    }
