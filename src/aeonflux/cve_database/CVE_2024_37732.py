import requests
import datetime

class cve_2024_37732():
	def backdoor_upload(self, domain):
		payload = '/index.php/admin/upload'
		url = 'https://'+domain+payload
		access_endpoint = requests.post(url, allow_redirects=True)
		time = datetime.datetime.now()
		if access_endpoint.status_code == 200 : return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-37732 : vulnerable'
		else : return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-37732 : not vulnerable'
