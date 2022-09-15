#!/usr/bin/python3
""" 0-lookup Module """


def lookup(obj):
	atts_and_mets = list(dir(obj))
	return atts_and_mets
