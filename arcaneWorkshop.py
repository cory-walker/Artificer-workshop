import kivy
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

al = arcana.ArcaneLab()


class MenuBarButton(Button):
    def __init__(self, **kwargs):
        super(MenuBarButton, self).__init__(**kwargs)

    def new_item():
        global al
        al.new_item()


class MenuBar(BoxLayout):
    pass


class kivyFactory():

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

    def gen_Label(self, text=""):
        l = Label()
        l.text = text
        return l

    def gen_button(self, text=""):
        b = Button()
        b.text = text
        return b


class ScrnCraftItem(Screen):
    global al
    cur_item = ObjectProperty(al.current_item)
    name = StringProperty('craft item')

    def __init__(self, **kwargs):
        super(ScrnCraftItem, self).__init__(**kwargs)
        kf = kivyFactory()
        blM = kf.gen_BoxLayout()
        self.add_widget(blM)

        # Item Name
        l_in = kf.gen_Label("Item Name")
        t_in = TextInput()
        t_in.bind(text=self.cur_item_name)
        b_in = kf.pack_h_box(widgets=[l_in, t_in])

        # Item Description
        l_id = kf.gen_Label("Item Description")
        t_id = TextInput()
        t_id.bind(text=self.cur_item_description)
        b_id = kf.pack_h_box(widgets=[l_id, t_id])

        # Consumable
        l_ic = kf.gen_Label("Consumable")
        t_ic = CheckBox()
        t_ic.bind(active=self.cur_item_consumable)
        b_ic = kf.pack_h_box(widgets=[l_ic, t_ic])

        # Artifact
        l_ia = kf.gen_Label("Artifact")
        t_ia = CheckBox()
        t_ia.bind(active=self.cur_item_artifact)
        b_ia = kf.pack_h_box(widgets=[l_ia, t_ia])

        # Rarity
        l_ra = kf.gen_Label("Rarity")
        bt_ra = kf.gen_button("Rarity")
        bt_ra.on_release = self.open_rarity_popup()
        bt_ra.text = al.current_item.rarity_str()
        b_ra = kf.pack_h_box(widgets=[l_ra, bt_ra])

        # Load Main BoxLayout
        widgets = [MenuBar(), b_in, b_id, b_ic, b_ia, b_ra]
        for w in widgets:
            blM.add_widget(w)

    def cur_item_name(self, *args):
        al.current_item.name = args[1]

    def cur_item_description(self, *args):
        al.current_item.description = args[1]

    def cur_item_consumable(self, *args):
        al.current_item.is_consumable = args[1]

    def cur_item_artifact(self, *args):
        al.current_item.is_artifact = args[1]

    def open_rarity_popup(self, *args):
        rarPop = RarityPopup()
        rarPop.open()


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


class RarityPopup(Popup):
    def __init__(self, **kwargs):
        super(RarityPopup, self).__init__(**kwargs)

    def update_rarity(self, rarity):
        global al
        al.current_item.rarity = rarity


class ScrnMgr(ScreenManager):
    pass
    # def __init__(self, **kwargs):
    #    super(ScrnMgr, self).__init__(**kwargs)


root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
ScrnMgr:
    transition: FadeTransition()
    ScrnMain:
    ScrnSplash:
    ScrnCraftItem:

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
        on_release: self.new_item; app.root.current = 'craft item'

<ScrnMain>:
    name: "main"
    BoxLayout:
        orientation: "vertical"
        MenuBar:
        Label:
            text: "Main Menu"
<RarityPopup>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "common"
            on_release: root.update_rarity(1); root.dismiss()
        Button:
            text: "uncommon"
            on_release: root.update_rarity(2); root.dismiss()
        Button:
            text: "rare"
            on_release: root.update_rarity(3); root.dismiss()
        Button:
            text: "very rare"
            on_release: root.update_rarity(4); root.dismiss()
        Button:
            text: "legendary"
            on_release: root.update_rarity(5); root.dismiss()

<ScrnCraftItemOrig>:
    name: "craft item orig"

    BoxLayout:
        orientation: "vertical"
        MenuBar:
        BoxLayout:
            orientation: "horizontal"
            Label:
                text: "Item Name"
            TextInput:
                text: root.cur_item.name
        BoxLayout:
            orientation: "horizontal"
            Label:
                text: "Description"
            TextInput:
                text: root.cur_item.description
        BoxLayout:
            orientation: "horizontal"
            Label:
                text: "Consumable"
            CheckBox:
                text: root.cur_item.is_consumable
        BoxLayout:
            orientation: "horizontal"
            Label:
                text: "Artifact"
            CheckBox:
                text: root.cur_item.is_artifact
        BoxLayout:
            id: 'rarBoxLayout'
            orientation: "horizontal"
            Label:
                text: "Rarity"
            Button:
                id: 'rarBtn'
                text: str(root.cur_item.rarity_str())
                on_release: root.open_rarity_popup()


 ''')


class ArcaneWorkshopApp(App):
    def build(self):
        return root_widget


ArcaneWorkshopApp().run()
