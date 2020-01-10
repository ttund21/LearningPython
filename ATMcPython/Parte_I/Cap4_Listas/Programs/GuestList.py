names = []

print('Enter your list names:\n')
while True:  
    rnames = input('>>> ')
    if rnames == '':
        break
    else:
        names += [rnames]

print('\nYour guest are:')
for i in range(len(names)):
    print(f'{i + 1}º Guest: {names[i]}')

print('\nThe name with the most letters in your list is:', max(names, key=len))
