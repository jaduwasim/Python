'''To Dispaly The sum of first Number:'''
print(__doc__)

num = int(input('Enter a Number:'))
i = 1
sum = 0
while i <= num:
	sum = sum + i
	i+=1

print('The sum of first {} is {}'.format(num, sum))