'''
As the part of programming, it is very common required to convert from python object into
JSON object and from json form to python object. For these conversion (Serialization and deserialization)
python provide inbuilt module json

json module defie multiple functions fro serialization and deserialization

For Serializations purpose(from python to json form):
1. dumps():
-----------
its serializaes python dict object to json string

2. dump():
----------
converting python dict object to json and write that json data to provide json file 
its serialize to a file
'''

import json
employee ={
	'name':'Durga',
	'age':35,
	'salary':1000.0,
	'isMarried':True,
	'isHavingGF':None
}
# Serializtions with json string:
json_string = json.dumps(employee, indent=4)
print(json_string)

# Serialization with json file:
with open('emp.json','w') as f:
	json.dump(employee, f, indent=4)

print('Serialization Completed')
print('Data saved into emp.json file')