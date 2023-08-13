'''
yaml module conatins the following function to perform deserializa:
-------------------------------------------------------------------
2. load():
----------
load() is deprecated and we have to use safe_load() functions
'''

from pyaml import yaml

with open('emp.yaml', 'r') as f:
	python_dict = yaml.safe_load(f)

print(python_dict)