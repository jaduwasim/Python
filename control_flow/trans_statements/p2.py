'''Continue:
we can use continue statement to skip current iteration and continue next iteration
To print odd numbers in the range of 0 to 9 use continue statement '''

for i in range(0,10):
	if i%2 == 0:
		continue
	print(i)