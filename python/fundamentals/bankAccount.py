class BankAccount:
	def __init__(self,interest_rate,balance=0):
		self.balance = balance
		self.interest_rate = interest_rate

	def deposit(self,amount):
		self.balance = self.balance + amount

	def withdraw(self,amount):
		if self.balance < amount:
			print("Insufficient funds:Charging $5 fee")
			self.balance = self.balance - 5	
		else:
			self.balance = self.balance - amount

	def display_account_info(self):
		print(f"Balance : ${self.balance}")

	def yield_interest(self):
		if self.balance > 0:
			self.balance = self.balance * (1 + self.interest_rate)				
			
c1 = BankAccount(0.03,100)
c1.withdraw(30)
c1.display_account_info()

c1.yield_interest()
c1.display_account_info()			