import requests
import datetime

class cve_2024_21519():
    def arbitrary_verify(self, domain):
        payload = '/opencart/admin/index.php?route=tool/'
        url = 'https://'+domain+payload
        access_url = requests.get(url)    
        time = datetime.datetime.now()
        if access_url.status_code == 200: return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-21519 : vulnerable'
        else: return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-21519 : not vulnerable'
