def traverse_list(my_list):
    print("List elements:")
    for item in my_list:
        print(item)


def traverse_tuple(my_tuple):
    print("Tuple elements:")
    for item in my_tuple:
        print(item)


# List
numbers = [10, 20, 30, 40, 50]

# Tuple
values = (1, 2, 3, 4, 5)

# Passing list and tuple to functions
traverse_list(numbers)
traverse_tuple(values)