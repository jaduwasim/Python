# Calling user define function from f-string 
def mymax(a,b,c):
	max = a if a>b and a>c else b if b>a and b>c else c
	return max
a = int(input('Enter First Number:'))
b = int(input('Enter Second Number:'))
c = int(input('Enter Third Number:'))
print(f'The greatest number of {a}, {b} and {c} is {mymax(a,b,c)}')