# 22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

def divi(num):
    div = []
    for i in range(2, num + 1):
        if num % i == 0:
            div.append(i)
    return print(f'Divisivel por: {div}')



num = int(input('Número: '))

for i in range(2, num + 1):
    if num == 2 or i == num:
        print('Primo!')
        break
    elif num % i == 0:
        print('Não Primo!')
        divi(num)
        break


