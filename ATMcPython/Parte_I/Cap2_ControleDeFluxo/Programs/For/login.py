luser = ''
lpass = ''
chance = 6 
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
for i in range(6):       
    luser = input('\nUsername: ')
    lpass = input('Password: ')
    chance = chance - 1 
    if luser == user and lpass == passwd:
        print('\nAccess Granted!')
        break
    if chance == 0:
        print('\nAccount Blocked!')
    else:
        print('\nYour login attempt failed;\nVerify that the username and password are correct;\nAttempts to block: ' + str(chance) + '.')
        continue

