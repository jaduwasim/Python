'''write a program to display *'s in pyramid style'''
n = int(input('Enter Number of Rows:'))
for i in range(1, n+1):
	print(' '*(n-i),end='')
	print('* '*i)