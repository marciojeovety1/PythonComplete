#conditionals - are set of rules that someone can implement to their code
#example
#if and else, else if = elif

age = int(input('What\'s your age? '))

if age < 18:
    print('You\'re not allowed to enter to this event. Grow.')
    
elif age == 18:
    print(f'You are {age}, but we need your parent\'s document permission.')
    
elif age > 50:
    print(f"You are {age}, this event is not longer for your age.")

else:
    print(f'You are {age}, so you are welcome to this event.')
    
    
names = 'Feuniria'

if names != 'Feuniria':
    print(f'No you are not Feuniria, you are {names}, stop lying to me, I will bite you.')
    
else:
    print(f"Welcome {names}, Python loves you so much.")