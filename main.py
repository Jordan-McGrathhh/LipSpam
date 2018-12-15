#!/usr/env/python

import requests
import time
import os

def banner():

    print """

  _      _       _____
 | |    (_)     / ____|
 | |     _ _ __| (___  _ __   __ _ _ __ ___
 | |    | | '_  \___ \| '_ \ / _` | '_ ` _  |
 | |____| | |_) |___) | |_) | (_| | | | | | |
 |______|_| .__/_____/| .__/ \__,_|_| |_| |_|
          | |         | |
          |_|         |_|

    """









banner()
userPath = raw_input("UserPath: ")
message = raw_input("Message: ")
numOfMessages = int(raw_input("# of Messages: ")) 

#POST URL
url = "https://web.lipsiapp.com/conversation/web"

#Headers
headers = {
        "Accept": '*/*',
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "text/plain;charset=UTF-8",
        "DNT": "1",
        "Host": "web.lipsiapp.com",
        "Origin": "https://lipsiapp.com",
        "Referer": "https://lipsiapp.com/",
        "TE": "Trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"


        }

#JSON
data = {
        "fingerprint": "11111111111111111111111111111111",
        "message": message,
        "userPath": userPath
        }

proxies = {
        
        #"https": "76.76.76.74:53281"
        
        }

requestAttempts = 0

while(requestAttempts < numOfMessages):

    lipsiRequest = requests.post(url, headers=headers, json=data, proxies=proxies)
    print "[*] REQUEST " + str(requestAttempts + 1) + " SUCCESSFUL [*]"

    requestAttempts = requestAttempts + 1
