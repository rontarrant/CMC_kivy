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

def sanity_one():
    print("sanity_one called.")
    return True

def sanity_two() -> bool:
    print("sanity_two called.")
    return False

def sanity_three() -> bool:
    print("sanity_three called.")
    return True

def sanity_four() -> bool:
    print("sanity_four called.")
    return False

flags_and_callers = {'one': {'pass': False, 'function': 'sanity_one'},
                     'two': {'pass': False, 'function': 'sanity_two'},
                     'three': {'pass': False, 'function': 'sanity_three'},
                     'four': {'pass': False, 'function': 'sanity_four'}}


for item in flags_and_callers:
	quit = False
	
	for key, value in flags_and_callers[item].items():
		if key == 'pass':
			flag = value
			to_update = key
		elif key == 'function':
			function = value
			return_value = eval(function+'()')
			flags_and_callers[item][to_update] = return_value
			
			if not return_value:
				quit = True
				break
	
	if quit:
		break

#pretty(flags_and_callers)
so_pretty = json.dumps(flags_and_callers, indent = 1)
print(so_pretty)
#pprint.pprint(flags_and_callers, compact = False)
