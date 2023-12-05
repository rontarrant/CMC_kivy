# Canadian Mortgage Calculator
# calculatorscreen.py

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import platform
from kivy.properties import ObjectProperty

# local imports
from floatinput import FloatInput
from sanity import Sanity
from mortgagemath import MortgageMath
import error_codes
from currency import format_currency

Builder.load_file("calculatorscreen.kv")


class CalculatorScreen(Screen):
	current_input = ObjectProperty()
	sanity = Sanity()
	mortgage_math = MortgageMath()
	
	def update_current_input(self, text):
		# print("Updating current_input")
		# print("Number: ", self.manager.get_screen('numpad').number)
		print("CalculatorScreen.current_input: ", self.current_input)
		# print("fieldinput: ", self.manager.ids.numpad.ids.fieldinput.text)
		self.current_input.text = text


class HelpButton(Button):
	def on_press(self):
		print("Going to Help Screen...")


class ResetButton(Button):
	pass


class CalculateButton(Button):
	flags = {'home_price': False,
			'down_payment': False,
			'mortgage_principal': False,
			'interest_rate': False,
			'mortgage_term': False,
			'amortization_period': False}

	def on_press(self):
		screen = App.get_running_app().root.get_screen('calculator')

		# run sanity checks and store results
		self.flags['home_price'] = screen.ids.home_price_input.sanity_check()
		self.flags['down_payment'] = screen.ids.down_payment_input.sanity_check()
		self.flags['mortgage_principal'] = screen.ids.mortgage_principal_label.sanity_check()
		self.flags['interest_rate'] = screen.ids.interest_rate_input.sanity_check()
		self.flags['mortgage_term'] = screen.ids.mortgage_term_input.sanity_check()
		self.flags['amortization_period'] = screen.ids.amortization_period_input.sanity_check()

		failure = None # assume success of all flags

		while True:
			if False in self.flags.values():
				failure = [key for key, value in self.flags.items() if value == False][0]
				print(f"SANITY: failed on: '{failure}'.")
				break
			elif all(self.flags.values()):
				print("All flags True.")
				all_good = True
				break

		if not failure:
			# store the numbers...
			storage = screen.mortgage_math
			storage.home_price = float(screen.ids.home_price_input.text)
			storage.down_payment = float(screen.ids.down_payment_input.text)
			storage.mortgage_principal = float(storage.home_price - storage.down_payment)
			storage.interest_rate = float(screen.ids.interest_rate_input.text)
			storage.mortgage_term = float(screen.ids.mortgage_term_input.text)
			storage.amortization_period = float(screen.ids.amortization_period_input.text)
			# do the math
			screen.mortgage_math.calculate_monthly_payments()
			screen.ids.mortgage_principal_label.text = format_currency(storage.mortgage_principal)
			screen.ids.monthly_payment_label.text = format_currency(storage.monthly_payment)

			# make pretty
			screen.ids.home_price_input.text = format_currency(float(screen.ids.home_price_input.text))
			screen.ids.down_payment_input.text = format_currency(float(screen.ids.down_payment_input.text))

			print("Home Price stored as: ", str(storage.home_price))
			print("Down Payment stored as: ", str(storage.down_payment))
			print("Mortgage Principal stored as: ", str(storage.mortgage_principal))
			print("Interest Rate stored as: ", str(storage.interest_rate))
			print("Mortgage Term stored as: ", str(storage.mortgage_term))
			print("Amortization Period stored as: ", str(storage.amortization_period))
			print("Retrieved from mortgage_math: ", str(storage.monthly_payment))

class HomePriceInput(FloatInput):
	def sanity_check(self) -> bool:
		screen = App.get_running_app().root.get_screen('calculator')
		# print("Doing Home Price sanity check...")
		result = screen.sanity.check_home_price(self.text)
		return result
	
	def reset(self):
		print("Resetting HomePriceInput...")


class DownPaymentInput(FloatInput):
	def sanity_check(self) -> bool:
		screen = App.get_running_app().root.get_screen('calculator')
		# print("Doing Down Payment sanity check...")
		result = screen.sanity.check_down_payment(self.text)
		return result

	def reset(self):
		print("Resetting DownPaymentInput...")


class MortgagePrincipalLabel(Label):
	def sanity_check(self) -> bool:
		screen = App.get_running_app().root.get_screen('calculator')
		home_price = screen.ids.home_price_input
		down_payment = screen.ids.down_payment_input
		# print("Doing Mortgage Principal sanity check...")
		# screen.sanity.check_mortgage_principal(self.text)
		result = screen.sanity.compare_price_to_down(home_price, down_payment)
		return result

	def reset(self):
		print("Resetting MortgagePrincipalLabel...")


class InterestRateInput(FloatInput):
	def sanity_check(self) -> bool:
		screen = App.get_running_app().root.get_screen('calculator')
		# print("Doing Interest Rate sanity check...")
		result = screen.sanity.check_interest_rate(self.text)
		return result

	def reset(self):
		print("Resetting InterestRateInput...")


class MortgageTermInput(FloatInput):
	# Mortgage Term criteria:
	# - non-zero
	# - not blank
	# - minimum 6 months (.5 years)
	# - maximum 10 years
	def sanity_check(self) -> bool:
		screen = App.get_running_app().root.get_screen('calculator')
		# print("Doing Mortgage Term sanity check...")
		result = screen.sanity.check_mortgage_term(self.text)
		return result

	def reset(self):
		print("Resetting MortgageTermInput...")


class AmortizationPeriodInput(FloatInput):
	# Amortization Period criteria:
	# - minimum: 6 months (.5 years)
	# - if down payment == 20%, maximum: 35 years
	# - if down payment < 20%, maximum: 25 years
	def sanity_check(self) -> bool:
		screen = App.get_running_app().root.get_screen('calculator')
		# print("Doing Amortization Period sanity check...")
		result = screen.sanity.check_amortization_period(self.text)
		return result

	def reset(self):
		print("Resetting AmortizationPeriodInput...")

class MonthlyPaymentLabel(Label):
	def reset(self):
		print("Resetting Monthly Payment Label.")