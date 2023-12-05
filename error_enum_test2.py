from enum import Enum

Errors = {
	1: "Home Price cannot be zero.",
	2: "Home Price cannot be blank.",
	3: "Home Price must be at least $3000.00",
	4: "Down Payment cannot be zero.",
	5: "Down Payment cannot be blank.",
	6: "Down Payment cannot be higher than Home Price.",
	7: "Down Payment must be at least 5% of Home Price.",
	8: "Interest Rate cannot be zero.",
	9: "Interest Rate cannot be blank.",
	10: "Interest Rate too high. You might consider switching mortgage providers.",
	11: "Mortgage Term cannot be zero.",
	12: "Mortgage Term cannot be blank.",
	13: "Mortgage Term must be at least six months (enter as 0.5 years).",
	14: "Mortgage Term cannot be longer than 10 years.",
	15: "Amortization Period cannot be zero.",
	16: "Amortization Period cannot be blank.",
	17: "Amortization Period must be at least five years.",
	18: "Amortization Period cannot be longer than 35 years.",
	19: "With a Down Payment of less than 20% (a High Ratio mortgage), Amortization Period must be 25 years or less.",
	20: "All fields must be filled in."
}

class ErrorCodes(Enum):
	HOME_PRICE_ZERO = 1
	HOME_PRICE_BLANK = 2
	HOME_PRICE_LOW = 3
	DOWN_PAYMENT_ZERO = 4
	DOWN_PAYMENT_BLANK = 5
	DOWN_PAYMENT_TOO_HIGH = 6
	DOWN_PAYMENT_TOO_LOW = 7
	INTEREST_RATE_ZERO = 8
	INTEREST_RATE_BLANK = 9
	INTEREST_RATE_TOO_HIGH = 10
	TERM_ZERO = 11
	TERM_BLANK = 12
	TERM_SHORT = 13
	TERM_LONG = 14
	AMORTIZATION_ZERO = 15
	AMORTIZATION_BLANK = 16
	AMORTIZATION_LOW = 17
	AMORTIZATION_HIGH = 18
	AMORTIZATION_TO_DOWN_LONG = 19
	FIELD_EMPTY = 20

print("error: ", Errors[ErrorCodes.HOME_PRICE_LOW.value])
