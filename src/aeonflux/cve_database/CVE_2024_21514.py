import requests
import datetime

class cve_2024_21514():
	def sql_injection(self, domain):
		payload = '/index.php?route=extension/payment/divido/update'
		url = 'https://'+domain+payload
		access_endpoint = requests.post(url, allow_redirects=True)
		time = datetime.datetime.now()
		if access_endpoint.status_code == 200 : return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-21514 : vulnerable'
		else : return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-21514 : not vulnerable'
