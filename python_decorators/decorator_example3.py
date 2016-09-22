'''
crated by Krishna Karki decorator example

'''

def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print("Wrapper execute before {}".format(original_function.__name__))
		return original_function(*args, **kwargs)
	return wrapper_function

@decorator_function
def display():
	print("Display function ran.")

@decorator_function
def display_info(name, age):
	print("Display info ran with the argument {} {}").format(name,age)

my_variable = decorator_function(display)
my_variable()

display_info("John", 20)

