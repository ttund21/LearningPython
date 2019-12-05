print("Hello, what's your name?")
name = input()
print('\nHow old are you?')
age = int(input())

if name == 'Alice' and age > 12:
    print('\nHello, Alice.')
elif age < 12:
    print('\n' + name +', U are only ' + str(age) + ', get out kiddo!')
else:
    print('\nHey ' + name + ', you not supposed to be here,'  + ' get out!')
