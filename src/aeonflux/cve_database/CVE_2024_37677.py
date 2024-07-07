import datetime
import requests

class cve_2024_37677():
    def endpoint_xss(self, domain):
        payload = '/ACT_ID_355'
        url = 'https://'+domain+payload
        xss_endpoint = requests.get(url, allow_redirects=True)
        time = datetime.datetime.now()
        time_str = time.strftime('%H:%M:%S')
        time_str_fixed = f'{time_str:>8}'
        if xss_endpoint.status_code == 200 : return f'[{time_str_fixed}] CVE-2024-37677 : vulnerable'
        else : return f'[{time_str_fixed}] CVE-2024-37677 : not vulnerable'
