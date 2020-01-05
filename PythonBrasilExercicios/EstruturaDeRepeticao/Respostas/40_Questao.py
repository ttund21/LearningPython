# 40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#   Código da cidade;
#   Número de veículos de passeio (em 1999);
#   Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#   Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#   Qual a média de veículos nas cinco cidades juntas;
#   Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

codigo = []
numVeic = []
acidentes = []
lowVeic = []
media = 0

for i in range(5):
    while True:
        try:
            cod = int(input('Códogo da Cidade: '))
            num = int(input('Número de veículos de passeio: '))
            aci = int(input('Número de acidentes de trânsito: '))
            break
        except ValueError:
            print('Valor Inválido!')
            continue

    codigo.append(cod)
    numVeic.append(num)
    acidentes.append(aci)
    if num < 2000:
        lowVeic.append(acidentes[i])

for i in lowVeic:
    media += i

print('\nAcidentes')
print(f'Maior índice de trânsito\nCidade: { codigo[acidentes.index(max(acidentes))] }, Número de acidentes: { max(acidentes) }')
print(f'\nMenor índice de trânsito\nCidade: { codigo[acidentes.index(min(acidentes))] }, Número de acidentes: { min(acidentes) }')

print(f'\nMédia de veiculos: { sum(numVeic) / len(numVeic) }')

print(f'\nMédia de acidentes em cidades com menos de dois mil veiculos:  { media / len(lowVeic) }')
