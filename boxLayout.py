from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
    
BoxLayout:
    oreintation: 'vertical'
    spacing: 50
    padding: 50
    Button:
        text: 'Button 1'
    Button:
        text: 'Button 2'
'''))