from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string("""
GridLayout:
    rows:3
    Button:
        text:'Button 1'
    Button:
        text:'Button 2'
    Button:
        text:'Button 3'
    Button:
        text:'Button 4'
    Button:
        text:'Button 1'
    Button:
        text:'Button 2'
    Button:
        text:'Button 3'
    Button:
        text:'Button 4'
    Button:
        text:'Button 1'
    Button:
        text:'Button 2'
    Button:
        text:'Button 3'
    Button:
        text:'Button 4'         
"""))