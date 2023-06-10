def Samrt_Div(fun):
	def  inner(a,b):
		print(f'We are Dividing {a} with {b}')
		if b == 0:
			print('Oops!, We cant Divide by Zero')
		else:
			fun(a,b)
	return inner

@Samrt_Div
def Divide(a,b):
	return a/b

Divide(5,0)