my_bike = {
    'brand': 'Custom',
    'price': 2000
}

print(my_bike.keys())

print(my_bike.items())

other_bike = my_bike.copy()

other_bike['color'] = 'red'
print(my_bike)
print(other_bike)