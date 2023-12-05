# Canadian Mortgage Calculator

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import platform
from kivy.properties import ObjectProperty

from calculatorscreen import CalculatorScreen
from numpadscreen import NumPadScreen
from helpscreen import HelpScreen
from errorscreen import ErrorScreen


class WindowManager(ScreenManager):
	pass


class CMCApp(App):
	def build(self):
		if (platform == 'android') | (platform == 'ios'):
			Window.maximize()
		else:
			Window.size = (600, 1024)
			Window.left = 1100
			Window.top = 50

		return Builder.load_file("manager.kv")
	

if __name__ == "__main__":
	CMCApp().run()
