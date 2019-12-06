luser = ''
lpass = ''
user= 'admin'
passwd = 'admin'

print('WeLcOmE\n')
print('If u want to create a new account, press 1. If not just hit enter.')
resp = input('>>> ')

if resp == '1':
   print('\nWelcome to account creator. Now put your username and password.')
   user = input('Username: ')
   passwd = input('Password: ')

print('Sign In')
while True:       
    luser = input('\nUsername: ')
    lpass = input('Password: ')
    if luser == user and lpass == passwd:
        print('\nACCESS GRANTED!!!!')
        break
    else:
        print('\nYour login attempt failed. Verify that the username and password are correct.')
        continue

