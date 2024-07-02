'''
Red Team Security App
'''

import toga
import datetime
import requests
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

#cve,cpe,cwe vulnerability modules
from aeonflux.cve_database.CVE_2024_4704 import cve_confirmation

class aeonflux(toga.App):
    def startup(self):
        
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        name_label = toga.Label('Target:', style=Pack(padding=(0,5)),)
        self.name_input = toga.TextInput(style=Pack(flex=1))
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)
        button = toga.Button('Start Attack!', on_press=self.say_hello, style=Pack(padding=5),)
        self.main_box.add(name_box)
        self.main_box.add(button)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()


    def say_hello(self, widget):
            time = datetime.datetime.now()
            target_domain = self.name_input.value
            if '.' in target_domain:
                self.alive_network_test(target_domain)
            else:
                text = f'[{time.hour}:{time.minute}:{time.second}] no target value found, cant perform the attack'
                show_values = toga.Label(text, style=Pack(background_color='yellow', color='black'))
                self.main_box.add(show_values)

    def alive_network_test(self, domain):
        url = 'https://'+domain
        response = requests.get(url)
        time = datetime.datetime.now()
        if response.status_code == 200:
            alive_message = f'[{time.hour}:{time.minute}:{time.second}] target is alive in the network and can be tested.'
            CVE_2024_4704 = cve_confirmation()

            alive_message = toga.Label(alive_message)
            CVE_2024_4704 = toga.Label(CVE_2024_4704.redirect_vulnerability(domain))

            self.main_box.add(alive_message)
            self.main_box.add(CVE_2024_4704)
            
        else:
            down_message = f'[{time.hour}:{time.minute}:{time.second}] target is not alive in the network and can not be tested!'
            show_values = toga.Label(down_message, style=Pack(background_color='red', color='black'))
            self.main_box.add(show_values)


def main():
    return aeonflux()

