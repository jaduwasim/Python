'''
problems with %-formatting:
---------------------------
1. If more number of variable are there, then it is more verbose and error prone
'''
name = 'Aradhya'
father_name = 'Abhishek'
mother_name = 'Aishwarya'
grand_father = 'Big B'
subject = 'python'

s = 'Hello %s, Your are most luckiest girl as you have %s, %s and %s family members, You can learn %s very easily' %(name, father_name, mother_name, grand_father,subject)
print(s)
