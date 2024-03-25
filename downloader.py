import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'sourabh13062023'
    key = 'lambda_package22.zip'
    local_file_path = '/tmp/lambda_package22.zip'
    
    # Download the file from S3
    try:
        s3.download_file(bucket_name, key, local_file_path)
        print("File downloaded successfully from S3")
        
        # Process the file as needed
        with open(local_file_path, "r") as file:
            # Process the file content
            pass
        
        return {
            "statusCode": 200,
            "body": "File downloaded and processed successfully"
        }
    except Exception as e:
        print(f"Error downloading file from S3: {str(e)}")
        return {
            "statusCode": 500,
            "body": "Error downloading file from S3"
        }
