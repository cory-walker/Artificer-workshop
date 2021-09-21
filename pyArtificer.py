import csv

from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.anchorlayout import AnchorLayout


class ScrnMgr(ScreenManager):
    pass


class MainMenuScreen(Screen):
    pass


class CreateMagicItemScreen(Screen):
    pass


class CreateMagicPropertyScreen(Screen):
    pass


class LoadMagicItemScreen(Screen):
    pass


class HeaderMenu(Screen):
    pass


root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
ScrnMgr:
    transition: FadeTransition()
    MainMenuScreen:
    CreateMagicItemScreen:
    CreateMagicPropertyScreen:
    LoadMagicItemScreen:
    HeaderMenu:

<Btn@Button>:
    size_hint: [None,None]
    size: [100,100]

<Header@AnchorLayout>:
    anchor_x: 'center'
    anchor_y: 'top'

    canvas:
        Color: 
            rgb: [.5,.9,.5]
        Rectangle:
            pos: self.pos
            size: int(self.size / 10)
    Btn:
        text: 'Main'
        on_release: app.root.current = 'main menu'

<MainMenuScreen>:
    name: 'main menu'
    BoxLayout:
        orientation: 'vertical'
        Header:

        BoxLayout:
            orientation: 'vertical'

            Button:
                text: 'Create magic Item'
                font_size: 30
                on_release: app.root.current = 'create magic item'
            Button:
                text: 'Load magic Item'
                font_size: 30
                on_release: app.root.current = 'load magic item'
            Button:
                text: 'Create magic property'
                font_size: 30
                on_release: app.root.current = 'CreateMagicPropertyScreen'

<CreateMagicItemScreen>:
    name: 'create magic item'
<CreateMagicPropertyScreen>:
    name: 'create magic property'
<LoadMagicItemScreen>:
    name: 'load magic item'
''')


class artificerApp(App):
    def build(self):
        return root_widget


artificerApp().run()
