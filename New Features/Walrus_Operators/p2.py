'''
Heroines = []
Heroine = input('Enter Your Favorite Heroine Name:')

while Heroine != 'done':
	Heroines.append(Heroine)
	Heroine = input('Enter Yor Favorite Heroine Name:')

print(Heroines)
'''

Heroines = []
while (Heroine := input('Enter Your Favorite Heroine Name:')) != 'done':
	Heroines.append(Heroine)
print(Heroines)