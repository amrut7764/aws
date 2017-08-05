__author__ = 'imroot <chougale.amrut@gmail.com>'

import boto3
import json
import pdb

class RDS():

    def __init__(self):

        # create a RDS client object
        self.RDSClient = boto3.client('rds')
        # Create a RDS resource object
        #self.RDSResource = boto3.resource('rds')

    def createRDSSecurityGroup(self, **kwargs):
        _dbSecGroupName = kwargs.get("dbSecGroupName")
        _dbSecGroupDescription = kwargs.get("dbSecGroupDescription")
        _subnetIDs = kwargs.get("subnetIDs")
        _tags = kwargs.get("tags")

        if not (type(_subnetIDs) is list) or not(type(_tags) is list):
            raise Exception ("Please provide subnet IDs and tags as list")
        try:
            resp = self.RDSClient.create_db_subnet_group(DBSubnetGroupName=_dbSecGroupName,
                                                         DBSubnetGroupDescription=_dbSecGroupDescription,
                                                         SubnetIds=_subnetIDs,
                                                         Tags = _tags)
        except Exception:
            raise
        else:
            return resp

    def createDBInstance(self, **kwargs):
        pass
