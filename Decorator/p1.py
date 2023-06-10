'''
Decorator:
----------
Decorator is a fucnction which take a function as arguments and exten ist functionaliy
and return modified function with extended functionality

The main objective of decorator fucntion is we can extend the functionality of existing
function wihtout modifies that function.
'''
def decor(fun):
	def inner(name):
		if name == 'sunny':
			print(f'Hello {name} Very Very Good Morning, You are my favorite guest!!!')
		else:
			fun(name)

	return inner

@decor
def wish(name):
	print(f'Hello {name} Good Morning')

name = input('Enter your name: ')
wish(name)