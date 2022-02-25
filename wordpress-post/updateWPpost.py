#!/usr/bin/python3
import requests
import json
import base64
import sys
import os
from datetime import datetime

# Get inputs from jenkins job
JOB_NAME = sys.argv[1]
BUILD_NUMBER = sys.argv[2]
BUILD_TAG = sys.argv[3]

# WP Post configuration
url = "https://unixutils.com/wp-json/wp/v2/posts/"
postID = "2877"
user = os.environ['wpuser']
password = os.environ['wppw']
credentials = user + ':' + password
token = base64.b64encode(credentials.encode())
header = {'Authorization': 'Basic ' + token.decode('utf-8')}

# Content for WP Post
now = datetime.now()
current_time = now.strftime("%d/%m/%Y %H:%M:%S")

content = """This post was updated using a CI/CD pipeline job run by jenkins on AWS @{0}.
JOB_NAME = {1}
BUILD_NUMBER = {2}
BUILD_TAG = {3}""".format(current_time, JOB_NAME, BUILD_NUMBER, BUILD_TAG)

post = {
 'title'    : 'CI/CD Live',
 'content'  : content
}

response = requests.post(url + postID , headers=header, json=post)
print(response.content)
