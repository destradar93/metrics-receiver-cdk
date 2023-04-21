import json
import os
from decimal import Decimal

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])


def lambda_handler(event, context):
    print(event)

    for record in event['Records']:
        payload = json.loads(record['body'])

        # Convert any float values in the payload to Decimal types
        for key, value in payload.items():
            if isinstance(value, float):
                payload[key] = Decimal(str(value))

        table.put_item(Item={"deviceId": payload['deviceId'], "timestamp": payload['timestamp'], "payload": payload})
