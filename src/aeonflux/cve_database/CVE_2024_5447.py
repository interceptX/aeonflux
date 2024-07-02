import requests
import datetime

class cve_2024_5447():
	def endpoint_xss(self, domain):
		payload = '/wp-admin/options-general.php?page=wpdev-paypal-button'
		url = 'https://'+domain+payload
		access_endpoint = requests.post(url, allow_redirects=True)
		time = datetime.datetime.now()
		if access_endpoint.status_code == 200 : return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-5447 : vulnerable'
		else : return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-5447 : not vulnerable'
