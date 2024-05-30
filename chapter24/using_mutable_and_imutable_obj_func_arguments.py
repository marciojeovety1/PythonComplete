def print_fruits_info(person_name, fruits):
    fruits.pop()
    for fruit in fruits:
        print(f'{person_name} likes {fruit}')



my_name = 'Marcio'
favorite_fruits = ['oranges', 'apples', 'bananas']

print_fruits_info(my_name, favorite_fruits)

print(favorite_fruits)