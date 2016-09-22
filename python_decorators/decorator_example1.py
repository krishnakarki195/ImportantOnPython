'''
crated by Krishna Karki decorator example

'''

def decorator_function(original_function):
	def wrapper_function():
		print("Wrapper execute before {}".format(original_function.__name__))
		return original_function()
	return wrapper_function


def display():
	print("Display function ran.")

my_variable = decorator_function(display)
my_variable()

