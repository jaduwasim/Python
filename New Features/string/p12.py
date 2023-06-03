'''
timeit module:
--------------
By using timeit module, we can mesure execution time of small coding snippets.
'''

import timeit
# If we print
t = timeit.timeit("print('Hello')", number =100000)
# if we dont want to print only execution 
t2 = timeit.timeit("'Hello'", number =100000)

print(f'The time taken {t} seconds')

# for Limit the Number after Decimal

print(f'The time taken {t:.2f} seconds')
