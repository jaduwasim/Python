'''
Expression inside f-string:
---------------------------
We can pass expressions inside f-string and these expression will be evaluated at runtime
'''
a=10
b=20
c=30
print(f'The Result: {10*20/3}')
print(f'The Result: {10*20/3:.3f}')
print(f'The Result: {a+b*c}')