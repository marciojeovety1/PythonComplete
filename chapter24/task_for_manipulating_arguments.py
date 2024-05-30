def merge_lists_to_dict(*args):
    first_list = ['Name', 'Age']
    second_list = ['Marcio', 22]
    zip_var = zip(first_list, second_list)
    dict_var = dict(zip_var)
    return dict_var


my_list = []
other_list = []

res = merge_lists_to_dict(my_list, other_list)
print(res)
