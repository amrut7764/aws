__author__ = 'imroot <chougale.amrut@gmail.com>'

import boto3
import json
import pdb


class S3(object):
    """Class for S3 related operations

    """

    def __init__(self):
        # Get the s3 resource
        s3_resource = boto3.resource("s3")
        self.resource = s3_resource

        # Get low level access to resources using client
        s3_client = boto3.client("s3")
        self.client = s3_client

    # Create S3 bucket
    def createBucket(self, **kwargs):
        """
        Creates S3 bucket in specified region, default is us-east-1
        :param kwargs:
        :param bucketName: Name of the bucket in small letters
        :param region: Region name in which bucket needs to be created
        :param ACL: Access Control List to make authorization for the bucket, default "private"
        :return: API response
        """
        # bucketName = kwargs.get(bucketName, None)
        bucket = kwargs.get("bucketName", None)
        region = kwargs.get("Region", "us-east-1")
        print(region)
        ACL = kwargs.get("ACL", "private")
        if any(x is None for x in [bucket]):
            raise Exception("Any of the mandatory parameters [bucketName] should not be None")
        try:
            bucketResponse = self.client.create_bucket(Bucket = bucket,
                                               CreateBucketConfiguration = {'LocationConstraint': region}, ACL = ACL)
        except Exception as e:
            raise
        return bucketResponse

    # Get Bucket ACL
    def getBucketACL(self, bucketName):
        # pdb.set_trace()
        """

        :param bucketName:
        :return:
        """
        try:
            response = self.client.get_bucket_acl(Bucket = bucketName)
        except Exception as e:
            raise
        else:
            return response

    # Put Object to the S3 bucket
    def uploadObjToBucket(self, **kwargs):
        bucketName = kwargs.get("Bucket", None)
        key = kwargs.get("Key", None)
        fileName = kwargs.get("Filename", None)
        ExtraArgs= kwargs.get("ExtraArgs", None)
        Callback = kwargs.get("Callback",None)
        Config = kwargs.get("Config", None)
        if any(x is None for x in [bucketName, fileName, key]):
            raise Exception("Any of the mandatory parameters should not be None")
        try:
            response = self.resource.Object(bucketName, key).upload_file(fileName)
        except Exception as e:
            raise
        else:
            return True

    # Delete Bucket
    def deleteBucket(self, bucketName):
        try:
            bucketObj = self.resource.Bucket(bucketName)
        except Exception as e:
            raise
        else:
            try:
                bucketObj.delete()
            except Exception as e:
                raise
            else:
                return True

    def testS3(self):
        # pdb.set_trace()
        buck = []
        buckets = self.resource.buckets.all()
        for bucket in buckets:
            buck.append(bucket.name)
