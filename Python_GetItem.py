import boto3
from boto3.dynamodb.conditions import Key
import json

def lambda_handler(event, context):
  client = boto3.resource('dynamodb')
  table = client.Table('<Your Table>')


  response = table.get_item(

    Key={
    '<PartitionKey>':'<Value>',
    '<SortKey>':'<Value'
    }
  )
  print(response['Item'])

  response = table.query(
		KeyConditionExpression=Key('<PartitionKey>').eq('<VALUE>') & Key('<SortKey>').gt('<VALUE>')
	)

	items = response['Items']
	for item in items:
		print(item)

