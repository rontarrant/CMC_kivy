# Python imports


# Kivy imports
from kivy.properties import StringProperty, ObjectProperty

# local imports
import error_codes
from currency import format_currency

class Sanity():
	# Cost scene sanity flags
	home_price_ok = False
	interest_rate_ok = False
	down_payment_ok = False
	price_to_down_ok = False
	high_ratio = False # True if down payment is less than 20%

	# Mortgage scene sanity flags
	mortgage_principal_ok = False
	mortgage_term_ok = False
	amortization_period_ok = False

	# local imports
	import error_codes

	error_message: StringProperty()


	def reset_sanity_flags():
		print("sanity.set_sanity_flags")
		self.home_price_ok = False
		self.interest_rate_ok = False
		self.down_payment_ok = False
		self.price_to_down_ok = False
		self.high_ratio = False

		self.mortgage_principal_ok = False
		self.mortgage_term_ok = False
		self.amortization_period_ok = False
		

	# NOTE: Incoming numbers must be strings.
	def check_home_price(self, _home_price: str) -> bool:
		# Home Price criteria:
		# - not blank
		# - non-zero
		# - minimum $3000
		price: float
		# print("check_home_price: ", _home_price)
		# if we're reentering a field where a number has already been checked,
		# flip the flag so we can check the new, edited number.
		if(self.home_price_ok == True):
			self.home_price_ok = False

		match _home_price:
			case "":
				# print("Sanity: No Home Price entered.")
				self.error_code = error_codes.ErrorCodes.HOME_PRICE_BLANK.value
				self.home_price_ok = False
			case _:
				# convert to float before the next test
				price = float(_home_price)
				
				if(price == 0):
					# print("Sanity: Zero asking price")
					self.error_code = error_codes.ErrorCodes.HOME_PRICE_ZERO.value
					self.home_price_ok = False
				elif(price < 3000.00):
					# print("Sanity: Home Price too low.")
					self.error_code = error_codes.ErrorCodes.HOME_PRICE_LOW.value
					self.home_price_ok = False
				else:
					self.home_price_ok = True
		
		# print("home_price_ok flag: ", self.home_price_ok)
		return self.home_price_ok


	def check_down_payment(self, _down_payment: str) -> bool:
		# Down Payment criteria:
		# - non-zero
		# - not blank
		# - must be more than Home Price
		# - minimum: 5% of Home Price entered above
		# - if it's less than 20%, set High Ratio flag
		down_payment: float

		# if we're reentering a field where a number has already been checked,
		# flip the flag so we can check the new, edited number.
		if(self.down_payment_ok == True):
			self.down_payment_ok = False

		match _down_payment:
			case "":
				# print("Sanity: No Down Payment entered.")
				self.error_code = error_codes.ErrorCodes.DOWN_PAYMENT_BLANK.value
				self.down_payment_ok = False
			case _:
				down_payment = float(_down_payment)
				
				if(down_payment == 0):
					# print("Sanity: Zero down")
					self.error_code = error_codes.ErrorCodes.DOWN_PAYMENT_ZERO.value
					self.down_payment_ok = False
				else:
					self.down_payment_ok = True
		# print("down_payment_ok flag: ", self.down_payment_ok)		
		return self.down_payment_ok

	# Not needed. In the Godot version, it was never called.
	def check_mortgage_principal(self, _principal: float) -> bool:
		# maximum: 95% of Home Price
		# not blank
		if(self.mortgage_principal_ok == True):
			self.mortgage_principal_ok = False
		
		# print("_principal: ", _principal)
		match _principal:
			case "":
				# print("Sanity: No Principal calculated.")
				self.error_code = error_codes.ErrorCodes.PRINCIPAL_BLANK
			case _:
				principal = float(_principal)
		
				if(principal > 2400):
					self.mortgage_principal_ok = True
				else:
					self.mortgage_principal_ok = False
		# print("mortgage_principal_ok: ", self.mortgage_principal_ok)
		return self.mortgage_principal_ok


	# Somewhere in here, we need to determine the percentage of
	# the down payment and set a local flag accordingly.
	def compare_price_to_down(self, _home_price, _down_payment):
		# Mortgage Principal criteria:
		# - maximum: 95% of Home Price
		# - non-zero
		# - not blank
		home_price: float
		down_payment: float
		
		# reset flags
		if(self.price_to_down_ok == True):
			self.price_to_down_ok = False
		
		if(self.high_ratio == True):
			self.high_ratio = False
			# print("Turning high_ratio FLAG OFF")
			#emit_signal("set_high_ratio_flag", False)
		
		# make sure we have data to work with
		match _home_price.text:
			case "":
				# print("Sanity: No Home Price entered.")
				self.error_code = error_codes.ErrorCodes.HOME_PRICE_BLANK.value
				self.home_price_ok = False
			case _:
				home_price = float(_home_price.text)

		match _down_payment.text:
			case "":
				# print("Sanity: No Down Payment entered.")
				self.error_code = error_codes.ErrorCodes.DOWN_PAYMENT_BLANK
				self.down_payment_ok = False
			case _:
				down_payment = float(_down_payment.text)

		if self.home_price_ok == False | self.down_payment_ok == True:
			# Home Price is less than Down Payment
			# User doesn't need a mortgage.
			if(home_price < down_payment):
				self.price_to_down_ok = False # defaults to False if test doesn't pass
				self.error_code = error_codes.ErrorCodes.DOWN_PAYMENT_TOO_HIGH.value
				#emit_signal("error_condition", self.error_code)
			# maximum principal: 95% of home price
			# Not allowed
			elif(down_payment < (home_price * .05)):
				# print("down_payment be at least 5% (" + format_currency(home_price * .05) + ") of home price (" + format_currency(home_price) + ")")
				self.price_to_down_ok = False
				self.error_code = error_codes.ErrorCodes.DOWN_PAYMENT_TOO_LOW.value
				#emit_signal("error_condition", self.error_code)
			# Down Payment is less than 20% of Home Price
			# (High-ratio mortgage)
			elif(down_payment < (home_price * .20)):
				# print("down_payment is less than 20% " + str(home_price * .2) + " of home_price: " + str(home_price - down_payment))
				self.price_to_down_ok = True
				self.high_ratio = True
				# print("Turning high_ratio FLAG ON")
				#emit_signal("set_high_ratio_flag", True)
				# print("\bHigh ratio mortgage. Flag set.")
				#emit_signal("price_to_down_okay", home_price - down_payment)
			# Down Payment is > 20% (Low ratio mortgage)
			else:
				# print("The down payment looks good.")
				self.price_to_down_ok = True
				return self.price_to_down_ok
				# set price/down ratio variable
				#emit_signal("price_to_down_okay", home_price - down_payment)
		else:
			pass
			# print("Either Home Price or Down Payment (or both) was left blank making Mortgage Principal invalid.")


	def check_interest_rate(self, _interest_rate: str) -> bool:
		# Interest Rate criteria:
		# - non-zero
		# - not blank
		# - at least .01%
		# - can't be more than 20%
		interest_rate: float

		# if we're reentering a field where a number has already been checked,
		# flip the flag so we can check the new, edited number.
		if(self.interest_rate_ok == True):
			self.interest_rate_ok = False

		match _interest_rate:
			case "":
				# print("Sanity: No Interest Rate entered.")
				self.error_code = error_codes.ErrorCodes.INTEREST_RATE_BLANK.value
				self.interest_rate_ok = False
			case _:
				interest_rate = float(_interest_rate)
				
				if(interest_rate == 0):
					# print("Sanity: Zero Interest")
					self.error_code = error_codes.ErrorCodes.INTEREST_RATE_ZERO.value
					self.interest_rate_ok = False
				elif(interest_rate > 20):
					self.error_code = error_codes.ErrorCodes.INTEREST_RATE_TOO_HIGH.value
					# print("Sanity: Interest rate over 20%")
					self.interest_rate_ok = False
				else:
					self.interest_rate_ok = True
					
		return self.interest_rate_ok
		# minimum: 0.01%


	def check_mortgage_term(self, _term_in_years: str) -> bool:
		# not empty
		# minimum: 6 months
		# maximum: 10
		term: float

		# if we're reentering a field where a number has already been checked,
		# flip the flag so we can check the new, edited number.
		if(self.mortgage_term_ok == True):
			self.mortgage_term_ok = False

		match _term_in_years:
			case "":
				# print("Sanity: No Mortgage Term entered.")
				self.error_code = error_codes.ErrorCodes.TERM_BLANK.value
				self.mortgage_term_ok = False
			case _:
				# convert to float before the next test
				term = float(_term_in_years)
				
				if(term == 0):
					# print("Sanity: Term is Zero")
					self.error_code = error_codes.ErrorCodes.TERM_ZERO.value
					self.mortgage_term_ok = False
				elif(term < 0.5):
					# print("Sanity: Term too short.")
					self.error_code = error_codes.ErrorCodes.TERM_SHORT.value
					self.mortgage_term_ok = False
				elif(term > 10):
					# print("Sanity: Term is too long.")
					self.error_code = error_codes.ErrorCodes.TERM_LONG.value
				else:
					self.mortgage_term_ok = True
					
		return self.mortgage_term_ok


	def check_amortization_period(self, _amortization_period_in_years: str) -> bool:
		# minimum: 6 months
		# if down payment = 20%, maximum: 35 years
		# if down_payment < 20%, maximum: 25 years
		amortization: float
		# print("Checking Amortization Period...")
		
		# if we're reentering a field where a number has already been checked,
		# flip the flag so we can check the new, edited number.
		if(self.amortization_period_ok == True):
			self.amortization_period_ok = False
		
		match _amortization_period_in_years:
			case "":
				# print("Sanity: No Amortization Period entered.")
				self.error_code = error_codes.ErrorCodes.AMORTIZATION_BLANK.value
				self.amortization_period_ok = False
			case _:
				# convert to float before the next test
				amortization = float(_amortization_period_in_years)
				
				if(amortization == 0):
					# print("Sanity: Amortization Period is Zero")
					self.error_code = error_codes.ErrorCodes.AMORTIZATION_ZERO.value
					self.amortization_period_ok = False
				elif(amortization < 0.5):
					# print("Sanity: Amortization Period too short.")
					self.error_code = error_codes.ErrorCodes.AMORTIZATION_LOW.value
					self.amortization_period_ok = False
				elif(amortization > 35):
					self.amortization_period_ok = False
					self.error_code = error_codes.ErrorCodes.AMORTIZATION_HIGH.value
				elif(amortization > 25):
					if self.high_ratio == True:
						# print("Sanity: Amortization Period too long for high ratio mortgage.")
						self.error_code = error_codes.ErrorCodes.AMORTIZATION_TO_DOWN_LONG.value
						self.amortization_period_ok = False
					else:
						self.amortization_period_ok = True
				else:
					self.amortization_period_ok = True
					
		return self.amortization_period_ok


	# origin: Numpad.gd, signal: sane_input_check
	def match_field(self, _current_label: ObjectProperty, _current_input: ObjectProperty, _number: str):
		# print("Sanity.gd...")
		pass

		match _current_label.text:
			case "House Price $":
				if self.check_home_price(_number) == True:
					# print("Sanity: home_price")
					# emit_signal("home_price_okay", _current_label, _number) # Math._on_Sanity_home_price_okay()
					pass
				else:
					# print("Error found in home price. Calling error screen.")
					# emit_signal("error_condition", self.error_code) # go to Error screen
					pass
			case "Down Payment $":
				if self.check_down_payment(_number) == True:
					# print("Sanity: down_payment check")
					# emit_signal("down_payment_okay", _current_label, _number)
					pass
				else:
					# print("Error found in down payment. Calling error screen.")
					# emit_signal("error_condition", self.error_code)
					pass
			case "Interest Rate %":
				if self.check_interest_rate(_number) == True:
					# print("Sanity: interest rate check")
					# emit_signal("interest_rate_okay", _current_label, _number)
					pass
				else:
					# print("Error found in down payment. Calling error screen.")
					# emit_signal("error_condition", self.error_code)
					pass
			case "Mortgage Term (yrs)":
				# print("Sanity: mortgage_term")
				if self.check_mortgage_term(_number) == True:
					# print("Sanity: mortgage_term okay")
					# emit_signal("mortgage_term_okay", _current_label, _number)
					pass
				else:
					# print("Error found in mortgage term.")
					# emit_signal("error_condition", self.error_code)
					pass
			case "Amortization Period (yrs)":
				# print("Sanity: amortization_period")
				pass
				
				if check_amortization_period(_number) == True:
					# print("Sanity: amortization_period okay")
					# emit_signal("amortization_period_okay", _current_label, _number)
					pass
				else:
					# print("Error on amortization period.")
					# emit_signal("error_condition", self.error_code)
					pass


	# origin: Cost.gd, signal: next_pressed
	def check_cost_entries(self, _price: ObjectProperty, _down: ObjectProperty):
		# print("Checking all cost fields...")
		
		if(home_price_ok == True & down_payment_ok == True & interest_rate_ok == True):
			# print("Sanity: check_cost_entries - comparing home price to down payment...")
			compare_price_to_down(_price, _down)
		else:
			# print("Not all fields are filled in.")
			# emit_signal("error_condition", error_codes.ErrorCodes.FIELD_EMPTY.value)
			pass


	def mortgage_sanity_check(self, _term: ObjectProperty, _amortization: ObjectProperty):
		# print("Sanity: Checking all mortgage fields...")
		
		# It's assumed that all other sanity checks have been passed by now.
		if(mortgage_term_ok == True & amortization_period_ok == True):
			# print("Sanity: mortgage entries checked.")
			# emit_signal("mortgage_fields_okay")
			pass
		else:
			# print("Sanity: Not all mortgage fields are filled in.")
			# emit_signal("error_condition", error_codes.ErrorCodes.FIELD_EMPTY.value)
			pass
