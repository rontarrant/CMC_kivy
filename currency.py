## format currency for printing on the command line or
## in a TextInput
import locale


def format_currency(number: float):
	## set up
	locale.setlocale(locale.LC_ALL, 'English_Canada.1252')
	##format_string = locale.format_string()
	conv = locale.localeconv()
	
	
	return(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], number), grouping = True))
