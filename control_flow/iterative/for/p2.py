'''To Print Charcters present in string index wise'''
print(__doc__)
s = input('Enter A String:')

i = 0
for ch in s:
	print('On The index of {} is {}'.format(i,ch))
	i=i+1