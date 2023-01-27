import json
import boto3

client = boto3.client('iot-data', region_name='us-east-2')

def lambda_handler(event, context):
    response = client.publish(
        topic='devduck001/duck/on',
        qos=0,
        payload="quack")
    )
    print(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Quack!')
    }
