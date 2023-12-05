from enum import Enum

class ErrorCodes(Enum):
	HOME_PRICE_ZERO = "Home Price cannot be zero."
	HOME_PRICE_BLANK = "Home Price cannot be blank."
	HOME_PRICE_LOW = "Home Price must be at least $3000.00"
	DOWN_PAYMENT_ZERO = "Down Payment cannot be zero."
	DOWN_PAYMENT_BLANK = "Down Payment cannot be blank."
	DOWN_PAYMENT_TOO_HIGH = "Down Payment cannot be higher than Home Price."
	DOWN_PAYMENT_TOO_LOW = "Down Payment must be at least 5% of Home Price."
	INTEREST_RATE_ZERO = "Interest Rate cannot be zero."
	INTEREST_RATE_BLANK = "Interest Rate cannot be blank."
	INTEREST_RATE_TOO_HIGH = "Interest Rate too high."
	DOWN_PAYMENT_HIGH = "The down payment is greater than the home price."
	DOWN_PAYMENT_LOW = "The down payment must be at least 5% of the home price."
	COST_FIELD_EMPTY = "Home Price, Down Payment, and Interest Rate must all be filled in."
	TERM_ZERO = "Mortgage Term cannot be zero."
	TERM_BLANK = "Mortgage Term cannot be blank."
	TERM_SHORT = "Mortgage Term must be at least six months (enter as 0.5 years)."
	TERM_LONG = "Mortgage Term cannot be longer than 10 years."
	AMORTIZATION_ZERO = "Amortization Period cannot be zero."
	AMORTIZATION_BLANK = "Amortization Period cannot be blank."
	AMORTIZATION_LOW = "Amortization Period is lower than five years."
	AMORTIZATION_HIGH = "Amortization Period is longer than 35 years."
	AMORTIZATION_TO_DOWN_LONG = "With a Down Payment of less than 20% (a High Ratio mortgage), Amortization Period must be 25 years or less."
	MORTGAGE_FIELD_EMPTY = "Both Mortgage Term and Amortization Period fields must be filled in."

print("error: ", ErrorCodes.HOME_PRICE_ZERO)
