import csv
from os import path

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button


class Display(BoxLayout):
    cur_item_name = StringProperty("none")

    def __init__(self, **kwargs):
        super(Display, self).__init__(**kwargs)


class LoadItemScreen(Screen):

    name = StringProperty("load_item")

    def __init__(self, **kwargs):
        super(LoadItemScreen, self).__init__(**kwargs)
        self.load_item_list = self.build_load_items_list()

        dd = DropDown(size_hint_y=None, size_hint_x=None)
        self.add_widget(dd)
        for il in self.load_item_list:
            btn = Button(text=il, size_hint=(None, None))
            btn.bind(on_release=self.print_something)
            dd.add_widget(btn)

    def print_something(self, *args):
        print(args[0].text)
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


class CraftingScreen(Screen):
    def __init__(self, **kwargs):
        super(CraftingScreen, self).__init__(**kwargs)


class EldrictWorkshopApp(App):
    def build(self):
        return Display()


if __name__ == '__main__':
    EldrictWorkshopApp().run()
