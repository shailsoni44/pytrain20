# import boto3
#
# s3_client = boto3.client('s3')
# s3_client.list_objects_v2(Bucket='awstraining4ss-resized')
#
#
# def get_s3_keys(bucket):
#     """Get a list of keys in an S3 bucket."""
#     keys = []
#     resp = s3_client.list_objects_v2(Bucket=bucket)
#     for obj in resp['Contents']:
#         keys.append(obj['Key'])
#     return keys
#
#
# result = get_s3_keys('awstraining4ss-resized')
# print(result)

import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='myuser', password='mypassword')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

create or replace table largest_countries(
    country_rank number,
    country_name string,
);
