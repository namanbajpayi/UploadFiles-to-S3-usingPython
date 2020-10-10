# UploadFiles-to-S3-usingPython
With the help of Boto3 module we are going to upload files from ec2 instance to S3 bucket

Steps:
1. setup ec2 linux machine and s3 on aws with 1 IAM user
2. save access_key and secret_key of IAM user (you have to use these in the python code provided for accessing the s3 bucket)
3. Install python3 and pip3 on your instance
4. install boto3 python module using pip (pip3 install boto3)
5. Recommended: put your files or images in the same folder of python file provides
6. make python file executable ( chmod +x upload_files_to_s3.py)
7. Run the file (./upload_files_to_s3.py)

Thank you!!!
