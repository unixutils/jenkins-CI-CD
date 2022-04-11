#!/usr/bin/python3
from datetime import datetime
import base64
import json
import os
import requests
import sys

# WP Post configuration
jobname = os.environ['jobname']
buildnumber = os.environ['buildnumber']
buildtag = os.environ['buildtag']
buildurl = os.environ['buildurl']
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
PIPELINE_LOG_URL : <a href="https://unixutils.com/ci-cd-live-pipeline-log/">https://unixutils.com/ci-cd-live-pipeline-log/</a>""".format(current_time, jobname, buildnumber, buildtag)

post = {
 'title'    : 'CI/CD Live',
 'content'  : content
}

response = requests.post(url + postID , headers=header, json=post)
print(response)

