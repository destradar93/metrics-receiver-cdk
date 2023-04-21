import json
import os

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])


def lambda_handler(event, context):
    print(event)

    for record in event['Records']:
        payload = json.loads(record['body'])

        table.put_item(Item={"deviceId": payload['deviceId'], "timestamp": payload['timestamp'], "payload": payload})
