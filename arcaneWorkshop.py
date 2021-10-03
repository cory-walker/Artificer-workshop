import arcana

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.button import Button

al = arcana.ArcaneLab()


class MenuBarButton(Button):
    pass


class MenuBar(BoxLayout):
    pass


class ScrnMain(Screen):
    pass


class ScrnSplash(Screen):
    name = StringProperty("splash")

    def __init__(self, **kwargs):
        super(ScrnSplash, self).__init__(**kwargs)
        bl = BoxLayout(orientation="vertical")
        self.add_widget(bl)
        lbl = Label(text="splash screen")
        bl.add_widget(lbl)


class ScrnMgr(ScreenManager):
    def __init__(self, **kwargs):
        super(ScrnMgr, self).__init__(**kwargs)
        self.add_widget(ScrnSplash())
        self.add_widget(ScrnMain())
        self.current = "main"


root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
ScrnMgr:
    transition: FadeTransition()
    ScrnMain:
    ScrnSplash:

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
        on_release: app.root.current = 'main'
    MenuBarButton:
        text: "New Item"
        on_release: print("new item pressed")
<ScrnMain>
    name: "main"
    BoxLayout:
        orientation: "vertical"
        MenuBar:
        Label:
            text: "Main Menu"
 ''')


class ArcaneWorkshopApp(App):
    def build(self):
        return root_widget


ArcaneWorkshopApp().run()
