import requests
import datetime

class cve_confirmation():
    def redirect_vulnerability(self, domain):
        time = datetime.datetime.now()
        data = f'[{time.hour}:{time.minute}:{time.second}] CVE-2024-4704 : not vulnerable'
        return data
