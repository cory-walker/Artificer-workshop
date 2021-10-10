#import kivy
import arcana

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


class kivyFactory():

    def __init__(self, **kwargs):
        super(kivyFactory, self).__init__(**kwargs)
        self.app = App.get_running_app()

    def gen_BoxLayout(self, orientation="vertical"):
        b = BoxLayout()
        b.orientation = orientation
        return b

    def pack_h_box(self, widgets=[]):
        bl = BoxLayout()
        bl.orientation = "horizontal"
        for w in widgets:
            bl.add_widget(w)
        return bl

    def pack_v_box(self, widgets=[]):
        bl = BoxLayout()
        bl.orientation = "vertical"
        for w in widgets:
            bl.add_widget(w)
        return bl

    def gen_label(self, text=""):
        l = Label()
        l.text = text
        return l

    def gen_button(self, text="", button_type=""):
        b = Button()
        b.text = text

        if button_type == "rarity":
            b.bind(on_release=self.app.set_rarity)

        return b


class rarityPopup(Popup):
    def __init__(self, **kwargs):
        super(rarityPopup, self).__init__(**kwargs)
        self.app = App.get_running_app()

        self.bCommon = self.app.kivyFactory.gen_button(
            text="common", button_type="rarity")
        self.bUncommon = self.app.kivyFactory.gen_button(
            text="uncommon", button_type="rarity")
        self.bRare = self.app.kivyFactory.gen_button(
            text="rare", button_type="rarity")
        self.bVeryRare = self.app.kivyFactory.gen_button(
            text="very rare", button_type="rarity")
        self.bLegendary = self.app.kivyFactory.gen_button(
            text="legendary", button_type="rarity")
        self.buttons = [self.bCommon, self.bUncommon,
                        self.bRare, self.bVeryRare, self.bLegendary]
        self.bl = self.app.kivyFactory.pack_v_box(self.buttons)
        self.add_widget(self.bl)


class attributePickerPopup(Popup):
    def __init__(self, **kwargs):
        super(attributePickerPopup, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.bl = BoxLayout()
        self.bl.orientation = "vertical"
        self.add_widget(self.bl)
        self.gen_buttons()
        self.title = "Attributes"

    def gen_buttons(self):
        self.bl.clear_widgets()
        dct = self.app.attribute_dct()
        lst = list(dct.keys())
        lst.sort()
        if lst is None:
            lst = []
        for k in lst:
            s = k + ": " + dct[k]
            b = Button()
            b.text = s
            b.bind(width=lambda s, w: s.setter("text_size")(s, (w*0.98, None)))
            b.bind(on_release=self.app.choose_attribute)
            self.bl.add_widget(b)

        b = Button()
        b.text = "Cancel"
        b.bind(on_release=self.dismiss)
        self.bl.add_widget(b)


class attributesPopup(Popup):
    def __init__(self, **kwargs):
        super(attributesPopup, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.bl = BoxLayout()
        self.bl.orientation = "vertical"
        self.add_widget(self.bl)
        self.gen_buttons()
        self.title = "Attributes"

    def gen_buttons(self):
        self.app = App.get_running_app()
        kf = self.app.kivyFactory
        self.buttons = []
        max_attributes = arcana.attributes_by_rarity[self.app.lab.current_item.rarity]
        i = 1
        for attr in self.app.lab.magic_properties:
            b = Button()
            b.text = "attribute: " + str(i)
            b.id = "attribute_" + str(i)
            b.bind(on_release=self.app.gen_attribute_picker_popup)
            self.buttons.append(b)

            i += 1
            if i > max_attributes:
                break

        bDismiss = Button()
        bDismiss.text = "Cancel"
        bDismiss.on_release = self.dismiss
        self.buttons.append(bDismiss)

        self.bl.clear_widgets()
        for b in self.buttons:
            self.bl.add_widget(b)


class ScrnCrafting(Screen):

    name = StringProperty("crafting")
    id = StringProperty("crafting")

    def __init__(self, **kwargs):
        super(ScrnCrafting, self).__init__(**kwargs)
        self.app = App.get_running_app()

        kf = self.app.kivyFactory

        # Item name
        self.lName = kf.gen_label(text="Item name")
        self.tiName = TextInput()
        self.tiName.bind(text=self.app.set_item_name)
        self.blName = kf.pack_h_box(
            [self.lName, self.tiName])

        # Item Description
        self.lDescription = kf.gen_label(text="Item name")
        self.tiDescription = TextInput()
        self.tiDescription.bind(text=self.app.set_item_description)
        self.blDescription = kf.pack_h_box(
            [self.lDescription, self.tiDescription])

        # Consumable
        self.lConsumable = kf.gen_label(text="Consumable")
        self.cbConsumable = CheckBox()
        self.cbConsumable.bind(active=self.app.set_consumable)
        self.blConsumable = kf.pack_h_box(
            [self.lConsumable, self.cbConsumable])

        # Artifact
        self.lArtifact = kf.gen_label(text="Consumable")
        self.cbArtifact = CheckBox()
        self.cbArtifact.bind(active=self.app.set_artifact)
        self.blArtifact = kf.pack_h_box(
            [self.lArtifact, self.cbArtifact])

        # Rarity button
        self.bRarity = kf.gen_button(text="rarity")
        self.bRarity.bind(on_release=self.app.gen_rarity_popup)

        # Attributes
        self.bAttributes = kf.gen_button(text="attributes")
        self.bAttributes.bind(on_release=self.app.gen_attributes_popup)

        self.bl = kf.pack_v_box(
            [self.blName, self.blDescription, self.blConsumable, self.blArtifact, self.bRarity, self.bAttributes])
        self.add_widget(self.bl)


class ScrnMgr(ScreenManager):
    def __init__(self, **kwargs):
        super(ScrnMgr, self).__init__(**kwargs)
        self.app = App.get_running_app()


class ArcaneWorkshopApp(App):

    def __init__(self, **kwargs):
        super(ArcaneWorkshopApp, self).__init__(**kwargs)
        self.lab = arcana.ArcaneLab()
        self.kivyFactory = kivyFactory()
        self.rarityPopup = rarityPopup()
        self.ScrnMgr = ScrnMgr()
        self.ScrnMgr.add_widget(ScrnCrafting())
        self.ScrnMgr.current = "crafting"
        self.attributesPopup = attributesPopup()
        self.attribute_picker_popup = attributePickerPopup()

        self.attribute_button_clicked = ""

    def build(self):
        return self.ScrnMgr

    def gen_rarity_popup(self, *args):
        self.rarityPopup.open()

    def set_rarity(self, *args):
        self.lab.current_item.rarity = arcana.rarity_numbers[args[0].text]
        self.ScrnMgr.screens[0].bRarity.text = args[0].text
        self.attributesPopup.gen_buttons()
        self.rarityPopup.dismiss()

    def set_item_name(self, *args):
        self.lab.current_item.name = args[1]

    def set_item_description(self, *args):
        self.lab.current_item.description = args[1]

    def set_consumable(self, *args):
        self.lab.current_item.is_consumable = args[1]

    def set_artifact(self, *args):
        self.lab.current_item.is_artifact = args[1]

    def gen_attributes_popup(self, *args):
        self.attributesPopup.open()

    def gen_attribute_picker_popup(self, *args):
        self.attribute_picker_popup.gen_buttons()
        self.attribute_button_clicked = args[0].id
        self.attribute_picker_popup.open()

    def attribute_dct(self):
        return self.lab.fetch_magic_property_descriptions(1)

    def choose_attribute(self, *args):
        pass


if __name__ == "__main__":
    aw = ArcaneWorkshopApp()
    aw.run()
