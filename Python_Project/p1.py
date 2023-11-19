'''
Write a program to list out all prime number between two given Number
'''

def prime_number(lower, upper):
	print('The list of Prime Number:')
	for num in range(lower, upper+1):
		if num > 1:
			for i in range(2,num):
				if num%i == 0:
					break
			else:
				print(num, end=',')
		else:
			print('one is not prime number')

lower = int(input('Etner Lower Number:'))
upper = int(input('Enter upper Number:'))
prime_number(lower, upper)
