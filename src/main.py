from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.picker import MDTimePicker
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.theming import ThemableBehavior
from kivymd.icon_definitions import md_icons
from helper import load_colors
import json


'''
canvas.before:
    Color:
        rgba: (1,0,0,1)
    Rectangle:
        size: self.size
        pos: self.pos
'''

colors = load_colors()
print(colors)

class MainScreen(MDScreen):
    def save_class(self):
        #assume this is mongoDB, I don't have it on my system now :("
        with open("database.json", "r") as f:
            self.data = json.load(f) 
        if len(self.ids.username.text) >= 5:
            if self.ids.yoga.active:
                self.add_class("yoga")
            elif self.ids.dance.active:
                self.add_class("dance")
            elif self.ids.gym.active:
                self.add_class("gym")

    def add_class(self, classname):
            if self.data["capacity"][classname] >= 0:
                self.data["classes"].append({"class": classname, "user": self.ids.username.text, "time": str(self.time_dialog.time)})
                self.data["capacity"][classname] -= 1
            else:
                self.data["waiting_list"].append({"class": classname, "user": self.ids.username.text, "time": str(self.time_dialog.time)})
            with open("database.json", "w") as f:
                json.dump(self.data, f, indent=2)

    def show_time_picker(self):
        self.time_dialog = MDTimePicker()
        self.time_dialog.bind(time=self.get_time)
        self.time_dialog.open()

    def get_time(self, instance, time):
        return time
    def cancel_class(self):
        classname = ""
        print(self.time_dialog.time)
        if self.ids.yoga.active:
            classname = "yoga"
        elif self.ids.dance.active:
            classname = "gym"
        elif self.ids.gym.active:
            classname = "dance"
        with open("database.json", "r") as f:
            self.data = json.load(f) 
        try:
            self.data["classes"].remove({"class":classname, "time":str(self.time_dialog.time), "username": self.username.text})
        except:
            print("Entry does not exist")



class ContentNavigationDrawer(BoxLayout):
    pass

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()

class ContentNavigationDrawer(BoxLayout):
    pass

class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class KuddleApp(MDApp):
    icons = list(md_icons.keys())[15:30]

    def build(self):
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Teal"
        #self.theme_cls.accent_palette = "Teal"

    def on_start(self):
        pass


KuddleApp().run()
