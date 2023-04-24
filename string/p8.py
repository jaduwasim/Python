'''write a program to print characters at odd postiion and Even Position fot the given string
 2nd way:'''
print(__doc__)
s=input('Enter some string:')
i=0
print('characters at Even postiion:')
while i< len(s):
	print(s[i],end=',')
	i+=2
print('characters at odd postiion:')
i=1
while i<len(s):
	print(s[i],end=',')
	i+=2
