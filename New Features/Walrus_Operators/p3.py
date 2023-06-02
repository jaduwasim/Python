'''
read data line by line fro abc.txt file and print to the console
'''
'''
Without Walrus operator:
f = open('abc.txt')
line = f.readline()
while line !='':
	print(line, end='')
	line = f.readline()
f.close()
'''

# With Walrus operator
f = open('abc.txt')
while (line:=f.readline()) !='':
	print(line, end='')
f.close()