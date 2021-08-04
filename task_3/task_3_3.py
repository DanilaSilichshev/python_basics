def my_func(first_num, second_num, third_num):
    num_array = [first_num, second_num, third_num]
    num_array.remove(min(num_array))
    return sum(num_array)


my_func(7, 9, 5)
