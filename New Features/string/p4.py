'''
problems with %-formatting:
---------------------------
2. To process data from the dictionary is complex
3. performance wise not upto the mark
'''
student={
	'name':'Aradhya',
	'father_name':'Abhisek',
	'mother_name':'Aishwarya',
	'grand_father':'Big B',
	'subject':'python'
}

s = 'Hello %s, You are luckiest girl as you have %s,%s, and %s is your family, you can learn %s very easily' %(student['name'],student['father_name'],student['mother_name'],student['grand_father'],student['subject'])
print(s)