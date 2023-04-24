'''Write a program to Accept some string from the keyword and display its characters by index wise
(Both Posetive and Negative index)'''
print(__doc__)

s = input('Enter Some String:')

index=0
for i in s:
	print('On Posetive index {} and Negative index {} Characters is {}'.format(index,index-len(s),i))
	index +=1