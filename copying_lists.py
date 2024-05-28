my_list = [10, 'abc', True]
copy_of_my_list = my_list.copy()

copy_of_my_list.append(None)
print(my_list)
print(copy_of_my_list)
print(id(my_list) == id(copy_of_my_list))