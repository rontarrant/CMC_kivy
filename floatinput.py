## generic floating point input

import re ## regular expression library
from kivy.uix.textinput import TextInput
from kivy.app import App


class FloatInput(TextInput):
	pattern = re.compile('[^0-9]') ## equal to '[\d]'
	
	def insert_text(self, substring, from_undo = False):
		pattern = self.pattern
		
		if '.' in self.text: ## there's already a dot
			string = re.sub(pattern, '', substring) ## do nothing
		else:
			string = '.'.join(re.sub(pattern, '', string)
			for string in substring.split('.', 1))
				
		return super().insert_text(string, from_undo = from_undo)


	# This handles the transition from Calculator to NumPad screen
	# and tracks which TextInput initiated the transition.
	def on_focus(self, instance, value):
		## fires on focus IN, but not focus out
		if value:
			## manager is WindowManager (derived from ScreenManager)
			manager = App.get_running_app().root ## create a shortcut for less typing below
			manager.transition.direction = 'left' ## set the transition direction
			manager.current = 'numpad' ## we're heading for the NumPad screen
			manager.get_screen('calculator').current_input = self ## remember which input we're working with so the number returned from numpad goes into the right spot.
			manager.get_screen('numpad') ## goto the numpad screen
			
			## transfer whatever number is already in the input to the numpad input
			if manager.get_screen('calculator').current_input.text:
				text = manager.get_screen('calculator').current_input.text
				print("text in textinput: ", text)
				manager.ids.numpad.ids.fieldinput.text = text
			## if the input has no number, make numpad's fieldinput blank
			else:
				manager.ids.numpad.ids.fieldinput.text = ""
