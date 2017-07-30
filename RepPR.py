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


lista = [{"weight": 90, "reps": 3, "est1RM": 100},
         {"weight": 81, "reps": 4, "est1RM": 95},
         {"weight": 72, "reps": 5, "est1RM": 90},
         {"weight": 70, "reps": 6, "est1RM": 80}]


def prettyOutprint(dicts):
    for row in dicts:
        row["text"] = str(row["est1RM"]) \
            + " kg x " + str(row["reps"]) \
            + " reps"
    return dicts


def my_callback():
    print("hej")


prettyOutprint(lista)


class LiftListButton(ListItemButton):
    pass


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)




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
