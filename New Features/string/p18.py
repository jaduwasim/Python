# Calling user define function from f-string 
def mymax(a,b):
	max = a if a>b else b
	return max
a = int(input('Enter a Number:',))
b = int(input('Enter b Number:'))
print(f'The maximum Number of {a} and {b} is {mymax(a,b)}')