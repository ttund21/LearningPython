# 39. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

numero = []
altura = []

for i in range(10):
    print(f'\n{i + 1}º Conjunto:')
    while True:
        try:
            num = int(input('Número: '))
            alt = float(input('Altura: '))
            break
        except ValueError:
            print('Valor Inválido!')
            continue
    numero.append(num)
    altura.append(alt)
    
print(f'\nAluno mais alto\nNúmero: { numero[altura.index(max(altura))] }\nAltura: { max(altura) } m')
print(f'\nAluno mais baixo\nNúmero: { numero[altura.index(min(altura))] }\nAltura: { min(altura) } m')
