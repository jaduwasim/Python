'''
what about def f1(a,*,b,c)
Here we can take a as Postional and keyword Arguments
But b and c should be keyword arguments
'''
def f1(a,*,b,c):
	print(a,b,c)

# case-1
f1(10,b=20,c=30) #Valid
# f1(10,20,30) #TypeError: f1() takes 1 positional argument but 3 were given
# f1(10,20,c=30) #TypeError: f1() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given
# f1(a=10,a=20,c=30) #SyntaxError: keyword argument repeated: a
f1(a=10,b=20,c=30) #Valid