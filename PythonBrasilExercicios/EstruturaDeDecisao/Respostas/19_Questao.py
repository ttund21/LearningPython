# 19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#   326 = 3 centenas, 2 dezenas e 6 unidades
#   12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = int(input('Número: '))

if num > 0 and num < 1000:
    cent = num // 100
    dez = (-(cent * 100) + num) // 10
    uni = (-(cent * 100) + num) - (dez * 10)
    print(f'{ cent } centena(s), { dez } dezena(s) e { uni } unidade(s).')
else:
    print('Número Inválido!')

