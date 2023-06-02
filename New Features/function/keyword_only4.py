'''def f1 (*,a=10,b=20)'''
def f1 (*,a=10,b=20):
	print(a,b)
f1() #Valid
f1(a=30) #Valid
f1(a=30,b=40) #Valid
f1(30,40) #TypeError: f1() takes 0 positional arguments but 2 were given