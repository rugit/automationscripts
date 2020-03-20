#!/usr/bin/env python3

from PIL import Image
import os

for files in os.listdir("/home/student-00-8b3ca195f985/supplier-data/images/"):
    im = Image.open("/home/student-00-8b3ca195f985/supplier-data/images/"+files)
    im = im.resize((600,400))
    im = im.convert("RGB")
    im.save("/home/student-00-8b3ca195f985/supplier-data/images/"+files.split(".")[0]+".jpeg")
