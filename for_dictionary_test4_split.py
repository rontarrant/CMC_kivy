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

def mortgage_principal() -> bool:
    print("mortgage_principal called.")
    return True

def interest_rate() -> bool:
    print("interest_rate called.")
    return True

def mortgage_term() -> bool:
    print("mortgage_term called.")
    return True

def amortization_period() -> bool:
    print("amortization_period called.")
    return True

all_good = True # assume everything's okay until it isn't

principal_flags = [{'check': 'home_price', 'flag': False},
					{'check': 'down_payment', 'flag': False},
                    {'check': 'mortgage_principal', 'flag': False}]

payment_flags = [{'check': 'interest_rate', 'flag': False},
				{'check': 'mortgage_term', 'flag': False},
				{'check': 'amortization_period', 'flag': False}]

# Set all flags according to simulated tests
print("Set flags (simulated tests)")

for item in principal_flags:
	return_value = eval(item['check'] + '()')
	item['flag'] = return_value
    
	if return_value == False:
		all_good = False
		break
	
if all_good:
	for item in payment_flags:
		return_value = eval(item['check'] + '()')
		item['flag'] = return_value
    
		if return_value == False:
			all_good = False
			break

if all_good:
	print("all flags are True")
else:
	print("found a fault")

# Show all flags and callers.
print("\nResults of flags being set:")
for flag in principal_flags:
	print(flag)

for flag in payment_flags:
	print(flag)
