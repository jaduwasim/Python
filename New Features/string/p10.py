# Eg-2: Multiple Variable
name = 'Durga'
salary = 100000
gf = 'Sunny Leone'

# 1. %-formatting Way:
s1 = 'Hello %s, your salary is %s, your girl freind %s is waiting' %(name,salary,gf)
print(s1)

# 2. str.fromat() Mehtod:
s2 = 'Hello {}, your salary is {}, your girl freind {} is waiting'.format(name,salary,gf)
print(s2)

# 3. f-staring Techinique which introduced in 3.6
s3 = f'Hello {name}, your salary is {salary}, your girl freind {gf} is waiting'
print(s3)