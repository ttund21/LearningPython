# 15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

# F = F1.ultimo + F2.penultimo

nesimo = int(input('N-ésimo: '))
f1 = 1
f2 = 1 

for i in range(0, nesimo):
    f = f1 + f2 
    f2 = f1 # penultimo igual ultimo
    f1 = f # ultimo igual a ultima resposta
    print(f, end=' ')
