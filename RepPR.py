from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.listview import ListView, ListItemButton
from kivy.adapters.listadapter import ListAdapter
from kivy.properties import ObjectProperty
from random import random


class LiftListButton(ListItemButton):
    pass


class RepPRLayout(BoxLayout):
    nReps = ObjectProperty()
    weight = ObjectProperty()
    est1RM = ObjectProperty()

    def replaceLift(self):
        pass


class RepPRApp(App):
    def build(self):
#self.load_kv('reppr.kv')
        return RepPRLayout()


if __name__ == "__main__":
    RepPRApp().run()
