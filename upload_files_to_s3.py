'''libraries'''
import boto3
from botocore.client import Config

'''inputs for file and bucket name'''
print("hey!! kindly provide the file name that you want to upload on s3: ",end="")
str=input()
print("kindly provide the s3 Bucket name: ",end="")
BUCKET_NAME=input() 

'''Credentials'''
ACCESS_KEY = ''
SECRET_KEY = ''
           
'''Opening binary File'''
data = open(str, 'rb')
    
'''Accessing the bucket'''
s3 = boto3.resource( 's3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY,config=Config(signature_version='s
3v4')) 
s3.Bucket(BUCKET_NAME).put_object(Key=str, Body=data)
    
print ("Successfully Uploaded")
