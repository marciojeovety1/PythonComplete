a = {'a', 'c', 'd'}
b = {'l', 'm', 'c'}

print(a.symmetric_difference(b))

print((a | b) - (a & b))