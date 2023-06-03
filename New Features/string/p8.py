'''
problems with str.fromat() technique:
-------------------------------------
1. If number of variables are more still it is more verbose.
2. Performance wise not upto the mark
'''
name = 'Aradhya'
father_name = 'Abhishek'
mother_name = 'Aishwarya'
grand_father = 'Big B'
subject = 'Python'

s = 'Hello {n}, You are most luckiest girl as you have {f},{m} and {g} is your family, you can learn {s} very eaisy'.format(n=name, f=father_name,m=mother_name,g=grand_father,s=subject)
print(s)