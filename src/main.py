__author__ = 'imroot <chougale.amrut@gmail.com>'

from src.commonLib.lib import *

from src.S3Lib import S3Lib
from src.EC2Lib import EC2Lib
from src.IAMLib import IAMLib
from src.RDSLib import RDSLib

#import json

def main():

    # S3 bucket 
    s3Obj  = S3Lib.S3()
    ec2Obj = EC2Lib.EC2()
    iamObj = IAMLib.IAM()

    # create S3 Bucket
    # try:
    #   response = s3Obj.createBucket(bucketName="amrut-test-buck-automation1", Region="EU")
    # except Exception:
    #   raise
    # else:
    #   print("Successfully Created S3 bucket [ %s ]" % bucketName)

    # Get bucketACL
    # try:
    #     response = s3Obj.getBucketACL(bucketName="amrut-test-buck-automation1")
    # except Exception:
    #     raise
    # else:
    #     print("ACL for bucket are: %s" % response)

    # Get all instances IDs
    # allInstanceIds = ec2Obj.getAllInstanceIds()
    # print(allInstanceIds)

    # create Role and update policy
    # response = iamObj.createRole(Path = "/",RoleName="Test_amrut_role1")
    # response = iamObj.updateAssumeRolePolicy(RoleName="Test_amrut_role1",)

    # Test Objects if it work
    #test = s3Obj.testS3()
    #print (test)

    # # Create Role, update assume policy, create Instance Profile, add role to instance profile
    #res = iamObj.createRole(path="/", roleName="Test_amrut_role1")
    #res = iamObj.attachManagedPolicyToRole(roleName="Test_amrut_role1", policyArn="arn:aws:iam::aws:policy/AmazonS3FullAccess")
    #res = iamObj.updateAssumeRolePolicy(roleName="Test_amrut_role1")
    #res = iamObj.createInstanceProfile(path="/",instanceProfileName="instance_test_amrut_profile")
    #res = iamObj.addRoleTOInstanceProfile(instanceProfileName="instance_test_amrut_profile",  roleName="Test_amrut_role1")

    # # create a security group and configure ports in it
    # ec2SecObj = EC2Lib.EC2security()
    # secGroupIdWeb = ec2SecObj.createSecurityGroup(groupName="test_amrut_sec_group_web", description="security group for WEB by Amrut", vpcID="vpc-362a2851")
    # print ("Security Group created successfully and GroupID is %s !\n\n" % secGroupIdWeb)
    # res = ec2Obj.tagResources(resources=[secGroupIdWeb], tags=[{"Key":"Name","Value":"Amrut_security_group_automated"}])
    # res = ec2SecObj.ingressRulesTOSecurityGroup(groupID=secGroupIdWeb, ipProtocol="tcp", fromPort=22, toPort=22, cidr="0.0.0.0/0")
    # res = ec2SecObj.ingressRulesTOSecurityGroup(groupID=secGroupIdWeb, ipProtocol="tcp", fromPort=80, toPort=80, cidr="0.0.0.0/0")
    #
    # # Create RDS security Group
    # secGroupIdRds = ec2SecObj.createSecurityGroup(groupName="test_amrut_sec_group_rds", description="security group for RDS by Amrut", vpcID="vpc-362a2851")
    # print ("Security Group created successfully and GroupID is %s !\n\n" % secGroupIdRds)
    # res = ec2Obj.tagResources(resources=[secGroupIdRds], tags=[{"Key":"Name","Value":"Amrut_security_group_automated_RDS"}])
    # res = ec2SecObj.ingressRulesTOSecurityGroup(groupID=secGroupIdRds,ipProtocol="tcp",fromPort=3306,toPort=3306, targetSecurityGroupId=secGroupIdRds )
    # print ("Security group ingress rules are updated for security group %s" % secGroupIdRds)

    #create a VPC with user input
    ########################
    '''
    ec2netObj = EC2Lib.EC2Networking()
    resVPCOp = ec2netObj.createVPC(dryRun = False,
                                   cidrBlock = "10.10.0.0/18",
                                   instanceTenancy = "default",
                                   amazonProvidedIpv6CidrBlock = False)
    # print (resVPCId)
    vpcID = resVPCOp["Vpc"]["VpcId"]
    print("VPC is being created with VPC ID: %s" % vpcID)
    tagVPC = ec2Obj.tagResources(resources=[vpcID], tags = [{"Key":"Name", "Value":"Amrut_VPC_auto1"}])
    print("VPC is being tagged properly!")

    # create subnet in given VPC
    resSubnetOp = ec2netObj.createSubnet(dryRun=False,vpcId=vpcID, cidrBlock="10.10.10.0/24")
    subnetID1 = resSubnetOp["Subnet"]["SubnetId"]
    print ("Subnet is created properly with subnet ID: %s" % subnetID1)
    tagSubnet = ec2Obj.tagResources(resources=[subnetID1], tags = [{"Key": "Name", "Value":"Amrut_subnet_auto1"}])
    print ("Subnet has been tagged properly")

    resSubnetOp = ec2netObj.createSubnet(dryRun=False,vpcId=vpcID, cidrBlock="10.10.20.0/24",availabilityZone="us-east-1b")
    subnetID2 = resSubnetOp["Subnet"]["SubnetId"]
    print ("Subnet is created properly with subnet ID: %s" % subnetID2)
    tagSubnet = ec2Obj.tagResources(resources=[subnetID2], tags = [{"Key": "Name", "Value":"Amrut_subnet_auto2"}])
    print ("Subnet has been tagged properly")

    #Create an RDS instance and tag it
    rdsObj = RDSLib.RDS()
    resRDSOps = rdsObj.createRDSSecurityGroup(dbSecGroupName="Amrut-RDS-sec-grp-1", dbSecGroupDescription="Amrut-auto security group for RDS",subnetIDs=[subnetID1,subnetID2], tags=[{"Key":"Name","Value":"Amrut RDS sec group"}])
    '''
    #print (ec2Obj.EC2Client.describe_instances())

# Call the main function
if __name__ == "__main__":
    main()
