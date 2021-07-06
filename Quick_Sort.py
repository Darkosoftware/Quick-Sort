def quicksort(first):
	if len(first) <= 1:
		sorted_list = first
	else:
		pivot = first[0]
		
		larger = []
		smaller = []
		equal = []
		
		for item in first:
			if item > pivot:
				larger.append(item)
			elif item < pivot:
				smaller.append(item)
			else:
				equal.append(item)
		sorted_list = quicksort(smaller) + equal + quicksort(larger)
	return sorted_list

n = int(input("How many different numbers would you like to sort?: "))
sort_this_list = list(map(int,input("Enter the numbers here: ").strip().split()))[:n]

print(quicksort(sort_this_list))

input("Press enter to close.")
