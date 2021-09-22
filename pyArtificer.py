import csv

from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class ScrnMgr(ScreenManager):
    pass


class MenuBarButton(Button):
    pass


class MenuBar(BoxLayout):
    pass


class MainMenu(Screen):
    pass


class CreateMagicItemScreen(Screen):
    pass


class LoadMagicItemScreen(Screen):
    pass


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
    BoxLayout:
        orientation: 'vertical'
        MenuBar:
        Label:
            text: 'Load magic item'
            
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
        return root_widget


ArtificerApp().run()
