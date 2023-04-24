'''To Check Type of characters present in a string'''
print(__doc__)

s = input('Enter a String:')

if s.isalnum():
	print('string is alpha numeric')
	if s.isalpha():
		print('String is alphabate characters')
		if s.islower():
			print('string in lower case')
		else:
			print('String in upper case')
	else:
		print('String is in digit format')
else:
	print('Empty String')
