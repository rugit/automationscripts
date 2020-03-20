#!/usr/bin/env python3

import emails
import os
from datetime import datetime
import reports

hd = "/home/student-00-832fa9b08727/supplier-data/descriptions/"
data = []
now = datetime.now()
title = "Processed Update on {}".format(now.strftime("%B %d, %y"))
for files in os.listdir(hd):
    f = open(hd+files, 'r')
    data.append(["name:", f.readline()])
    data.append(["weight:", f.readline()])
    data.append(["",""])
    f.close()

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."


if __name__ == "__main__":
    reports.generate("/tmp/processed.pdf",title, data)
    message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send(message)

