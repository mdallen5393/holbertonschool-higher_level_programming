#!/usr/bin/python3
def safe_print_division(a, b):
	try:
		return a / b
	except ValueError:
		print("Cannot Divide by 0")
	finally:
		print("Inside result: {}".format(a / b))
