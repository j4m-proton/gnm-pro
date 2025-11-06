import boto3

session = boto3.session.Session()

s3 = session.client(
    's3',
    region_name='fra1',
    endpoint_url='https://fra1.digitaloceanspaces.com',
    aws_access_key_id='DO80177H8LUGKRC99Y8G',
    aws_secret_access_key='aX/0DFlyYiyczEnAsM7NjtMVuOaVz/Fv3jrzetTllYs'
)

# Jaribu kuorodhesha buckets zako
print(s3.list_buckets())
