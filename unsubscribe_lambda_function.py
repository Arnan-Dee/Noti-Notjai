import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('sns')
    TopicArn = 'arn:aws:sns:ap-northeast-1:502983918849:Test-101'
    event = json.loads(event['body'])
    email = event['email']

    response = client.list_subscriptions_by_topic(
        TopicArn=TopicArn,
    )
    print(response)

    # there is no email subscribe to our joke. Return not registered.
    if len(response['Subscriptions']) == 0:
        print("there is no email subscribed")
        return {
            'statusCode': 200,
            'body': json.dumps(f'There is no email subscribed')
        }

    for sub in response['Subscriptions']:
        if sub['Endpoint'] == email:
            sub_Arn = sub['SubscriptionArn']
            if sub_Arn == 'PendingConfirmation':

                print(f'{email} is still in pending state.')
                return {
                    'statusCode': 200,
                    'body': json.dumps(f'{email} is still in pending state. Just ignore the confimation message. You are not recieveing a JOKE form us.')

                }
            else:
                # we found the email to unsub
                unsub_response = client.unsubscribe(
                    SubscriptionArn=sub_Arn
                )
                print(
                    f"sub_Arn = {sub_Arn}, email = {email} unsub sucessfully")
                return {
                    'statusCode': 200,
                    'body': json.dumps(f"Your email({email}) has sucessfully unsubcribed to our JOKEs :(")
                }

    print("we cannot found email in sub list")

    return {
        'statusCode': 200,
        'body': json.dumps("We cannot found email in subcription list. Make sure you provide the right email.")
    }
