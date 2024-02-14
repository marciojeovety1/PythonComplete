#dictionaries - a dictionary is a collection of key-value pairs.

my_dictionaries = {'name': 'Marcio', 'country': 'Angola'}
print(my_dictionaries)

#adding something to the dictionarie
my_dictionaries['car'] = 'Range Rover'
print(my_dictionaries)

#update
my_dictionaries.update({'list': ['this a list', 2024]})
print(my_dictionaries)

#edit
my_dictionaries['country'] = 'Portugal'
print(my_dictionaries)

my_dictionaries['car'] = 'Lamborghini'
print(my_dictionaries)


#delete

del my_dictionaries['list']
print(my_dictionaries)

del my_dictionaries['car']
print(my_dictionaries)


popped_dictionary = my_dictionaries.pop('country')
print(popped_dictionary)
print(my_dictionaries)
print(popped_dictionary)

duplicated_dictionary = {'name': 'Marcio', 'name': 'Feuniria'}
print(duplicated_dictionary)
print(type(my_dictionaries))
print(len(my_dictionaries))
print(my_dictionaries)