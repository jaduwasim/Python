'''To overcome some of %-formatting probles, to provide more 
options to the programmer we shuold go for str.format() method'''
'''
string formatting by using str.format() method:
-----------------------------------------------
It is introduced in python 2.6 version
It is advanced version of %-formatting technique.
It is very easy and provides several options tha %-formatting technique
'''
# eg-1: Single Variable
name = 'Durga'
s = 'Hello {}, Good Evening'.format(name)
print(s)
print('Hello {}, Good Evening'.format(name))