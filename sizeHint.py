from kivy.lang import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string("""
FloatLayout:
    Button:
        text: 'B1'
        size_hint: 0.2, 0.1
        post_hint: {'down':1, 'lift':1}
"""))