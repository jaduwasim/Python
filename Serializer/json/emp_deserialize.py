'''
Deserialization:
----------------
1. loads():
-----------
Converting json string to python dict.
It deserialize from json string

2.load():
----------
Reading json from a file and converting to pythoon dict object. 
It Deserialiazation form json file
'''
import json

json_string = '''
{
    "name": "Durga",
    "age": 35,
    "salary": 1000.0,
    "isMarried": true,
    "isHavingGF": null
}
'''

#Desrialization: Converting from json string object to python object
python_obj = json.loads(json_string)
print(python_obj)

# Deserialization : Converting from json file to python object
with open('emp.json','r') as f:
	employee = json.load(f)
	print(employee)