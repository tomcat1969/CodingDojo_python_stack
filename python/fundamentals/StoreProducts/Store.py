from Product import Product
class Store:
	def __init__(self,name,product_list=[]):
		self.store_name = name
		self.product_list = product_list
	def add_product(self,new_product):
		self.product_list.append(new_product)
	def sell_product(self,id):
		p = self.product_list.pop(id)
		print(f"{p.product_name} is sold!")
	def inflation(self,percent_increase):
		for i in product_list:
			i.update_price(percent_increase,True)
	def set_clearance(self,category,percent_discount):
		for i in product_list:
			if i.category == category:
				i.update_price(percent_discount,False)
myStore = Store("A1 gun shop")
m1911 = Product("M1911",1200,"pistal")
m1911.print_info()
m16 = Product("M16",700,"rifle")
m16.print_info()
m16.update_price(5,False)
m16.print_info()
myStore.add_product(m1911)	
myStore.add_product(m16)
for i in myStore.product_list:
	print(i.product_name)
myStore.sell_product(1)
for i in myStore.product_list:
	print(i.product_name)



			
		
