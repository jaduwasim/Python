from random import randint
from abc import ABC
import sys
import datetime
class Utils(ABC):
	history = []
	@staticmethod
	def generate_account_no():
		ano = ''
		for i in range(12):
			ano = ano + str(randint(0,9))
		return ano
	@classmethod
	def addEntry(cls, msg):
		Utils.history.append(msg)

	@staticmethod
	def createAccount(accountType):
		if accountType == 'Savings':
			name = input('Enter Your Name:')
		else:
			name = input('Etner Company Name:')
		balance = float(input('Enter Initial Balance:'))
		while balance < 0:
			balance = float(input('Initail Balance should not be Negative/Minus, Please enter valid value :'))
		if accountType == 'Savings':
			account = SavingAccount(name, balance)
			Utils.addEntry(f'{datetime.datetime.now()}- {accountType} Account Created with A/C No. {account.account_no} and Initial Balance {account.balance}')
		else:
			account = CurrentAccount(name, balance)
			Utils.addEntry(f'{datetime.datetime.now()}- {accountType} Account Created with A/C No. {account.account_no} and Initial Balance {account.balance}')
		print('-'*50)
		print(f'Congratulation, Your {accountType} Account Created Successfully')
		print('Account Details:')
		if accountType == 'Savings':
			print(f"Your Name is {account.name.strip().capitalize()} ")
		else:
			print(f"Your Company Name is {account.name.strip().capitalize()} ")
		print(f'Your Account No is {account.account_no}')
		return account

class Account:
	Bank_Name = 'Jadu World Bank'
	def __init__(self, name, balance, min_balance):
		self.account_no = Utils.generate_account_no()
		self.name = name
		self.balance = balance
		self.min_balance = min_balance

class SavingAccount(Account):
	def __init__(self, name, balance):
		super().__init__(name, balance, 0)

class CurrentAccount(Account):
	def __init__(self, name, balance):
		super().__init__(name, balance, -1000)

print()
print(f'Welcome to {Account.Bank_Name}')
print(f'--------------------------')
option1 = input('Do You Want to Open Saving or Current Account[Yes|No]:')
while option1.lower() not in ['yes','no',]:
	option1 = input('Please Input Valid Option[Yes|No]:').lower()
if option1.lower() == 'no':
	print('Thanks for Using Our Application')
	sys.exit()
else:
	print(f'Please Choose Option Which Account You Want to Open:')
	print(f's-Savings Account \nc-Current Account')
	option2 = input('Please Enter Your Option:')
	count = 1
	while option2.lower() not in ['s','c']:
		if count >= 3:
			print('Sorry, Max Number of Attempt reached, Try after some time')
			sys.exit()
		option2 = input('Please Select Valid Option:')
		count +=1
	if option2 == 's':
		account = Utils.createAccount('Savings')
		
	else:
		account =Utils.createAccount('Current')
	
print(Utils.history)



