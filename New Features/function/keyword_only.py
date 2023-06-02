'''
After *, All parameters will become keyword only parameters
At the time of calling we should pass values by keyword only
introduced in python 3.0 version only
'''

def f(*,a,b):
	print(a,b)

f(a=20,b=20) #Valid
# f(20,30) #TypeError: f() takes 0 positional arguments but 2 were given
# f(20, b=20) #TypeError: f() takes 0 positional arguments but 1 positional argument (and 1 keyword-only argument) were given
# f(a=10, 20) SyntaxError: positional argument follows keyword argument