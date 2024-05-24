print(id(print))

my_name = 'Marcio'
print(id(my_name))

my_num = 777
print(id(my_num))

other_num = my_num
print(id(other_num))

print(id(my_num) == id(other_num))