num_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
featured_list = [element for element in num_list if num_list.count(element) == 1]
print(featured_list)
