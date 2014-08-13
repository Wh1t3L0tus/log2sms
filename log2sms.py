#!/usr/bin/python
# -*- coding: utf-8 -*-

import httplib, urllib, sys


# Reading command-line arguments
if len(sys.argv) != 4:
    print "Usage : log2sms FreeMobile_ID FreeMobile_password message"
    exit(1)


# USER RELATED CONSTANTS
USER_ID = sys.argv[1]
USER_PASSWD = sys.argv[2]

# USER MESSAGE
MSG = sys.argv[3]

getRequest = "/sendmsg?user=" + USER_ID + "&pass=" + USER_PASSWD + "&msg=" + MSG

conn = httplib.HTTPSConnection("smsapi.free-mobile.fr")
conn.request("GET", getRequest)


response = conn.getresponse()

if response.status == 
print response.status, response.reason

conn.close()
