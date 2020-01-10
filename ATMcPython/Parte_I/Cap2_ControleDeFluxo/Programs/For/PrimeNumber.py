print('Welcome to prime number checker!\nWrite a number:')
primeNum = int(input('>>> '))

for i in range(2, primeNum + 1):
    rest = primeNum % i
    if rest == 0 and primeNum != i:
        print(f'{primeNum} is not a Prime Number!')
        break
    elif rest == 0 and primeNum == i:
        print(f'{primeNum} is a Prime Number!')
     
