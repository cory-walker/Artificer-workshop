import csv
from os import path

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox

cur_item = None


class magicItem:
    def __init__(self, name="new item", description="", eldrict_properties=[], rarity="common", is_artifact=False, is_consumable=False, eldrict_materials=[]):
        self.name = name
        self.description = description
        self.eldrict_properties = eldrict_properties
        self.rarity = rarity
        self.is_artifact = is_artifact
        self.is_consumable = is_consumable

        self.eldrict_materials = eldrict_materials

    def get_properties(self):
        l = self.eldrict_properties
        for material in self.eldrict_materials():
            if material.eldrict_property is not None:
                l.append(material.eldrict_property)
        return l


class Display(BoxLayout):
    cur_item_name = StringProperty("none")

    def __init__(self, **kwargs):
        super(Display, self).__init__(**kwargs)


class RarityDropDown(BoxLayout):
    state = BooleanProperty(False)


class EldrictPropertyDropDown(BoxLayout):
    state = BooleanProperty(False)


class LoadItemScreen(Screen):

    name = StringProperty("load_item")

    def __init__(self, **kwargs):
        super(LoadItemScreen, self).__init__(**kwargs)
        self.load_item_list = self.build_load_items_list()

        dd = DropDown(size_hint_y=1, size_hint_x=None, width=200)
        self.add_widget(dd)
        for il in self.load_item_list:
            btn = Button(text=il, size_hint_y=None,
                         size_hint_x=None, height=30)
            btn.bind(on_release=self.print_something)
            dd.add_widget(btn)

    def print_something(self, *args):
        print(args[0].text)
        self.load_item(args[0].text)
        self.parent.current = "crafting"

    def build_load_items_list(self):
        lst = []
        scrpt_dir = path.dirname(__file__)
        filepath = path.join(scrpt_dir, ".\\data\\magic_items.csv")
        f = open(filepath, "r")
        reader = csv.reader(f, delimiter=',', quotechar='"',
                            skipinitialspace=True)
        next(reader, None)  # skip headers
        for l in reader:
            lst.append(l[0])
        f.close()
        return lst

    def load_item(self, item_name):
        scrpt_dir = path.dirname(__file__)
        filepath = path.join(scrpt_dir, ".\\data\\magic_items.csv")
        f = open(filepath, "r")
        reader = csv.reader(f, delimiter=',', quotechar='"',
                            skipinitialspace=True)
        next(reader, None)  # skip headers
        for l in reader:
            if l[0] == item_name:
                break

        cur_item = magicItem(name=l[0], description=l[1], rarity=l[2],
                             is_artifact=l[3], is_consumable=l[4])
        spl = l[5].split(",")
        for s in spl:
            cur_item.eldrict_properties.append(
                s.replace("[", "").replace("]", ""))

        spl = l[6].split(",")
        for s in spl:
            cur_item.eldrict_materials.append(
                s.replace("[", "").replace("]", ""))

        f.close()
        return


class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)


class CraftingScreen(Screen):
    def __init__(self, **kwargs):
        super(CraftingScreen, self).__init__(**kwargs)
        eld = EldrictPropertyDropDown()
        for c in self.children:
            print(c.name)
        print("i")


class EldrictWorkshopApp(App):
    def build(self):
        return Display()


if __name__ == '__main__':
    EldrictWorkshopApp().run()
