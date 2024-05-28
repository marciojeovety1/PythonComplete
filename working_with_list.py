my_nums = [10, 3, 100, 35]
other_nums = [351, 245, 425]

merged_nums = my_nums + other_nums

print(my_nums)
print(type(my_nums))
print(isinstance(my_nums, list))
print(id(my_nums))

print(my_nums[0], my_nums[-1], my_nums[2])

print(my_nums)
print(id(my_nums))
#my_nums.append(50)
print(id(my_nums))
print(my_nums)

print(my_nums)
print(len(my_nums))
my_nums.pop(2)
print(my_nums)
print(len(my_nums))


my_nums.extend([34, 62])
print(my_nums)


print(my_nums.index(34))

my_nums.clear()
print(my_nums)


my_nums.append(50)
print(my_nums)


print(merged_nums)