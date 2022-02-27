#!/usr/bin/python3
from datetime import datetime
import base64
import json
import os
import requests
import sys

# Get inputs from jenkins job
BUILD_NUMBER = sys.argv[2]
BUILD_TAG = sys.argv[3]
JOB_NAME = sys.argv[1]

# WP Post configuration
url = os.environ['wpurl']
postID = os.environ['wppostid']
user = os.environ['wpuser']
password = os.environ['wppw']
credentials = user + ':' + password
token = base64.b64encode(credentials.encode())
header = {'Authorization': 'Basic ' + token.decode('utf-8')}

# Content for WP Post
now = datetime.now()
current_time = now.strftime("%d/%m/%Y %H:%M:%S")

content = """This post was updated using a CI/CD pipeline job run by jenkins on AWS @{0}.
JOB_NAME : {1}
BUILD_NUMBER : {2}
BUILD_TAG : {3}
PIPELINE_LOG_URL : <a href="https://unixutils.com/ci-cd-live-pipeline-log/">https://unixutils.com/ci-cd-live-pipeline-log/</a>""".format(current_time, JOB_NAME, BUILD_NUMBER, BUILD_TAG)

post = {
 'title'    : 'CI/CD Live',
 'content'  : content
}

response = requests.post(url + postID , headers=header, json=post)
print(response)
