class Product:
	def __init__(self,product_name,product_price,category):
		self.product_name = product_name
		self.product_price = product_price
		self.category = category
	def update_price(self, percent_change, is_increased):
		if is_increased == True:
			self.product_price += percent_change
		else:
			self.product_price -= percent_change
	def print_info(self):
		print(f"name of the product : {self.product_name}")
		print(f"category : {self.category}")
		print(f"price of the product : {self.product_price}")

			
	