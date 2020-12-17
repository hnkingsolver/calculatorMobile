from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button

class Controller2(FloatLayout):
    
    def __init__(self, **kwargs):
        super(Controller2, self).__init__(**kwargs)
        
        button = Button(text='Hello World', color=(.9, 0, .8,1), font_size= 15, pos_hint= {'x': .7, 'y': .8}, size_hint=(.1,.1))
        self.add_widget(button)
        
        button = Button(text='Im your...', color=(.9, .1, .2,1), font_size= 10, pos_hint= {'x': .5, 'y': .5}, size_hint=(.2,.2))
        self.add_widget(button)
        
        button = Button(text='Wild girl', color=(.5, 0, .7,1), font_size= 25, pos_hint= {'x': .2, 'y': .3}, size_hint=(.3,.4))
        self.add_widget(button)
        
class Controller2App(App):
    def build(self):
        return Controller2()
    
    
if __name__ == '__main__':
    Controller2App().run()