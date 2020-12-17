from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Cone(BoxLayout):
    
    def __init__(self, **kwargs):
        super(Cone, self).__init__(**kwargs)

        self.padding = 200
        
        button = Button(text='hannah kingsolver')
        self.add_widget(button)
        
class Ctwo(App):
    def build(self):
        return Cone()

if __name__ == '__main__':
    Ctwo().run()