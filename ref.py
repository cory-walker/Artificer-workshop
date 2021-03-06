import csv
from os import path
import ArcaneLab

from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty


class ScrnMgr(ScreenManager):
    def __init__(self, **kwargs):
        super(ScrnMgr, self).__init__(**kwargs)


class MenuBarButton(Button):
    pass


class MenuBar(BoxLayout):
    pass


class MainMenu(Screen):
    pass


class CreateMagicItemScreen(Screen):
    pass


class loadItemDropDown(DropDown):
    def __init__(self, **kwargs):
        super(loadItemDropDown, self).__init__(**kwargs)


class LoadMagicItemScreen(Screen):

    #addButton = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(LoadMagicItemScreen, self).__init__(**kwargs)

        self.height = Window.height
        self.width = Window.width

        self.saved_items = self.load_saved_items_names()

        bl = BoxLayout(orientation="vertical")
        self.add_widget(bl)
        bl.add_widget(MenuBar())

        dd = DropDown(size_hint_y=None, height=500)
        bl.add_widget(dd)
        for item_name in self.saved_items:
            btn = Button(text=item_name, size_hint_y=None, height=25)
            btn.bind(on_release=lambda btn: dd.select(self.loadItem(btn.text)))
            dd.add_widget(btn)

    def loadItem(self, item_name):
        print(item_name)
        ScreenManager.current = 'create magic item'

    def load_saved_items_names(self):
        scrpt_dir = path.dirname(__file__)
        filepath = path.join(scrpt_dir, ".\\data\\magic_items.csv")
        lst = []
        f = open(filepath, "r")
        reader = csv.reader(f, delimiter=',', quotechar='"',
                            skipinitialspace=True)
        next(reader, None)  # skip headers
        for l in reader:
            lst.append(l[0])
        f.close()
        return lst


class CreateEldrictPropertyScreen(Screen):
    pass


class CreateSpecialMaterialScreen(Screen):
    pass


root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
ScrnMgr:
    transition: FadeTransition()
    MainMenu:
    CreateMagicItemScreen:
    CreateEldrictPropertyScreen:
    CreateSpecialMaterialScreen:
    LoadMagicItemScreen:

<MenuBarButton>:
    text_size: self.width, None
    halign: 'center'
    valign: 'center'

<MenuBar>:
    orientation: 'horizontal'
    size_hint_y: None
    size_y: 5
    MenuBarButton:
        text: 'Main'
        on_release: app.root.current = 'main menu'
    MenuBarButton:
        text: 'Craft Item'
        on_release: app.root.current = 'create magic item'
    MenuBarButton:
        name: 'load_item'
        text: 'Load Item'
        on_release: app.root.current = 'load magic item'
    MenuBarButton:
        text: 'Craft Property'
        on_release: app.root.current = 'create eldrict property'
    MenuBarButton:
        text: 'Craft Material'
        on_release: app.root.current = 'create special material'

<MainMenu>:
    name: 'main menu'
    BoxLayout:
        orientation: 'vertical'
        MenuBar:
        Label:
            text: 'Main Menu'

<CreateMagicItemScreen>:
    name: 'create magic item'
    BoxLayout:
        orientation: 'vertical'
        MenuBar:
        Label:
            text: 'Craft magic Item'

<LoadMagicItemScreen>:
    name: 'load magic item'

<CreateEldrictPropertyScreen>:
    name: 'create eldrict property'
    BoxLayout:
        orientation: 'vertical'
        MenuBar:
        Label:
            text: 'Craft Eldrict property'

<CreateSpecialMaterialScreen>:
    name: 'create special material'
    BoxLayout:
        orientation: 'vertical'
        MenuBar:
        Label:
            text: 'Craft special material'



''')


class ArtificerApp(App):

    def build(self):

        self.cur_item = None  # ArcaneLab.magicItem
        self.cur_property = None  # ArcaneLab.eldrictProperty
        self.cur_material = None  # ArcaneLab.specialMaterial
        self.rarities = self.load_rarities()

        return root_widget

    def load_rarities(self):
        scrpt_dir = path.dirname(__file__)
        filepath = path.join(scrpt_dir, ".\\data\\rarities.csv")
        dct = {}
        f = open(filepath, "r")
        reader = csv.reader(f, delimiter=',', quotechar='"',
                            skipinitialspace=True)
        next(reader, None)  # skip headers
        for l in reader:
            r = ArcaneLab.rarity(l[0], l[1], l[2], l[3],
                                 l[4], l[5], l[6], l[7])
            dct[r.name] = r

        f.close()
        return dct


ArtificerApp().run()
