my_comment = "This is my short comment"
print(my_comment)
print(len(my_comment))

my_comment = my_comment.replace('short', 'long')
print(my_comment)

print(my_comment.count('is'))

print(my_comment[2:7]) #is is

print(my_comment.find('long') == -1)

print(my_comment.split(' '))

print(my_comment.upper())

print(my_comment.lower())

print(dir(my_comment))