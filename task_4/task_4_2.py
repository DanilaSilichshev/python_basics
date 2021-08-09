num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
featured_list = [element for index, element in enumerate(num_list) if
                 num_list[index - 1] < num_list[index] and index != 0]
print(featured_list)
