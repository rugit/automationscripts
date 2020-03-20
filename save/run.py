#! /usr/bin/env python3

import os
import requests


hd = "/home/student-00-8b3ca195f985/"

for files in os.listdir(hd+"supplier-data/descriptions/"):
    datas = {}
    f = open(hd+"supplier-data/descriptions/"+files, 'r')
    datas["name"] = f.readline()
    datas["weight"] = int(f.readline().split(" ")[0])
    datas["description"] = f.readline()
    datas["image_name"] = files.split(".")[0]+".jpeg"

    requests.post(url="http://34.68.245.56/fruits/", data=datas)

    f.close()
