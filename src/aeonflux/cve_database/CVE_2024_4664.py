import requests
import datetime

class cve_2024_4664():
    def endpoint_verify(self, domain):
        payload = '/wp-admin/admin.php?page=nta_whatsapp_floating_widget'
        url = 'https://'+domain+payload
        access_url = requests.get(url, allow_redirects=True)
        time = datetime.datetime.now()
        time_str = time.strftime('%H:%M:%S')
        time_str_fixed = f'{time_str:>8}'
        if access_url.status_code == 200: return f'[{time_str_fixed}] CVE-2024-4664 : vulnerable'
        else: return f'[{time_str_fixed}] CVE-2024-4664 : not vulnerable'
            

