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
from aeonflux.cve_database.CVE_2024_21515 import cve_2024_21515
from aeonflux.cve_database.CVE_2024_21514 import cve_2024_21514
from aeonflux.cve_database.CVE_2024_6241 import cve_2024_6241
from aeonflux.cve_database.CVE_2024_5447 import cve_2024_5447


class aeonflux(toga.App):
    def startup(self):

        self.main_window = toga.MainWindow(title=self.formal_name,size=(400, 700))        
        self.scroller = toga.ScrollContainer(horizontal=False, vertical=True, style=Pack(flex=1, padding=0))

        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        name_label = toga.Label('Target:', style=Pack(padding=(0,5)))                
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))

        self.name_input = toga.TextInput(style=Pack(flex=1))
        button = toga.Button('Start Vulnerability Scan!', on_press=self.get_data, style=Pack(padding=5),)

        self.main_box.add(name_box)
        self.main_box.add(button)
        name_box.add(name_label)
        name_box.add(self.name_input)

                        
        self.scroller.content = self.main_box
        self.main_window.content = self.scroller
        self.main_window.show()


    def get_data(self, widget):
            target_domain = self.name_input.value
            time = datetime.datetime.now()
            time_str = time.strftime('%H:%M:%S')
            time_str_fixed = f'{time_str:>8}'
            
            if '.' in target_domain:
                url = 'https://'+target_domain
                response = requests.get(url)
                
                if response.status_code == 200:
                    status = f'[{time_str_fixed}] target is alive in the network.'
                    self.main_box.add(toga.Label(status, style=Pack(background_color='#005577', color='black')))
                    
                    vulnerabilities = [
                    
                        cve_2024_4704().redirect_vulnerability(target_domain),
                        cve_2024_4664().endpoint_verify(target_domain),
                        cve_2024_37732().backdoor_upload(target_domain),
                        cve_2024_37680().endpoint_xss(target_domain),
                        cve_2024_37677().endpoint_xss(target_domain),
                        cve_2024_21519().arbitrary_verify(target_domain),
                        cve_2024_21518().request_xss(target_domain),
                        cve_2024_21517().reflected_xss(target_domain),
                        cve_2024_21516().reflected_xss(target_domain),
                        cve_2024_21515().reflected_xss(target_domain),
                        cve_2024_21514().sql_injection(target_domain),
                        cve_2024_6241().sql_injection(target_domain),
                        cve_2024_5447().endpoint_xss(target_domain),
                    ]

                    
                    for cve in vulnerabilities:
                        self.main_box.add(toga.Label(cve, style=Pack(background_color='black', color='#FFFFFF')))
                                                                        
                else:
                    down_message = f'[{time_str_fixed}] target is not alive in the network and can not be tested!'
                    show_values = toga.Label(down_message, style=Pack(background_color='#00FFFF', color='black'))
                    self.main_box.add(show_values)
                
            else:
                text = f'[{time_str_fixed}] no target value found, cant perform the attack'
                self.main_box.add(toga.Label(text, style=Pack(background_color='#00FFFF', color='black')))

def main():
    return aeonflux()
