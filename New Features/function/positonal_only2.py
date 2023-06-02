'''
f1(a,b,/,c,d,*e,f)
Here
----
a and b Should be Positional only Parameters, We can not take any other.
c and d can be Positional or Keywords Parameters
e and f should be keyword only Parameters.
f1(val1,val2, val3,val4, e=val5, f=val6) or
f1(val1,val2, c=val3,d=val4, e=val5, f=val6) or
f1(val1,val2, val3,d=val4, e=val5, f=val6) or


'''
def f1(a,b,/,c,d,*,e,f):
	print(a,b,c,d,e,f)

# f1(10,20,c=30,40,e=50, f=60) SyntaxError: positional argument follows keyword argument