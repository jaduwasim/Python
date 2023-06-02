'''
positional only arguments:
--------------------------
We should pass values by positonal only arguments.
/ ---> Forward Slash
All parameters before /, will become positional only parameters.
Introduced in Python 3.8 Version as the Part PEP 570
'''
def f(a,b,/):
	print(a,b)
f(10,20) #Valid
f(10,b=20) #TypeError: f() got some positional-only arguments passed as keyword arguments: 'b'
