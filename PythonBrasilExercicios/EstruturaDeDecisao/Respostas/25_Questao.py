# 25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#   "Telefonou para a vítima?"
#   "Esteve no local do crime?"
#   "Mora perto da vítima?"
#   "Devia para a vítima?"
#   "Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

susp = 0

while True:
    questao1 = input('Telefonou para a vítima? s ou n\n>>> ')
    if questao1 == 's' or questao1 == 'n':
         if questao1 == 's':
             susp += 1
         break
    else:
        print('Comando Invalido')


while True:
    questao2 = input('Esteve no local do crime? s ou n\n>>> ')
    if questao2 == 's' or questao2 == 'n':
         if questao2 == 's':
             susp += 1
         break
    else:
        print('Comando Invalido')

while True:
    questao3 = input('Mora perto da vítima? s ou n\n>>> ')
    if questao3 == 's' or questao3 == 'n':
         if questao3 == 's':
             susp += 1
         break
    else:
        print('Comando Invalido')

while True:
    questao4 = input('Devia para a vítima? s ou n\n>>> ')
    if questao4 == 's' or questao4 == 'n':
         if questao4 == 's':
             susp += 1
         break
    else:
        print('Comando Invalido')

while True:
    questao5 = input('Já trabalhou com a vítima? s ou n\n>>> ')
    if questao5 == 's' or questao5 == 'n':
         if questao5 == 's':
             susp += 1
         break
    else:
        print('Comando Invalido')

if susp == 0:
    print('Inocente')
elif susp <= 2:
    print('Suspeita')
elif susp <= 4:
    print('Cúmplice')
else:
    print('Assassino')
