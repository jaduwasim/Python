'''program to Reverse Order of words
input : Learning Python is very Easy 
output :Easy Very is Python Learning '''
print(__doc__)
print()

s = input('Enter some string:')
l1 = s.split()
l2 = []
i = len(l1)-1
while i >=0:
	l2.append(l1[i])
	i=i-1
	output = ' '.join(l2)
print(output)