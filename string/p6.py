'''Program to Reverse Internal Content of each word
Example:
input : Durga Software Solutions
output : agruD erawtfoS snoituloS
'''
print(__doc__)
print()

s = input('Enter a Sentance:')
l1 = s.split()
l2 = []
i = 0
print('This is using from while loop:')
while i<len(l1):
	l2.append(l1[i][::-1])
	i=i+1
	output = ' '.join(l2)
print(output)
print('*'*40)
print('This is using from for loop:')

l3=[]
y=0
for ch in range(len(l1)):
	l3.append(l1[y][::-1])
	y+=1
	output=' '.join(l3)
print(output)