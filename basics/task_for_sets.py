my_set = {1, 2, 3, 4, 5}
other_sets = {8, 7, 10, 5}

my_set.add(7)
print(my_set)


new_set = set()
print(type(new_set))

print(my_set)
print(other_sets)

new_set = my_set & other_sets
print(type(new_set))
print(new_set)

new_list = list(new_set)
print(new_list)