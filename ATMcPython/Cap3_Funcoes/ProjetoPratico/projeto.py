def collatz(number):
    if number%2 == 0:
        return ( number / 2 )
    else:
        return ( 3 * number + 1 )

resp = input('Enter number:\n')

while resp != 1:
    try:
        resp = collatz(int(resp))
    except ValueError:
        print('\nValue Error\n')
        resp = input('Enter number:\n')
        continue
    print(int(resp))
