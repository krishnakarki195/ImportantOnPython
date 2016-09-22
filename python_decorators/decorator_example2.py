'''
crated by Krishna Karki decorator example

'''

def decorator_function(original_function):
	def wrapper_function():
		print("Wrapper execute before {}".format(original_function.__name__))
		return original_function()
	return wrapper_function


@decorator_function
def display():
	print("Display function ran.")

my_variable = display()
my_variable