# import boto3
# import base64
#
# key_id = 'ecba079a-b954-42ee-a253-5adc46c4902c'
#
#
# def kms_func():
#     session = boto3.session.Session(profile_name='aws_training')
#     client = session.client('kms')
#
#     encryption_result = client.encrypt(KeyId=key_id,
#                                        Plaintext='Hello, KMS!')
#
#     blob = encryption_result['CiphertextBlob']
#     print(base64.b64encode(blob))
#
#     encrypted_text = 'AQICAHhWKW0yE5YlWi4UYGfo9dYbtngzwZY7MhKM2DJKbcgUSAGyr/9mTHl3uMcrel8Plu9UAAAAaTBnBgkqhkiG9w0BBwagWjBYAgEAMFMGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMESh1NWoraCmEbOYuAgEQgCbLHdlUgno8bsQ0uhvBi7wLwQiysT7fzcRojiUI6DyH62zjar6efA=='
#     decrypted_text = client.decrypt(CiphertextBlob=base64.b64decode(encrypted_text))
#     print(decrypted_text['Plaintext'])
#
#
# if __name__ == '__main__':
#     kms_func()
#






