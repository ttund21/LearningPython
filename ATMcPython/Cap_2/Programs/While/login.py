luser = ''
lpass = ''
user= 'teste'

print('WeLcOmE\n')
print('If u want to create a new account, press 1. If not just hit enter')
resp = input('>>> ')

if resp == '1':
   print('\nWelcome to account creator. Now put your username and password.')
   user = input('Username: ')
   passwd = input('Password: ')
else:
    print('Sign In')
    while True:       
        luser = input('Username: ')
        if luser != user:
            continue
        if luser == user:
            break
   
    

