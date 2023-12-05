## Canadian Mortgage Calculator
## numpad.py

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty
## local imports
from floatinput import FloatInput

Builder.load_file("numpadscreen.kv")

class FieldIDLabel(Label):
	pass

class FieldInput(FloatInput):
	pass


class NumPadScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
	def set_number_field(self, _number):
		numpad = self.manager.get_screen('numpad')
		numpad.fieldinput = _number
		print("number is set: ", _number)
	



