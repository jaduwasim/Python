def python():
	print()
	print('\t\t\t------------------------------')
	print('\t\t\t Welcome to The Python World')
	print('\t\t\t------------------------------')
	print('\t\t\t   Author The Washim Akram')
	print('\t\t\t'+'-'*30)
	print()


def EnglishNumber():
	n=int(input('Enter First Number from 1 to 100 only otherwise you get an KeyError:'))
	units = {0:'Zero', 1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',
	11:'Eleven',12:'Tweleve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen',20:'Twenty',100:'OneHundred'}
	tens={2:'Twenty', 3:'Thirty', 4:'Fourty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninty'}

	if n in units:
		print(units[n])

	elif n not in units:
		unitdigit=n%10
		tendigit=n//10
		output = tens[tendigit]+' '+units[unitdigit]
		print(output)
EnglishNumber()