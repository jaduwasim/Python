'''program to merge characters of 2 string into a single string by taking charcters alternativly
input: s1='ravi'
	   s2='teja'
output: rtaevjia
'''
print(__doc__)
print()

s1 = input('Enter first string:')
s2 = input('Enter Second string:')
output =''
i,j=0,0
while i<len(s1) or j<len(s2):
	if i<len(s1):
		output = output+s1[i]
		i += 1
	if j<len(s2):
		output = output+s2[j]
		j+=1
print(output)