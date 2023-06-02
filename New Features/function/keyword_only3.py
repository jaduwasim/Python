'''
what about def f1(a,/,*,b,c)
Here  a shuold be Postional Arguments
But b and c should be keyword arguments
'''

def f1(a,/,*,b,c):
	print(a,b,c)
f1(10,b=20,c=30) #in this program this case is valid other all cases are invalid.