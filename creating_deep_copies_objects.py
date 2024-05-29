from copy import deepcopy

info = {
    'name': 'Marcio',
    'is_instructor': True,
    'reviews': []
}


info_deepcopy = deepcopy(info)

print(info_deepcopy)

info_deepcopy['reviews'].append('Great course!')

print(info)
print(info_deepcopy)
