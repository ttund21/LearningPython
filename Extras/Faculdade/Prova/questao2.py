def notaAbaixo(notas):
    reg = []
    for i in notas:
        if i < 7:
            reg.append(str(i))
    print(f"\nNotas Abaixo de 7: {' ,'.join(reg)}")

def parImpar(notas):
    impar = []
    par = []
    for i in notas:
        if i%2 == 0:
            par.append(str(i))
        else:
            impar.append(str(i))
    print(f"\nNotas Pares: {' ,'.join(par)}")
    print(f"Notas Impares: {' ,'.join(impar)}")


regNotas = []

while True:
    try:
        notas = float(input('Nota: '))
    except ValueError:
        continue
    if notas == 0:
        break
    else:
        regNotas.append(notas)

notaAbaixo(regNotas)
parImpar(regNotas)
print(f"\nMédia de notas: {sum(regNotas)/len(regNotas)}")
