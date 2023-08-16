# Input a3b5
# Ouput aaabbbbb

s = input('Enter String:')
ouput = ''
ouput2 = ''
for x in s:
	if x.isalpha():
		ouput = ouput+x
		ouput2 = ouput2+x
		target = x
	else:
		ouput = ouput + target*(int(x)-1)
		ouput2 = ouput2 + chr(ord(target)+ int(x))
print(ouput)
print(ouput2)
