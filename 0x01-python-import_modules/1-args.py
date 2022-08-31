#!/usr/bin/python3
from sys import argv


def print_args():
	numArgs = len(argv)
	if numArgs == 0:
		print("0 arguments.")
	elif numArgs == 1:
		print("1 argument:")
	else:
		print("{} arguments:".format(numArgs))
	for arg in 

