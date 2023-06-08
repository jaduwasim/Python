'''
Deserialization:
----------------
2.load():
----------
Reading json from a file and converting to pythoon dict object. 
It Deserialiazation form json file
'''

from json import load

with open('emp.json','r') as f:
	employe = load(f)
print('Employee Infromation:')
print('Employee Name :',employe['name'])
print('Employee Age :',employe['age'])
print('Employee Salary :',employe['salary'])
print('Is Employee Married:',employe['isMarried'])
print('Is Employee Having GF :',employe['isHavingGF'])

for k,v in employe.items():
	print(f'{k}:{v}')