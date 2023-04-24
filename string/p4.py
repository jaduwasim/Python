'''write a program to Reverse the given String'''
print(__doc__)
print()
print('program using slice operator:')
s = input('Enter some string:')
print(s[::-1])

print()
print('program using reversed method:')
s = input('Enter some String again:')
print(''.join(reversed(s)))

print()
print('program using while loop:')
print()
s = input('Enter some string again:')
i = len(s)-1
target = ''
while i >= 0:
	target = target+s[i]
	i-=1
print(target)