'''
1. The Walrus Operator:
-----------------------
:=
Python 3.8
This operator released as the part of PEP 572.
PEP-->Python Enhancement Proposals
To assign values to the variables as the part of expression itself.
Assignment Expressions
'''
'''
l = [10,20,30,40,50]
n = len(l)
if n > 3:
	print('List contains more than 3 elements:')
	print('The length of the List is:',n)

print(n)
'''
l = [10,20,30,40,50]
if (n := len(l)) > 3:
	print('List contains more than 3 elements:')
	print('The length of the List is:',n)

print(n)