__author__ = 'imroot <chougale.amrut@gmail.com>'

import boto3
import json
import pdb


class IAM(object):
    def __init__(self):
        self.iamResouce = boto3.resource("iam")
        self.iamClient = boto3.client("iam")
        # pass

    def createPolicyDocument(self, **kwargs):
        policy = """{
      "Version": "2012-10-17",
      "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "Service": "ec2.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
            }
        ]
    }
    """
        return policy

    def createRole(self, **kwargs):
        assumeRolePolicyDocument = self.createPolicyDocument()

        # create a Role with specified policy
        try:
            res = self.iamClient.create_role(Path=kwargs["path"], RoleName=kwargs["roleName"],
                                             AssumeRolePolicyDocument=assumeRolePolicyDocument)
        except Exception as e:
            raise
        else:
            return res

    def attachManagedPolicyToRole(self, **kwargs):
        try:
            res = self.iamClient.attach_role_policy(RoleName=kwargs["roleName"], PolicyArn=kwargs["policyArn"])
        except Exception:
            raise
        else:
            return True

    def updateAssumeRolePolicy(self, **kwargs):
        RoleName = kwargs["roleName"]
        PolicyDocument = self.createPolicyDocument()

        # attach the role policy
        try:
            res = self.iamClient.update_assume_role_policy(RoleName=RoleName, PolicyDocument=PolicyDocument)
        except Exception as e:
            raise
        else:
            return res

    def createInstanceProfile(self, **kwargs):
        try:
            instProfile  = self.iamClient.create_instance_profile(InstanceProfileName=kwargs["instanceProfileName"],Path=kwargs["path"])        
        except Exception:
            raise
        else:
            return True

    def addRoleTOInstanceProfile(self, **kwargs):
        try:
            res = self.iamClient.add_role_to_instance_profile(InstanceProfileName=kwargs["instanceProfileName"],RoleName=kwargs["roleName"])
        except Exception:
            raise
        else:
            return True


# ret = IAM()

# ret.createRole(Path = "/",RoleName="Test_amrut_role1")
# ret.updateAssumeRolePolicy()

# print ret
