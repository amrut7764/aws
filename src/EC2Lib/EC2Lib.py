__author__ = 'imroot <chougale.amrut@gmail.com>'

import boto3
import json
import pdb
from src.commonLib.lib import *

class EC2():

    def __init__(self, region=None):

        if region == None:
            region_name = "us-east-1"

        # create an ec2 resource object
        self.EC2Resource = boto3.resource("ec2")
        # create an ec2 client object
        self.EC2Client = boto3.client("ec2",region_name=region)

    def getAllInstanceIds(self):
        listInstanceID = []
        allInstances = self.EC2resource.instances.all()
        print (list(allInstances))
        #for i in list(allInstances):
        #    print i['id']
        #for key in allInstances:
        #    print key
            #for inst in key['Instances']:
            #     listInstanceID.append(inst['InstanceId'])
        return listInstanceID

    def tagResources(self, **kwargs):
        _resources = kwargs["resources"]
        _tags = kwargs["tags"]
        _dryRun = kwargs.get("dryRun", False)
        if not type(_resources) is list or not type(_tags) is list:
            raise Exception("Resources and tags needs to be list of elements")
        try:
            res = self.EC2Client.create_tags(DryRun=_dryRun,Resources=_resources,Tags=_tags)
        except Exception:
            raise
        else:
            return True

class EC2security(EC2):

    def getSecurityGroups(self):
        pass

    def createSecurityGroup(self, **kwargs):
        _groupName = kwargs.get("groupName")
        _description = kwargs.get("description")
        _vpcID = kwargs.get("vpcID")
        _dryRun = kwargs.get("dryRun", False)

        if _groupName is None or _description is None:
            raise Exception("For creation of Security Group, mandatory parameters are groupName, \
                                description and for EC2-VPC, vpcID is also mandatary")
        try:
            response = self.EC2Client.create_security_group(DryRun=_dryRun,
                                                            GroupName=_groupName,
                                                            Description=_description,
                                                            VpcId=_vpcID)
        except Exception:
            raise
        else:
            if response["ResponseMetadata"]['HTTPStatusCode'] == 200:
                return response["GroupId"]
            
    def ingressRulesTOSecurityGroup(self, **kwargs):
        _dryRun = kwargs.get("dryRun", False)
        _groupName = kwargs.get("groupName",None)
        _groupID = kwargs.get("groupID")
        #_sourceSecGrpName = kwargs.get("sourceSecGrpName", None)
        #_sourceSecGrpID = kwargs.get("sourceSecGrpID", None)
        _ipProtocol = kwargs.get("ipProtocol", None)
        _fromPort = kwargs.get("fromPort", "-1")
        _toPort = kwargs.get("toPort","-1")
        _cidr = kwargs.get("cidr",None)
        _targetSecurityGroupId = kwargs.get("targetSecurityGroupId", None)

        try:
            if(_cidr is None) and ( _targetSecurityGroupId is None):
                raise Exception("Either set CIDR or TargetSecurityGroup")
            elif(_targetSecurityGroupId is not None):
                _userIDGroupPairs = {'GroupId': _targetSecurityGroupId}
                _ipPermissions = { 'IpProtocol': _ipProtocol,
                                   "FromPort": _fromPort,
                                   "ToPort":_toPort,
                                   'UserIdGroupPairs': [_userIDGroupPairs]}

                res = self.EC2Client.authorize_security_group_ingress(DryRun=_dryRun,
                                                                      GroupId=_groupID,
                                                                      IpPermissions= [_ipPermissions])
            elif(_cidr is not None):
                res = self.EC2Client.authorize_security_group_ingress(DryRun=_dryRun,
                                                                      GroupId=_groupID,
                                                                      IpProtocol=_ipProtocol,
                                                                      FromPort=_fromPort,
                                                                      ToPort=_toPort,
                                                                      CidrIp=_cidr)
        except Exception:
            raise
        else:
            return True

class EC2Networking(EC2):

    def createVPC(self, **kwargs):
        _dryRun = kwargs.get("dryRun", False)
        _cidrBlock = kwargs.get("cidrBlock",False)
        _instanceTenancy = kwargs.get("instanceTenancy", "default")
        _amazonProvidedIpv6CidrBlock = kwargs.get("amazonProvidedIpv6CidrBlock", False)

        if(_cidrBlock is False):
            raise Exception("CIDR block for VPC should not be blank")
        try:
            resVpc = self.EC2Client.create_vpc(DryRun= _dryRun,
                                               CidrBlock = _cidrBlock,
                                               InstanceTenancy = _instanceTenancy,
                                               AmazonProvidedIpv6CidrBlock = _amazonProvidedIpv6CidrBlock)
        except Exception:
            raise
        else:
            return resVpc

    def createSubnet(self, **kwargs):
        _dryRun = kwargs.get("dryRun", False)
        _vpcId = kwargs.get("vpcId", False)
        _cidrBlock = kwargs.get("cidrBlock", False)
        _ipv6CidrBlock = kwargs.get("ipv6CidrBlock", None)
        _availabilityZone = kwargs.get("availabilityZone",None)

        if(_vpcId is False) or (_cidrBlock is False):
            raise Exception("VPC ID and CIDR block are mandatory for subnet creation!")

        defaultArr = {"dryRun": False}
        mandatoryArr = ["vpcId","cidrBlock" ]
        kwargs = validate(defaultArgs=defaultArr,mandatoryArgs=mandatoryArr,kwargs=kwargs)
        try:
            resSubnet = self.EC2Client.create_subnet(**kwargs)

        # try:
        #     if(_ipv6CidrBlock is None) and (_availabilityZone is None):
        #         resSubnet = self.EC2Client.create_subnet(DryRun = _dryRun,
        #                                              VpcId = _vpcId,
        #                                              CidrBlock = _cidrBlock)
        #         return resSubnet
        #
        #     elif (_ipv6CidrBlock is None) and (_availabilityZone is not None):
        #         resSubnet = self.EC2Client.create_subnet(DryRun = _dryRun,
        #                                              VpcId = _vpcId,
        #                                              CidrBlock = _cidrBlock,
        #                                                AvailabilityZone = _availabilityZone)
        #         return resSubnet
        #
        #     elif (_ipv6CidrBlock is not None) and (_availabilityZone is None):
        #         resSubnet = self.EC2Client.create_subnet(DryRun = _dryRun,
        #                                              VpcId = _vpcId,
        #                                              CidrBlock = _cidrBlock,
        #                                                  Ipv6CidrBlock = _ipv6CidrBlock)
        #         return resSubnet

        except Exception:
            raise