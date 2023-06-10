def decor1(fun):
	def inner():
		x=fun()
		return x*x
	return inner

def decor2(fun):
	def inner():
		x=fun()
		return 2*x
	return inner

@decor1
@decor2
def num():
	return 10
print(num())