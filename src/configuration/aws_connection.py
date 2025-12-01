import boto3

from src.constants import AWS_REGION_NAME


class S3Client:
    """This class creates a connection with s3 bucket"""

    s3_client=None
    s3_resource = None

    def __init__(self, region_name=AWS_REGION_NAME):
        """ 
        This class uses Boto3's default credential provider chain 
        to connect with S3.
        """
        if S3Client.s3_resource==None or S3Client.s3_client==None:        
            S3Client.s3_resource = boto3.resource('s3', region_name=region_name)
            S3Client.s3_client = boto3.client('s3', region_name=region_name)

        self.resource = S3Client.s3_resource
        self.client = S3Client.s3_client