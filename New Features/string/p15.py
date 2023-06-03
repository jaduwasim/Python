# Processing Dictionary data by f-string

student ={
	'name':'Aradhya',
	'father_name':'Abhishek',
	'mother_name':'Aishwarya',
	'grand_father':'Big B',
	'subject' : 'Python'
}

s = f"Hello {student['name']}, You are the most Luckiest girl as you have {student['father_name']},{student['mother_name']} and {student['grand_father']} as your family, you can learn {student['subject']} very easily"
print(s)