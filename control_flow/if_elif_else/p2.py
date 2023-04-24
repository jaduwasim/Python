'''write a program to find Biggest of given 3 Number from the command prompt: '''
print(__doc__)
print()
n1 = int(input('Enter First Number:'))
n2 = int(input('Enter Second Number:'))
n3 = int(input('Enter Third Number:'))

if n1 > n2 and n1 > n3:
	print('The Biggest Number is {}'.format(n1))
elif n2 > n1 and n2 >n3:
	print('The Biggest Number is {}'.format(n2))
else:
	print('The Biggest Number is {}'.format(n3))