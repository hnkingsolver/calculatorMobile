from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""
StackLayout:
    orientation: 'lr-bt'
    padding: 20
    spacing: 10
    Button:
        text: 'B1'
        size_hint: .2, .1
    Button:
        text: 'B2'
        size_hint: .2, .1
    Button:
        text: 'B3'
        size_hint: .2, .1
    Button:
        text: 'B4'
        size_hint: .2, .1

"""))