#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
	for val in sorted(a_dictionary):
		print(val, ': ', a_dictionary[val], sep='')
