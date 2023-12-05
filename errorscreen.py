## errorscreen.py

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

## local imports
Builder.load_file("errorscreen.kv")


class ErrorScreen(Screen):
	pass


