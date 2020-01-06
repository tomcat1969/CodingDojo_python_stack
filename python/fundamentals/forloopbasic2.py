# def biggie_size(list):
# 	for i in range(len(list)):
# 		if list[i] > 0:
# 			list[i] = "big"
# 	return list

# print(biggie_size([-1,3,5,-5]))			


# def count_positives(list):
# 	count = 0
# 	for i in range(len(list)):
# 		if list[i] > 0:
# 			count = count + 1
# 	list[len(list)-1] = count
# 	return list		

# print(count_positives([1,6,-4,-2,-7,-2]))	

# def sum_total(list):
# 	sum = 0
# 	for i in range(len(list)):
# 		sum = sum + list[i]
# 	return sum
# print(sum_total([1,2,3,4]))		

# def average(list):
# 	sum = 0
# 	for i in range(len(list)):
# 		sum = sum + list[i]
# 	return sum / len(list)
# print(average([1,2,3,4]))	

# def length(list):
# 	return len(list) 
# print(length([]))

# def minimum(list):
# 	if len(list) == 0:
# 		return False
# 	global_min = list[0]
# 	for i in range(len(list)):
# 		if list[i] < global_min:
# 			global_min = list[i]
# 	return global_min
# print(minimum([37,2,1,-9]))				


# def maximum(list):
# 	if len(list) == 0:
# 		return False
# 	global_max = list[0]
# 	for i in range(len(list)):
# 		if list[i] > global_max:
# 			global_max = list[i]
# 	return global_max
# print(maximum([37,2,1,-9]))				

# def ultimate_analysis(list):
# 	result = {}
# 	result['sumTotal'] = sum_total(list)
# 	result['average'] = average(list)
# 	result['minimum'] = minimum(list)
# 	result['maximum'] = maximum(list)
# 	result['length'] = length(list)
# 	return result
# print(ultimate_analysis([37,2,1,-9]))



def reverse_list(list):
	l = 0
	r = len(list) - 1
	while l < r:
		temp = list[l]
		list[l] = list[r]
		list[r] = temp	
		l = l + 1
		r = r - 1
	return list	
print(reverse_list([37,2,1,-9]))























