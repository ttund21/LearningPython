# 10. Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

unidade = {1:'Um', 2:'Dois', 3:'Três', 4:'Quatro', 5:'Cinco', 6:'Seis', 7:'Sete', 8:'Oito', 9:'Nove', 10:'Dez',
        11:'Onze', 12:'Doze', 13:'Treze',14:'Quatorze', 15:'Quinze', 16:'Dezesseis', 17:'Dezessete', 18:'Dezoito', 19:'Dezenove'}
dezena = {20:'Vinte', 30:'Trinta', 40:'Quarenta', 50:'Cinquenta', 60:'Sessenta', 70:'Setenta' ,80:'Oitenta', 90:'Noventa'}

while True:
    try:
        num = int(input('Número(1 - 99): '))
        if num < 1 or num > 99:
            print('Valor Inválido!')
            continue
        else:
            break
    except ValueError:
        print('Valor Inválido!')
        continue


dez = (num // 10) * 10
uni = num - dez

if dez != 0 and uni == 0:
    print(f'{dezena[num]}')
elif dez != 0 and uni != 0 and dez not in unidade:
    print(f'{dezena[dez]}-{unidade[uni]}')
else:
    print(f'{unidade[num]}')


