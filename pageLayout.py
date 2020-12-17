from kivy.lang import Builder
from kivy.base import runTouchApp
runTouchApp(Builder.load_string("""
PageLayout:
    Button:
        text: 'B1'
    Button:
        text: 'B2'
    Button:
        text: 'B3'

"""))