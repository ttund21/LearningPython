"""questao46
46. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
  Atleta: Rodrigo Curvêllo

  Primeiro Salto: 6.5 m
  Segundo Salto: 6.1 m
  Terceiro Salto: 6.2 m
  Quarto Salto: 5.4 m
  Quinto Salto: 5.3 m

  Melhor salto:  6.5 m
  Pior salto: 5.3 m
  Média dos demais saltos: 5.9 m

  Resultado final:
  Rodrigo Curvêllo: 5.9 m
"""

def resultado(registro, atleta):
    nome = registro[atleta]['nome']
    distancia = sorted(registro[atleta]['distancia'])
    print(f"\nAtleta: {nome}\n")
    for i in range(5):
        print(f"{ i + 1 }º Salto: { registro[atleta]['distancia'][i] } m ")
    print(f'''\nMelhor Salto: { max(distancia)  } m
Pior Salto: {min(distancia)} m
Média dos demais saltos: { round(sum(distancia[1:4]) / (len(distancia) - 2), 2) } m''')
    print(f'''\nResultado Final:
{nome}: { round(sum(distancia[1:4]) / (len(distancia) - 2), 2) } m''')



registro = {}
atleta = 0

while True:
    atleta += 1
    nome = input('\nNome: ')
    if nome == '':
        break
    else:
        registro.setdefault(atleta, {'nome':nome})
    for i in range(5):
        while True:
            try:
                salto = float(input('Distancia: '))
                break
            except ValueError:
                print('Valor Inválido!')
                continue
        if 'distancia' not in registro[atleta].keys():
            registro[atleta].setdefault('distancia',[salto])
        else:
            registro[atleta]['distancia'].append(salto)

    resultado(registro, atleta)



