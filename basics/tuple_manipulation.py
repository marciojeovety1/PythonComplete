screen_res = (1920, 1080)
screen_info = (True, 'Samsung', 150)
print(screen_res)
print(type(screen_res))
print(isinstance(screen_res, tuple))

print(screen_res.index(1080))

print(screen_res.count(1080))

screen_res_list = list(screen_res)

screen_res_list[0] = 1444
print(screen_res_list)

screen_res = tuple(screen_res_list)
print(screen_res)

screen_data = screen_res + screen_info
print(screen_data)
print(len(screen_data))