db_is_available = False

print(db_is_available)
print(type(db_is_available))
print(isinstance(db_is_available, bool))

db_is_available = True
print(db_is_available)

print(bool(10))#True
print(bool(0))#False
print(bool(0.0))#True
print(bool('abc'))#True
print(bool(''))#False

print(100 > 50)
print(100 == 50)

print([1, 2, 3] == [1, 2, 3, 4])
print([1, 2, 3] == [1, 2, 3])

is_available = True
print(not is_available)

my_name = 'Marcio'

if is_available and my_name:
    print('Is available')