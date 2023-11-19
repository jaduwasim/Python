'''
To check given number is either prime or not
'''
def check_Prime_Number(num):
	if num > 1:
		for i in range(2, num):
			if num%i == 0:
				print(f'{num} is not Prime Number...')
				break
		else:
			print(f'{num} is a prime Number')

	else:
		print(f'Prime number should be greater then One')

print('Provide Number to check either Prime Number or Not')
check_Prime_Number(int(input('Enter a Number:')))