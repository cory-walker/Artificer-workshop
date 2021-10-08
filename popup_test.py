from kivy.app import App

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty


class craftingScreen(Screen):

    def __init__(self, **kwargs):
        super(craftingScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.name = "craftng screen"

        self.bl = BoxLayout()
        self.bl.orientation = "vertical"
        self.btn = Button()
        self.btn.text = "rarity: ?"
        self.btn.bind(on_release=self.app.gen_rarpop)
        self.bl.add_widget(self.btn)
        self.add_widget(self.bl)

    def gen_rarpop(self, *args):
        self.rarpop.open()


class ScrnMgr(ScreenManager):
    def __init__(self, **kwargs):
        super(ScrnMgr, self).__init__(**kwargs)
        self.craftingScreen = craftingScreen()
        self.add_widget(self.craftingScreen)
        self.current = self.craftingScreen.name


class rarityPopup(Popup):
    def __init__(self, **kwargs):
        super(rarityPopup, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.rbl = BoxLayout()
        self.rbl.orientation = "vertical"
        self.btnCommon = Button()
        self.btnCommon.text = "common"
        self.btnUnCommon = Button()
        self.btnUnCommon.text = "uncommon"
        self.btnCommon.bind(on_release=self.app.set_rarbtn)
        self.btnUnCommon.bind(on_release=self.app.set_rarbtn)
        self.rbl.add_widget(self.btnCommon)
        self.rbl.add_widget(self.btnUnCommon)
        self.add_widget(self.rbl)


class testApp(App):

    def __init__(self, **kwargs):
        super(testApp, self).__init__(**kwargs)
        self.rarpop = rarityPopup()
        self.scrnmgr = ScrnMgr()

    def gen_rarpop(self, *args):
        self.rarpop.open()

    def set_rarbtn(self, *args):
        self.rarpop.dismiss()
        self.scrnmgr.screens[0].btn.text = args[0].text

    def build(self):
        return self.scrnmgr


if __name__ == "__main__":
    ta = testApp()
    ta.run()
