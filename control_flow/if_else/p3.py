'''write a program to check whether the given number is in between 1 to 100:'''
print(__doc__)
print()

num = int(input('Enter A Number:'))
if num >=1 and num <=100:
	print(' The given Number {} is between 1 to 100'.format(num))
else:
	print('The given number {} is not between 1 to 100')