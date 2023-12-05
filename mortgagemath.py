from kivy.properties import ObjectProperty

class MortgageMath():
	# signalhome_price_stored
	# signaldown_payment_stored
	# signalinterest_rate_stored
	# signalprincipal_stored
	# signalterm_stored
	# signalamortization_stored
	# signaldisplay_final

	# presets
	annual_compounding_periods: float = 2.0
	exponent: float = 1.0 /12.0

	home_price: float # (from user)
	down_payment: float # (from user)
	mortgage_principal: float # (from user)
	interest_rate: float # (from user)
	mortgage_term: float # (from user)
	amortization_period: float # in years (from user)
	
	nominal_rate: float # interest rate translated into a percentage
	effective_rate: float # interest rate (compounding 2 times, not 12, per year)
	monthly_periodic_rate: float # percent interest charged per month
	amortization_months: float # in months
	monthly_payment: float # calculated payment

	high_ratio: bool = False
	mortgage_premium: float


	def reset(self):
		# set all to no value
		self.home_price = None
		self.down_payment = None
		self.interest_rate = None
		self.mortgage_principal = None
		self.mortgage_term = None
		self.amortization_period = None


	def set_high_ratio_flag(self, _state: bool):
		self.high_ratio = _state


	def calculate_mortgage_premium(self):
		# CMHC Mortgage Insurance premiums are calculated for all high-ratio mortgages.
		# The interest rate varies based on the size of the down payment.
		# 5% to 9.99% down = 4.0% insurance premium
		# 10% to 14.99% down = 3.1% insurance premium
		# 15% to 19.99% down = 2.8% insurance premium
		# The premium is usually included in the mortgage amount.
		print("Calculating CMHC Mortgage Insurance Premium...")

		# Find out what percent of the home price the down payment is.
		percent_down = self.down_payment / self.home_price
		# Use that percent to decide which premium rate to use.
		if percent_down >= .15 & percent_down < .2:
			self.mortgage_premium = self.mortgage_principal * 0.028
		elif percent_down >= .1 & percent_down < .15:
			self.mortgage_premium = self.mortgage_principal * 0.031
		elif percent_down >= .05 & percent_down < .1:
			self.mortgage_premium = self.principal * 0.04
		print("mortgage_premium: " + str(self.mortgage_mortgage_premium))


	def calculate_cmhc_premium_tax(self):
		pass
		# This is different depending on which province you're buying in,
		# but in general, the buyer pays provincial tax on the CMHC premium.
		# Information is sparse, but this is what I have as of 2023-02-08:
		# Ontario 8%
		# Quebec 9% (or a sliding scale, not sure which it is yet)
		# Saskcatchewan 6%
		# No other provinces or territories charge tax on the CMHC premium.
		# The result is NOT added into the mortgage; it's one of the closing costs.


	def calculate_monthly_payments(self):
		self.nominal_rate = self.interest_rate / 100
		
		print("ENTERING: calculate_monthly_payments()")
		print("nominal_rate: ", self.nominal_rate)
		print("principal: ", self.mortgage_principal)
		print("amortization_period: ", self.amortization_period)
		
		# If it's a high ratio mortgage, add in CMHC mortgage premium.
		if(self.high_ratio == True):
			if(self.mortgage_premium > 0): # clean the slate to avoid errors
				self.mortgage_premium = 0
			self.calculate_mortgage_premium()
			self.mortgage_principal = self.mortgage_principal + self.mortgage_premium
		else:
			self.mortgage_premium = 0
		
		self.amortization_months = self.get_amortization_months()
		self.effective_rate = pow(1.0 + self.nominal_rate / self.annual_compounding_periods, 2.0) - 1.0 # done
		
		print("effective rate: ", self.effective_rate) # not needed
		# print("exponent: ", exponent) # not needed
		
		self.monthly_periodic_rate = pow(1.0 + self.effective_rate, self.exponent) - 1.0 # done
		print("monthly periodic rate:", self.monthly_periodic_rate) # not needed
		
		self.monthly_payment = self.get_monthly_payment() # done
		print("Monthly payment: " + str(self.monthly_payment))
		
		# emit_signal("display_final", home_price, down_payment,
		#			interest_rate, mortgage_principal, mortgage_term,
		#			amortization_period, monthly_payment, mortgage_premium)


	def get_amortization_months(self) -> float:
		months: float = 12.0
		return self.amortization_period * months
		
		
	def get_monthly_payment(self) -> float:
		print("ENTERING: get_monthly_payment()")
		# print("monthly_periodic_rate: ", monthly_periodic_rate)
		# print("principal: ", self.mortgage_principal)
		print("amortization_months: ", self.amortization_months)
		
		payment: float = (self.monthly_periodic_rate * self.mortgage_principal) / (1.0 - (1.0 / pow(1.0 + self.monthly_periodic_rate, self.amortization_months)))
		
		return payment


	def store_value(self, _label: str, _number: str):
		print("store_value()")
		
		match _label:
			case "House Price $":
				self.home_price = float(_number)
				print("Math.gd - home_price: " + str(self.home_price))
				# emit_signal("home_price_stored") # goes to Main.gd - _on_Math_home_price_stored()
			case "Down Payment $":
				self.down_payment = float(_number)
				print("Math.gd - down_payment: " + str(self.down_payment))
				# emit_signal("down_payment_stored")
			case "Interest Rate %":
				self.interest_rate = float(_number)
				print("Math.gd - interest_rate: " + str(self.interest_rate))
				# emit_signal("interest_rate_stored")
			case "Mortgage Term (yrs)":
				self.mortgage_term = float(_number)
				print("Math.gd - mortgage_term: " + str(self.mortgage_term))
				# emit_signal("term_stored")
			case "Amortization Period (yrs)":
				self.amortization_period = float(_number)
				# emit_signal("amortization_stored")
				print("Math.gd - amortization_period: " + str(self.amortization_period))


	# origin: Sanity.gd, signal: price_to_down_okay
	def store_principal(self, _principal: float):
		self.mortgage_principal = _principal
		# emit_signal("principal_stored", str(down_payment), str(_principal))
