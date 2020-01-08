"""47
47. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
  Atleta: Aparecido Parente

  Nota: 9.9
  Nota: 7.5
  Nota: 9.5
  Nota: 8.5
  Nota: 9.0
  Nota: 8.5
  Nota: 9.7

  Resultado final:
  Atleta: Aparecido Parente
  Melhor nota: 9.9
  Pior nota: 7.5
  Média: 9,04
"""

def resultado(registro, atleta):
    nome = registro[atleta]['nome']
    notas = sorted(registro[atleta]['notas'])
    print(f"\nAtleta: { nome }\n")
    for i in registro[atleta]['notas']:
        print(f'Nota: {i}')
    print(f'''\nResultado Final:
Atleta: { nome }
Melhor Nota: { max(notas) }
Pior nota: { min(notas) }
Média: { round( sum(notas[1:6]) / (len(notas) - 2), 2) }''')


registro = {}
atleta = 0

while True:
    atleta += 1
    nome = input('Nome: ')
    if nome == '':
        break
    else:
        registro.setdefault(atleta, {'nome':nome})
    for i in range(7):
        nota = float(input(f'{i + 1}ª Nota: '))
        if 'notas' not in registro[atleta].keys():
            registro[atleta].setdefault('notas', [nota])
        else:
            registro[atleta]['notas'].append(nota)
    
    resultado(registro, atleta)
