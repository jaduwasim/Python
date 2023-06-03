'''
f-string taken less execution time as compare to %-formatting and str.format()
'''

import timeit 

t =  timeit.timeit('''
name ='Durga'
salary=10000
gf='Sunny'
s='Hello %s, Your Salary is %d,Your Girl Friend %s is waiting'%(name,salary,gf)
''', number=10000)

print(f'%-formatting taken time {t:.2f} Seconds')

t =  timeit.timeit('''
name ='Durga'
salary=10000
gf='Sunny'
s='Hello {}, Your Salary is {},Your Girl Friend {} is waiting'.format(name,salary,gf)
''', number=10000)
print(f'str.foramt() taken time {t:.2f} Seconds')

t =  timeit.timeit('''
name ='Durga'
salary=10000
gf='Sunny'
s=f'Hello {name}, Your Salary is {salary},Your Girl Friend {gf} is waiting'
''', number=10000)
print(f'f-strings taken time {t:.2f} Seconds')