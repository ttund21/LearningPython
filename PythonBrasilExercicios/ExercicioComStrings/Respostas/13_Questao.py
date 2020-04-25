# 13. Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

from random import shuffle, randint
from sys import exit

def shufWord(word):
    listWord = list(word)
    shuffleWord = shuffle(listWord)
    return ''.join(listWord)


words = ['palavra', 'trator', 'casa', 'carro', 'cair', 'chuva', 'docker', 'kubernetes', 'amigo']
word = words[randint(0, len(words) - 1)]

print("Jogo da Palavra Embaralhada")
print(f"Tente acertar que palavra é essa: {shufWord(word)}, você terá 6 tentativas.")

for i in range(6):
    attempt = input(f"{i + 1}ª Tentativa: ")
    if attempt == word:
        print("Venceu!")
        exit()
    else:
        print('"Erouu" - Faustão')

print("Você Perdeu!")
