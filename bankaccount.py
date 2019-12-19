#bank account challenge
class Account:
	def __init__(self,owner,balance):
		self.owner=owner
		self.balance=balance
	def deposit(self,deposit_amount):
		self.balance=self.balance+deposit_amount
		print('New balance: ',self.balance)
	def withdraw(self,withdraw_amount):
		if withdraw_amount>self.balance:
			print("You don't have enough money in your account. Your balance: ",self.balance)
		else:
			self.balance = self.balance - withdraw_amount
			print('New Balance: ', self.balance)
		#may not exceed the available balance	
asd = Account('Oner',500)
asd.deposit(300)
asd.deposit(200)
asd.withdraw(1100)
asd.withdraw(500)
asd.withdraw(200)
