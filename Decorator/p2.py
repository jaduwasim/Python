# How to call same function with Decorator and without Decorator
# we should not use @decor
def decor(fun):
	def innner(name):
		if name == 'sunny':
			print(f'Hello {name} Very Very Good Morning, You are my favorite guest!!!')
		else:
			fun(name)

	return innner

def wish(name):
	print(f'Hello {name}, Good Morning')

decoratorfuction = decor(wish)

wish('Durga') #Decorator won't be executed
wish('sunny') #Decorator won't be executed

decoratorfuction('Durga') #Decorator will be executed
decoratorfuction('sunny') #Decorator will be executed