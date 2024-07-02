import requests
import datetime

class cve_2024_37680():
	def endpoint_xss(self, domain):
		payload = '/yy/login.jsp'
		url = 'https://'+domain+payload
		xss_endpoint = requests.get(url, allow_redirects=True)
		time = datetime.datetime.now()
		if xss_endpoint.status_code == 200 : return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-37680 : vulnerable'
		else : return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-37680 : not vulnerable'
