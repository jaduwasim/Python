'''
eg-2: Multiple variables
'''
name = 'Durga'
salary = 10000
gf = 'Sunny'
s = 'Hello {}, Your Salary is {}, and Your Girl freind {}, is waiting'.format(name,salary,gf)
print(s)
s2 = 'Hello {2}, Your Salary is {1}, and Your Girl freind {0}, is waiting'.format(gf,salary,name)
s3 = 'Hello {n}, Your Salary is {s}, and Your Girl freind {g}, is waiting'.format(g=gf,s=salary,n=name)
print(s2)
print(s3)
