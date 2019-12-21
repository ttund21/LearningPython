# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.

num = []

for i in range(3):
    addNum = int(input(f'Add o {i + 1}º número: '))
    num.append(addNum)

print(f'O maior número é: { max(num) }')
print(f'O menor número é: { min(num) }')

