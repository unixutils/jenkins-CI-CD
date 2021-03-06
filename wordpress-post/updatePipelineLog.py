#!/usr/bin/python3
from datetime import datetime
import base64
import json
import os
import requests
import sys
import re

# WP Post configuration
consoleurl = os.environ['buildurl'] + 'consoleText'
url = os.environ['wpurl']
log_postID = os.environ['log_wppostid']
user = os.environ['wpuser']
password = os.environ['wppw']
credentials = user + ':' + password
token = base64.b64encode(credentials.encode())
header = {'Authorization': 'Basic ' + token.decode('utf-8')}
jenkinsuser = os.environ['jenkinsuser']
jenkinstoken = os.environ['jenkinstoken']
jenkinsauth    = (jenkinsuser, jenkinstoken)

# Content for WP Post
now = datetime.now()
current_time = now.strftime("%d/%m/%Y %H:%M:%S")
log = requests.get(consoleurl, auth=jenkinsauth).text
log = re.sub('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', '*********', log)
log = re.sub('.*export.*\n?', '', log)

content = """This post was updated using a CI/CD pipeline job run by jenkins on AWS @{0}.

Output:
{1}""".format(current_time, log)

post = {
 'title'    : 'CI/CD Live pipeline log',
 'content'  : content
}

response = requests.post(url + log_postID , headers=header, json=post)
print(response)
