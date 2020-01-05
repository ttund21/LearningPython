# 37. Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.

codigo = []
altura = []
peso = []

while True:
    try:
        cod = int(input('Codigo: '))
        if cod == 0:
            break
        alt = float(input('Altura: '))
        pes = float(input('Peso: '))
    except ValueError:
        print('Valor Inválido!')
        continue
    # Entrada para lista
    codigo.append(cod)
    altura.append(alt)
    peso.append(pes)

print(f'\nCliente mais alto\nCódigo: { codigo[altura.index(max(altura))] }\nAltura: { max(altura) } m\nPeso: { peso[altura.index(max(altura))] } Kg')
print(f'\nCliente mais baixo\nCódigo: { codigo[altura.index(min(altura))] }\nAltura: { min(altura) } m\nPeso: { peso[altura.index(min(altura))] } Kg')
print(f'\nCliente mais gordo\nCódigo: { codigo[peso.index(max(peso))] }\nAltura: { altura[peso.index(max(peso))] } m\nPeso: { max(peso) } Kg')
print(f'\nCliente mais magro\nCódigo: { codigo[peso.index(min(peso))] }\nAltura: { altura[peso.index(min(peso))] } m\nPeso: { min(peso) } Kg')
print(f'\nMedia de altura: { round(sum(altura) / len(altura), 2) } m')
print(f'Media de peso: { round(sum(peso) / len(peso), 2) } Kg')


