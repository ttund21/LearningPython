# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

while True:
    paisA = float(input('População país A: '))
    taxA = float(input('Taxa de crescimento país A: '))
    paisB = float(input('População país B: '))
    taxB = float(input('Taxa de crescimento país B: '))
    i = 0

    while paisA <= paisB:
        i+= 1
        paisA += (paisA * taxA)/100
        paisB += (paisB * taxB)/100

    print(f'Ano: {i}, População A: {round(paisA, 2)}, População B: {round(paisB, 2)}')
    repetir = input('\nQuer repetir?\n>>> ')
    if repetir == 's':
        continue
    else:
        break


