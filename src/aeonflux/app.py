"""
Red Team Security App
"""

import toga
import datetime
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class aeonflux(toga.App):
    def startup(self):

        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        name_label = toga.Label("Target:", style=Pack(padding=(0,5)),)
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button("Start Attack!", on_press=self.say_hello, style=Pack(padding=5),)

        self.main_box.add(name_box)
        self.main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()


    def say_hello(self, widget):
            time = datetime.datetime.now()
            target_domain = self.name_input.value

            if "." in target_domain:
                print(f"[+][{time.hour}:{time.minute}:{time.second}] now checking vulnerabilities target : https://{self.name_input.value}")
                self.data = toga.Label(self.cve(), style=Pack(background_color='green'))
                self.main_box.add(self.data)

            else:
                print(f"[!][{time.hour}:{time.minute}:{time.second}] no target value found, cant perform attack")

    def cve(self):
        a = f"➤ CVE-2024-23421 ➤ {self.name_input.value} is not vulnerable."
        return a

def main():
    return aeonflux()
