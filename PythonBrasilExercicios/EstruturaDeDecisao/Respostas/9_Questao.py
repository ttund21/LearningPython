# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

num = []

for i in range(3):
    addNum = int(input(f'Add o {i + 1}º número: '))
    num.append(addNum)

num.sort(reverse=True)
for i in range(len(num)):
    print(f'{i + 1}º: { num[i] }')
