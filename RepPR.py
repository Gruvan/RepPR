from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button


class MyLabel(BoxLayout):
    pass

class CustomDropDown(DropDown):
    pass

class SimpleKivy(App):
    def build(self):
        CustomDropDown()
        self.load_kv('reppr.kv')

        dropdown = CustomDropDown()
        mainbutton = Button(text='Hello', size_hint=(None, None))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        return MyLabel()






if __name__ == "__main__":
    SimpleKivy().run()