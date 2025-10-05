from kivy.app import App
from kivy.uix.label import Label

class TesoApp(App):
    def build(self):
        return Label(text="Szia tesó, ez már a saját appod 😎")

TesoApp().run()

