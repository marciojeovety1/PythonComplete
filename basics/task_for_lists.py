my_list = [1, 2, 3, 4 , 5]

del my_list[2]
print(my_list)

print(len(my_list))

my_list.reverse()
print(my_list)

second_list = [6, 7]

third_element = [8, 9]

my_list.extend(third_element)
print(my_list)