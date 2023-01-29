"""
This file proposes a simple client to use the class
"""

import argparse
from uri import URI

parser = argparse.ArgumentParser(description='Process uri parsing and validating')
parser.add_argument('-u','--uri', help='The uri containing the full path')
args = parser.parse_args()

if args.uri:
    uri = args.uri
else:
    uri = input("Please enter an uri : ")

myuri = URI(uri)
print("Scheme: ", myuri.scheme)
print("Path: ", myuri.path)
print("Params: ", myuri.params)
print("Is the URI valid: ", myuri.validate())
