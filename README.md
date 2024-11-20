# Gaming Club Booking System

## Overview
This system allows users to book tables for a gaming club. It includes:
- **Frontend**: Hosted on S3, using a simple HTML/JavaScript app.
- **Backend**: Lambda function with API Gateway.
- **Database**: DynamoDB for storing booking data.
- **CI/CD Pipeline**: CodePipeline for automated deployments.

## Prerequisites
1. **AWS CLI**: Ensure you have the AWS CLI installed and configured with appropriate credentials.
2. **Permissions**: Your AWS account must have permissions to create IAM roles, Lambda functions, DynamoDB tables, and S3 buckets.
3. **ZIP Utility**: Required to package the Lambda code.

---

## Deployment Steps

### **1. Package and Upload Lambda Code**
1. Navigate to the `backend/` directory and create a zip file:
   ```bash
   cd backend/
   zip -r lambda_code.zip .

# gaming-club-booking-system
# gaming-club-booking-system
