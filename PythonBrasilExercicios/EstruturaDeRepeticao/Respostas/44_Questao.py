# 44. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
#  1 , 2, 3, 4  - Votos para os respectivos candidatos
#  (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#  5 - Voto Nulo
#  6 - Voto em Branco
#  Faça um programa que calcule e mostre:
#     O total de votos para cada candidato;
#     O total de votos nulos;
#     O total de votos em branco;
#     A percentagem de votos nulos sobre o total de votos;
#     A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

def exibir():
    print('Candidatos'.center(40, '-'))
    print('''1 - Meirelles
2 - Bolsonaro
3 - Amoedo
4 - Haddad
5 - Voto Nulo
6 - Voto em Branco''')
    print(''.center(40, '-'))

def porcentagem(eleitores, candidatos):
    print('Resultado'.center(60, '-'))
    for i in range(1, 7):
        print(f"{candidatos[i]['nome']} --> Total de Votos: { candidatos[i]['votos'] } , Porcentagem: { round((candidatos[i]['votos'] / eleitores) * 100, 2) } %")
    print(''.center(60, '-'))
    print(f"Total de Votos: {eleitores}")


candidatos = { 1:{ 'nome':'Meirelles', 'votos':0 }, 2:{ 'nome':'Bolsonaro', 'votos':0  }, 3:{ 'nome':'Amoedo', 'votos':0 }, 4:{ 'nome':'Haddad', 'votos':0 }, 
        5:{ 'nome':'Nulo', 'votos':0 }, 6:{ 'nome':'Branco', 'votos':0 } }
eleitores = 0


exibir()

while True:
    try:
        voto = int(input('Voto(0 para parar): '))
    except ValueError:
        print('Valor Inválido!')
        continue
    if voto == 0:
        break
    elif voto not in candidatos.keys():
        print('Valor Inválido!')
        continue
    else:
        eleitores += 1
        candidatos[voto]['votos'] += 1

porcentagem(eleitores, candidatos)
