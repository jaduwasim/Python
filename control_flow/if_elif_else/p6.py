def roman_number(number):
	if number == 0 or number > 3999:
		print('Please Enter Number, Which is greater then Zero and Less then or equal 3999!')
		roman_number(int(input('Enter Number Again:')))

	value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
	symbol = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
	roman = ''
	i=0
	while number>0:
		div = number // value[i]
		number = number % value[i]
		while div:
			roman = roman + symbol[i]
			div = div - 1
		i=i+1
	return roman
number = int(input('Enter Number:'))
print(f'The Roman symbol of {number} is {roman_number(number)}')