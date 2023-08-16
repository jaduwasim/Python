'''
Write a python Script to take a digit 1 to Hundred and give roman Number 
'''
print(f'Question: {__doc__}')

n = int(input('Enter Number:'))
units = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X'}
ten_digt = {20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',100:'C'}
hundred_digt = {150:'CL',200:'CC',250:'CL',300:'CCC',350:'CCCL',400:'CD',450:'CDL',500:'D',550:'DL',600:'DC',650:'DCL',700:'DCC',750:'DCCL',800:'DCCC',850:'DCCCL',900:'CM',950:'CML',1000:'MC'}
tens = {2:'XX',3:'XX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC',10:'C'}

if n in units:
	print(units[n]) 
elif n in ten_digt:
	print(ten_digt[n])
elif n in hundred_digt:
	print(hundred_digt[n])

elif n not in units:
	unitdigit = n%10
	tendigit = n//10
	print(tens[tendigit] + units[unitdigit])
# else:
# 	hundred= n%100
# 	hundred_unit = n//100
# 	unitdigit = n%10
# 	tendigit = n//10
# 	print(hundred_digt[unitdigit] + ten_digt[unitdigit] + tens[hundred] + units[hundred_unit])
