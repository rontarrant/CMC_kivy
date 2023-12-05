from enum import Enum

Errors = [
	"Home Price cannot be zero.",
	"Home Price cannot be blank.",
	"Home Price must be at least $3000.00",
	"Down Payment cannot be zero.",
	"Down Payment cannot be blank.",
	"Down Payment cannot be higher than Home Price.",
	"Down Payment must be at least 5% of Home Price.",
	"Interest Rate cannot be zero.",
	"Interest Rate cannot be blank.",
	"Interest Rate too high.",
	"The down payment is greater than the home price.",
	"The down payment must be at least 5% of the home price.",
	"Home Price, Down Payment, and Interest Rate must all be filled in.",
	"Mortgage Term cannot be zero.",
	"Mortgage Term cannot be blank.",
	"Mortgage Term must be at least six months (enter as 0.5 years).",
	"Mortgage Term cannot be longer than 10 years.",
	"Amortization Period cannot be zero.",
	"Amortization Period cannot be blank.",
	"Amortization Period is lower than five years.",
	"Amortization Period is longer than 35 years.",
	"With a Down Payment of less than 20% (a High Ratio mortgage), Amortization Period must be 25 years or less.",
	"Both Mortgage Term and Amortization Period fields must be filled in."
]

class ErrorCodes(Enum):
	HOME_PRICE_ZERO = 0
	HOME_PRICE_BLANK = 1
	HOME_PRICE_LOW = 2
	DOWN_PAYMENT_ZERO = 3
	DOWN_PAYMENT_BLANK = 4
	DOWN_PAYMENT_TOO_HIGH = 5
	DOWN_PAYMENT_TOO_LOW = 6
	INTEREST_RATE_ZERO = 7
	INTEREST_RATE_BLANK = 8
	INTEREST_RATE_TOO_HIGH = 9
	DOWN_PAYMENT_HIGH = 10
	DOWN_PAYMENT_LOW = 11
	COST_FIELD_EMPTY = 12
	TERM_ZERO = 13
	TERM_BLANK = 14
	TERM_SHORT = 15
	TERM_LONG = 16
	AMORTIZATION_ZERO = 17
	AMORTIZATION_BLANK = 18
	AMORTIZATION_LOW = 19
	AMORTIZATION_HIGH = 20
	AMORTIZATION_TO_DOWN_LONG = 21
	MORTGAGE_FIELD_EMPTY = 22

print("HOME_PRICE_BLANK: ", ErrorCodes.HOME_PRICE_BLANK.value)
print("error: ", Errors[ErrorCodes.HOME_PRICE_ZERO.value])
