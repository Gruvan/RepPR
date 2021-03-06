from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from kivy.adapters.listadapter import ListAdapter
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput

from kivy.uix.spinner import Spinner

from liftCalc import *

# lista = [{"weight": 90, "reps": 3, "est1RM": 100},
#          {"weight": 81, "reps": 4, "est1RM": 95},
#          {"weight": 72, "reps": 5, "est1RM": 90},
#          {"weight": 71, "reps": 6, "est1RM": 80},
#          {"weight": 70, "reps": 6, "est1RM": 80},
#          {"weight": 73, "reps": 6, "est1RM": 80},
#          {"weight": 12, "reps": 6, "est1RM": 80},
#          {"weight": 23, "reps": 6, "est1RM": 80},
#          {"weight": 12, "reps": 6, "est1RM": 80}]


def prettyOutprint(dicts):
    for row in dicts:
        row["text"] = str(row["weight"]) \
            + " kg x " + str(row["reps"]) \
            + " reps ---> " + str(row['est1RM']) + " kg"
    return dicts


def my_callback():
    print("hej")


lista = EpleySort(lista)
lista = filterDuplicates(lista)
prettyOutprint(lista)


class LiftListButton(ListItemButton):
    pass


class RV(RecycleView):
        def __init__(self, **kwargs):
            super(RV, self).__init__(**kwargs)
            self.data = lista
            # self.reps = lista["reps"]

            def updateRecord(self):
                pass


class RepPRLayout(BoxLayout):
    nReps = ObjectProperty()
    weight = ObjectProperty()
    est1RM = ObjectProperty()

    def clk(self):
        print "hJEHEJ"

    def replaceLift(self):
        pass


class RepPRApp(App):
    def build(self):
        #  self.load_kv('reppr.kv')
        return RepPRLayout()


if __name__ == "__main__":
    RepPRApp().run()
