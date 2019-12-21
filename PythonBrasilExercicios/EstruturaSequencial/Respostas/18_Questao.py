# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

print('Calculadora de velocidade de download')
tamArq = float(input('Tamanho do arquivo(MB): '))
velLink = float(input('Velocidade da Internet(Mbps): '))
print(f'O tempo de download vai ser de: { round(((tamArq * 8) / velLink) / 60 , 2) } minutos')
