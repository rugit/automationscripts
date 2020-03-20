#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
for files in os.listdir("/home/student-00-8b3ca195f985/supplier-data/images/"):
    if(files.split(".")[1] == "jpeg"):
        with open("/home/student-00-8b3ca195f985/supplier-data/images/"+files, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
