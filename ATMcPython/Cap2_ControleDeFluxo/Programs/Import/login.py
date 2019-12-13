from sys import exit

luser = ''
lpass = ''
user= 'admin'
passwd = 'admin'

while True:
    chance = 6

    print('WeLcOmE tO My FiRsT pRoGrAm!\n')
    print('1 - Create Account\n2 - Sign In\n3 - Exit')
    resp = input('>>> ')

    if resp == '1':
        print('\nWelcome to account creator. Now put your username and password.')
        user = input('Username: ')
        passwd = input('Password: ')

    elif resp == '2':
        print('Sign In')
        for i in range(6):       
            luser = input('\nUsername: ')
            lpass = input('Password: ')
            chance = chance - 1 
            if luser == user and lpass == passwd:
                print('\nAccess Granted!\n\n\n')
                break
            elif chance == 0:
                print('\nAccount Blocked!\n\n\n')
            else:
                print('\nYour login attempt failed;\nVerify that the username and password are correct;\nAttempts to block: ' + str(chance) + '.')
                continue

    elif resp == '3': 
        exit('System terminated.')

    else:
        print('Wrong Cammand.\n\n\n')
