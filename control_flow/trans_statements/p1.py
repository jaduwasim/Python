'''Break:
we can use break statement inside loops to break loop execution based on some conditon'''
print(__doc__)

for i in range(0,10):
	if i == 7:
		print('processing is enough, please break')
		break
	print(i)
