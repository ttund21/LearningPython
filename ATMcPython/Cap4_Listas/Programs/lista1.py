name = []
cname = None 
i = 0 

print('Welcome to the list system!')
print('Register the names, if u want stop just hit the enter.')

while True:
    i = i + 1
    cname = input(str(i) + 'º Name: ')
    if cname == '':
        break
    else:
        name = name + [cname]

for i in range(len(name)):
    print(f'{i + 1}º Registed Names: {name[i]}')
