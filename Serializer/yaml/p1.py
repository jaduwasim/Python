'''
object Serialization with yaml:
-------------------------------
YAML : 
------
a retronym for Yaml Ain't Markup Language that meant originally Yet Another Markup
language

it is alternative to JSON
it is also light weight and Human Understandable form.
it it more readable than JSON.

To Serialize and deserialize out python data to yaml,
we have to go for pyaml library.
This library bydefault not available and we have to install separately.

pip install pyaml

pyml library contains yaml module:
----------------------------------
yaml module conatins the following function to perform serializa:
-----------------------------------------------------------------
For Serialization:
1. dump() ---> To serialize dict object to yaml string or yaml file
'''

from pyaml import yaml
emp_data ={
	'eno' : 100,
	'ename' : 'Sunny',
	'esal' : 1000,
	'eaddr' : 'Mumbai'
}
# Serializing to yaml string
yaml_string = yaml.dump(emp_data)
print(f'Yaml Stirng Data: \n{yaml_string}')

# Serializing to yaml file
with open('emp.yaml', 'w') as f:
	yaml.dump(emp_data, f)

print('emp_data is saved in emp.yaml file')

print('Desrialization:')
python_dict = yaml.safe_load(yaml_string)
print(python_dict)