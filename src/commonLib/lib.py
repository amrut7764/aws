__author__ = 'imroot <chougale.amrut@gmail.com>'

import pdb
import boto3
import json

def validate(defaultArgs, mandatoryArgs, **kwargs):
    for i in defaultArgs.keys():
        if i not in kwargs.keys():
            kwargs[i] = defaultArgs[i]
    pdb.set_trace()
    for j in mandatoryArgs:
        if j not in kwargs.keys():
            raise Exception("%s is a mandatory argument." % j)
    return kwargs
