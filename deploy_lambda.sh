#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Load environment variables from a .env file if it exists
if [ -f .env ]; then
  source .env
else
  echo "Error: .env file not found. Create a .env file with BUCKET_NAME and LAMBDA_CODE_PATH variables."
  exit 1
fi

# Ensure all required environment variables are set
if [ -z "$BUCKET_NAME" ] || [ -z "$LAMBDA_CODE_PATH" ]; then
  echo "Error: BUCKET_NAME or LAMBDA_CODE_PATH environment variable is not set."
  exit 1
fi

# Zip the Lambda function code
echo "Zipping Lambda code..."
zip -r lambda_code.zip "$LAMBDA_CODE_PATH"

# Upload the Lambda code to the S3 bucket
echo "Uploading Lambda code to S3 bucket: $BUCKET_NAME"
aws s3 cp lambda_code.zip s3://$BUCKET_NAME/

# Clean up local zip file
rm lambda_code.zip

echo "Lambda code deployment completed successfully!"
