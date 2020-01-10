def frase(lista):
    frase = ''
    for i in range(len(lista)):
        if i == (len(lista) - 2):
            frase += lista[i]
        elif i < (len(lista) - 2):
            frase += lista[i] + ', '
        else:
            frase += ' and ' + lista[i]
    
    return frase

lista = []

while True:
    addList = input('Palavra: ')
    if addList == '':
        break
    else:
        lista.append(addList)

print(lista)

show = frase(lista)
print(show)
