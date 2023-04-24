'''To print sum of numbers present inside list'''
print(__doc__)
ls = eval(input('Enter list:'))
sum = 0

for i in ls:
	sum = sum + i
print('Sum of list:',sum)
