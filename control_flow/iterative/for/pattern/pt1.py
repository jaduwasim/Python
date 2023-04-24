'''write a program to display *'s in Right Angle Trianled form'''
print(__doc__)

n = int(input('Enter a Number of Rows:'))
for i in range(1,n+1):
	for j in range(1, i+1):
		print('* ', end='')
	print()