my_bike = {
    'brand': 'Custom',
    'price': 2000
}


other_bike = {
    'price': 3000,
    'brand': 'Custom',
    'max_speed': 50
}


print(my_bike)
print(type(my_bike))
print(len(my_bike))

print(my_bike['brand'])
print(my_bike['price'])
print(id(my_bike))

my_bike['max_speed'] = 50
print(my_bike)
print(id(my_bike))

my_bike['price'] = 3000
print(my_bike)


print(my_bike == other_bike)