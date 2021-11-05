import arcana as arc

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, ObjectProperty

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton


class Maker():
    def __init__(self):
        self.app = App.get_running_app

    def make_button(self, text=""):
        b = Button()
        b.text = text
        #b.size_hint_y = None
        return b

    def make_label(self, text=""):
        l = Label()
        l.text = text
        #l.size_hint_y = None
        return l

    def make_h_box(self, widgets=[]):
        bx = BoxLayout()
        bx.orientation = "horizontal"
        for w in widgets:
            bx.add_widget(w)
        return bx

    def make_v_box(self, widgets=[]):
        bx = BoxLayout()
        bx.orientation = "vertical"
        for w in widgets:
            bx.add_widget(w)
        return bx


maker = Maker()


class ScrnCrafting(Screen):

    name = StringProperty("crafting")

    def __init__(self, **kwargs):
        super(ScrnCrafting, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.scrl = ScrollView()
        self.bx_main = BoxLayout()
        self.bx_main.orientation = "vertical"
        self.scrl.add_widget(self.bx_main)
        self.add_widget(self.scrl)

        # Name
        self.l_name = maker.make_label("Item name")
        self.ti_name = TextInput()
        self.ti_name.bind(on_text=self.app.set_name)
        self.bx_name = maker.make_h_box([self.l_name, self.ti_name])

        # Description
        self.l_description = maker.make_label("Item description")
        self.ti_description = TextInput()
        self.ti_description.bind(on_text=self.app.set_description)
        self.bx_description = maker.make_h_box(
            [self.l_description, self.ti_description])

        # Is Consumable
        self.l_isConsumable = maker.make_label("Consumable")
        self.cb_isConsumable = CheckBox()
        self.cb_isConsumable.bind(active=self.app.set_is_consumable)
        self.bx_isConsumable = maker.make_h_box(
            [self.l_isConsumable, self.cb_isConsumable])

        # Is Artifact
        self.l_isArtifact = maker.make_label("Artifact")
        self.cb_isArtifact = CheckBox()
        self.cb_isArtifact.bind(active=self.app.set_is_artifact)
        self.bx_isArtifact = maker.make_h_box(
            [self.l_isArtifact, self.cb_isArtifact])

        # Rarity
        self.l_rarity = maker.make_label("Rarity")
        self.tb_common = ToggleButton(text="Common", group="rarity")
        self.tb_uncommon = ToggleButton(text="Uncommon", group="rarity")
        self.tb_rare = ToggleButton(text="Rare", group="rarity")
        self.tb_very_rare = ToggleButton(text="Very Rare", group="rarity")
        self.tb_legendary = ToggleButton(text="Legendary", group="rarity")

        self.tb_common.bind(on_release=self.app.set_rarity)
        self.tb_uncommon.bind(on_release=self.app.set_rarity)
        self.tb_rare.bind(on_release=self.app.set_rarity)
        self.tb_very_rare.bind(on_release=self.app.set_rarity)
        self.tb_legendary.bind(on_release=self.app.set_rarity)

        self.bx_rarity_toggles = maker.make_h_box(
            [self.tb_common, self.tb_uncommon, self.tb_rare, self.tb_very_rare, self.tb_legendary])
        self.bx_rarity = maker.make_v_box(
            [self.l_rarity, self.bx_rarity_toggles])

        # Add Widgets
        self.bx_main.add_widget(self.bx_name)
        self.bx_main.add_widget(self.bx_description)
        self.bx_main.add_widget(self.bx_isConsumable)
        self.bx_main.add_widget(self.bx_isArtifact)
        self.bx_main.add_widget(self.bx_rarity)


class ScrnMgr(ScreenManager):
    def __init__(self, **kwargs):
        super(ScrnMgr, self).__init__(**kwargs)
        self.app = App.get_running_app()


class WorkbenchApp(App):

    def __init__(self, **kwargs):
        super(WorkbenchApp, self).__init__(**kwargs)

        self.lab = arc.ArcaneLab()

        # Screen management
        self.ScrnMgr = ScrnMgr()
        self.ScrnCrafting = ScrnCrafting()

        self.Screens = [self.ScrnCrafting]
        self.addScreensToManager()
        self.ScrnMgr.current = "crafting"

        # Popups

    def build(self):
        return self.ScrnMgr

    def addScreensToManager(self):
        for s in self.Screens:
            self.ScrnMgr.add_widget(s)

    def set_name(self, *args):
        self.lab.current_item.name = args[1]

    def set_description(self, *args):
        self.lab.current_item.description = args[1]

    def set_rarity(self, *args):
        self.lab.current_item.rarity = arc.rarity_numbers[args[0].text.lower()]

    def set_is_consumable(self, *args):
        self.lab.current_item.is_consumable = args[1]

    def set_is_artifact(self, *args):
        self.lab.current_item.is_artifact = args[1]


if __name__ == "__main__":
    wa = WorkbenchApp()
    wa.run()
