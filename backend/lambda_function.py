import json
import boto3
import os

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'BookingTable')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Log the incoming event
        print(f"Received event: {event}")

        # Handle GET request
        if event['httpMethod'] == 'GET':
            response = table.scan()
            items = response.get('Items', [])
            return {
                'statusCode': 200,
                'body': json.dumps(items)
            }

        # Handle POST request
        elif event['httpMethod'] == 'POST' and 'body' in event:
            body = json.loads(event['body'])

            # Validate required fields
            if not all(k in body for k in ('table_id', 'game_system', 'user')):
                raise ValueError("Missing required fields in the payload.")

            # Insert the item into DynamoDB
            table.put_item(Item=body)

            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Booking confirmed'})
            }

        else:
            raise ValueError("Invalid HTTP method or payload.")

    except ValueError as ve:
        print(f"Validation Error: {ve}")
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Bad Request', 'error': str(ve)})
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error'})
        }
