#!/bin/python3
import requests
import datetime

class CVE_2024_23421():
    def check_vulnerability(self, target):
        url = 'https://'+target
        response = requests.get(url)
        time = datetime.datetime.now()
        if response.status_code == 200:
            return f'[{time.hour}:{time.minute}:{time.second}]➤ target is alive in the network!'
        else:
            return f'[{time.hour}:{time.minute}:{time.second}]➤ target is not alive in the network!'

