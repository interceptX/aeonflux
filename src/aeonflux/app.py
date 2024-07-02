'''
Red Team Security App
'''

import toga
import datetime
import requests
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

#cve,cpe,cwe vulnerability modules
from aeonflux.cve_database.CVE_2024_4704 import cve_2024_4704
from aeonflux.cve_database.CVE_2024_4664 import cve_2024_4664
from aeonflux.cve_database.CVE_2024_37732 import cve_2024_37732
from aeonflux.cve_database.CVE_2024_37680 import cve_2024_37680
from aeonflux.cve_database.CVE_2024_37677 import cve_2024_37677
from aeonflux.cve_database.CVE_2024_21519 import cve_2024_21519
from aeonflux.cve_database.CVE_2024_21518 import cve_2024_21518
from aeonflux.cve_database.CVE_2024_21517 import cve_2024_21517
from aeonflux.cve_database.CVE_2024_21516 import cve_2024_21516

class aeonflux(toga.App):
    def startup(self):
        
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        name_label = toga.Label('Target:', style=Pack(padding=(0,5)),)
        self.name_input = toga.TextInput(style=Pack(flex=1))
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)
        button = toga.Button('Start Attack!', on_press=self.get_data, style=Pack(padding=5),)
        self.main_box.add(name_box)
        self.main_box.add(button)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()


    def get_data(self, widget):
            time = datetime.datetime.now()
            target_domain = self.name_input.value
            
            if '.' in target_domain:
                url = 'https://'+target_domain
                response = requests.get(url)
                time = datetime.datetime.now()
                
                if response.status_code == 200:
                    alive_message = f'[{time.hour}:{time.minute}:{time.microsecond}] target is alive in the network and can be tested.'
                    CVE_2024_4704 = cve_2024_4704()
                    CVE_2024_4664 = cve_2024_4664()
                    CVE_2024_37732 = cve_2024_37732()
                    CVE_2024_37680 = cve_2024_37680()
                    CVE_2024_37677 = cve_2024_37677()
                    CVE_2024_21519 = cve_2024_21519()
                    CVE_2024_21518 = cve_2024_21518()
                    CVE_2024_21517 = cve_2024_21517()
                    CVE_2024_21516 = cve_2024_21516()

                    alive_message = toga.Label(alive_message, style=Pack(background_color='yellow', color='black'))
                    
                    CVE_2024_4704 = toga.Label(CVE_2024_4704.redirect_vulnerability(target_domain))
                    CVE_2024_4664 = toga.Label(CVE_2024_4664.endpoint_verify(target_domain))
                    CVE_2024_37732 = toga.Label(CVE_2024_37732.backdoor_upload(target_domain))
                    CVE_2024_37680 = toga.Label(CVE_2024_37680.endpoint_xss(target_domain))
                    CVE_2024_37677 = toga.Label(CVE_2024_37677.endpoint_xss(target_domain))
                    CVE_2024_21519 = toga.Label(CVE_2024_21519.arbitrary_verify(target_domain))
					CVE_2024_21518 = toga.Label(CVE_2024_21518.request_xss(target_domain))
					CVE_2024_21517 = toga.Label(CVE_2024_21517.reflected_xss(target_domain))
					CVE_2024_21516 = toga.Label(CVE_2024_21516.reflected_xss(target_domain))
                                        
                    self.main_box.add(alive_message)
                    self.main_box.add(CVE_2024_4704)
                    self.main_box.add(CVE_2024_4664)
                    self.main_box.add(CVE_2024_37732)
                    self.main_box.add(CVE_2024_37680)
                    self.main_box.add(CVE_2024_37677)
                    self.main_box.add(CVE_2024_21519)
                    self.main_box.add(CVE_2024_21518)
                    self.main_box.add(CVE_2024_21517)
                    self.main_box.add(CVE_2024_21516)
                    
                else:
                    down_message = f'[{time.hour}:{time.minute}:{time.microsecond}] target is not alive in the network and can not be tested!'
                    show_values = toga.Label(down_message, style=Pack(background_color='red', color='black'))
                    self.main_box.add(show_values)
                
            else:
                text = f'[{time.hour}:{time.minute}:{time.microsecond}] no target value found, cant perform the attack'
                show_values = toga.Label(text, style=Pack(background_color='yellow', color='black'))
                self.main_box.add(show_values)

def main():
    return aeonflux()

