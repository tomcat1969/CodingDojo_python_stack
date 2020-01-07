class User:
	def __init__(self,name,email):
		self.name = name
		self.email = email
		self.account_balance = 0
	def make_withdrawal(self,amount):
	    self.account_balance = self.account_balance - amount

	def display_user_balance(self):
	    print(self.account_balance)

	def transfer_money(self,other_user,amount):
		self.account_balance = self.account_balance - amount
		other_user.account_balance = other_user.account_balance + amount

	def make_deposit(self, amount):
		self.account_balance = self.account_balance + amount
		return self


user1 = User("huanglin","tomcat1969@gmail.com")
# user1.account_balance = 100
user2 = User("Marry","Marry@163.com")
# user2.account_balance = 100
# print(f"{user1.name} has {user1.account_balance}")
# print(f"{user2.name} has {user2.account_balance}")
# user1.transfer_money(user2,20)
# print(f"{user1.name} has {user1.account_balance}")
# print(f"{user2.name} has {user2.account_balance}")
user1.make_deposit(100).make_deposit(190).display_user_balance()