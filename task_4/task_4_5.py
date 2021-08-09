from functools import reduce


def product_numbers(element, next_element):
    return element * next_element


print(reduce(product_numbers, [i for i in range(99, 1001) if i % 2 == 0]))
