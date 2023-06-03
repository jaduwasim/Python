'''
By using str.format() technique, we can use dictionary very easily
'''
student = {
	'name':'Aradhya',
	'father_name':'Abhishek',
	'mother_name':'Aiswarya',
	'grand_frather':'Big B',
	'subject':'Python'
}
s = 'Hello {name}, you are the luckiest girl as you have {father_name}, {mother_name} and {grand_frather}, you can learn {subject} very easily'.format(**student)
print(s)