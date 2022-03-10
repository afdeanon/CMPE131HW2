def sort_list(list):
	n = len(list)
	i = 0
	while (i < n):
		j = i+1
		while (j<n):
			if(list[i] > list[j]):
				temp = list[j]
				list[j] = list[i]
				list[i] = temp
			j = j+1
		i = i+1
	return list
