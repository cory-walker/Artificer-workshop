from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup

from arcaneWorkshop import RarityPopup


class RarityPop(Popup):
    def __init__(self, **kwargs):
        super(RarityPop, self).__init__(**kwargs)
        self.app = App.get_running_app()

    def change_rarity(self, text, *args):
        self.app.bText = str(text)


class ScrnMgr(ScreenManager):
    pass


class ScrnMain(Screen):
    def __init__(self, **kwargs):
        super(ScrnMain, self).__init__(**kwargs)
        self.app = App.get_running_app()


class rarityButton(Button):

    def __init__(self, **kwargs):
        super(rarityButton, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.bind(bText=self.changed_value)

    def change_value(self):
        i = int(self.app.bText)
        i += 1
        self.app.bText = str(i)
        rp = RarityPopup()
        rp.open()

    def changed_value(self, _instance, newvalue):
        self.text = str(newvalue)

# https://stackoverflow.com/questions/49587156/how-to-bind-a-widget-to-a-value-from-kivy-app


Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
<ScrnMgr>:
    transition: FadeTransition()
    ScrnMain:
<rarityButton>:
<ScrnMain>:
    name: "main"
    BoxLayout:
        Label:
            text: "label"
        rarityButton:
            on_release: self.change_value()
<RarityPop>:
    name: "rarpop"
    BoxLayout:
        orientation: "vertical"
    Button:
        text: "common"
        on_release: self.change_rarity("common"); self.dismiss()
    Button:
        text: "uncommon"
        on_release: self.change_rarity("uncommon"); self.dismiss()
''')


class testApp(App):

    bText = StringProperty("0")

    def build(self):
        return ScrnMgr()


if __name__ == "__main__":
    testApp().run()
