'''
String formatting means inserting values and expression in string
3 types of techniques
1. %-formatting
2. str.format
3. f-strings
-----------------------
1. %-formatting:
----------------
It is the oldest way of string formatting.
It is available from begginning of the python

%i ---> signed int value
%d ---> signed int value
%f ---> float value
%s ---> string value
'''
# eg-1: Single Variable
name = 'Durga'
s = 'Hello %s, Good Evening' %(name)
s1 = 'Hello %s, Good Evening' %name
print(s)
print(s1)
