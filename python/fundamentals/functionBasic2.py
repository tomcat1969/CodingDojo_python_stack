def Countdown(a):
	newlist = []
	for i in range(a,-1,-1):
		newlist.append(i)
	return newlist	


print(Countdown(5))


def print_and_return(list):
	print(list[0])
	return list[1]

print(print_and_return([3,4]))	


def first_plus_length(list):
	return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))	


def values_greater_than_second(list):
	if len(list) < 2:
		return False
	newlist = []
	for i in range(0,len(list)-1):
		if list[i] > list[i+1]:
			newlist.append(list[i])

	newlist.append(list[len(list)-1])	
	print(len(newlist))
	return newlist	

print(values_greater_than_second([4,1,1,1,2]))

def length_and_value(size,value):
	newlist = []
	for i in range(size):
		newlist.append(value)
	return newlist
	
print(length_and_value(4,7))
