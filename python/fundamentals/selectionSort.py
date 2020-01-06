def selectionSort(list):
	if len(list) == 0:
		return list
	
	for i in range(len(list)):
		global_min = 999
		index_min = 0
		for j in range(i ,len(list)):
			if list[j] < global_min:
				global_min = list[j]
				index_min = j
		list[i],list[index_min] = list[index_min],list[i]
	return list

list = [64, 25, 12, 22, 11]
print(selectionSort(list))				