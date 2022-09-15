#!/usr/bin/python3
""" 1-my_list Module """


class MyList(list):
	""" Class that extends `list` """
	def print_sorted(self):
		""" Print list in ascending order """
		print(sorted(self))
