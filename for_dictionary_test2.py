# Test:
# Start with a set of items that need to be tested.
# Create a set of flags to keep track of whether or not each item has passed its test.
# Find the appropriate sanity check for each item, and
# set the flag for that item to True or False based on the sanity check.
# If all items pass, go to the next step.
# If just one item doesn't pass, stop all actions.
import json
import pprint

def pretty(dictionary, indent = 0):
	for key, value in dictionary.items():
		print(' ' * indent + str(key))
		
		if isinstance(value, dict):
			pretty(value, indent + 1)
		else:
			print(' ' * (indent + 1) + str(value))

def home_price():
    print("home_price called.")
    return True

def down_payment() -> bool:
    print("down_payment called.")
    return True

def interest_rate() -> bool:
    print("interest_rate called.")
    return True

def mortgage_term() -> bool:
    print("mortgage_term called.")
    return False

def amortization_period() -> bool:
    print("amortization_period called.")
    return False

flags_and_callers = {'home_price': False,
                     'down_payment': False,
                     'interest_rate': False,
                     'mortgage_term': False,
                     'amortization_period': False}


for function, flag in flags_and_callers.items():
	return_value = eval(function + '()')
	flags_and_callers[function] = return_value
	
	if not return_value:
		break


#pretty(flags_and_callers)
so_pretty = json.dumps(flags_and_callers, indent = 1)
print(so_pretty)
#pprint.pprint(flags_and_callers, compact = False)
