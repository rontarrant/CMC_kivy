# Test:
# Start with a set of items that need to be tested.
# Create a set of flags to keep track of whether or not each item has passed its test.
# Find the appropriate sanity check for each item, and
# set the flag for that item to True or False based on the sanity check.
# If all items pass, go to the next step.
# If just one item doesn't pass, stop all actions.


def home_price():
    print("home_price called.")
    return True

def down_payment() -> bool:
    print("down_payment called.")
    return True

def interest_rate() -> bool:
    print("interest_rate called.")
    return False

def mortgage_term() -> bool:
    print("mortgage_term called.")
    return False

def amortization_period() -> bool:
    print("amortization_period called.")
    return True

flags_and_callers = {'home_price': False,
                     'down_payment': False,
                     'interest_rate': False,
                     'mortgage_term': False,
                     'amortization_period': False}

# Set all flags according to simulated tests
print("Set all flags (simulated tests)")

for function, flag in flags_and_callers.items():
	return_value = eval(function + '()')
	flags_and_callers[function] = return_value
	

# Show all flags and callers.
print("\nResults of flags being set:")
for flag in flags_and_callers.values():
	print(flag)

print("\nSee if all flags are True:")
# see if any flags are set to False
for flag in flags_and_callers.values():
	print(flag, end = '')
	
	if flag == False:
		print(" Oops!")
		break
	elif flag == True:
		print(" Fine so far...")
