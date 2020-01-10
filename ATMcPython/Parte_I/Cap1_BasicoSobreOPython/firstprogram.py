# Este programa diz hello e pergunta o meu nome.
print('Hello world!')# usado para exibir uma informação na tela.
print()
print('What is your name?') # pergunta o nome.
myName = input() # o input() vai receber uma string.
print('It is good to meet you, ' + myName)
print()
print('The length of your name is:' + ' ' + str(len(myName))) # a função 'len()' conta o número de caracteres de uma string, ela é considerada um valor inteiro.
print()
print('What is your age?') # pergunta a idade.
myAge = input()
print()
print('You will be ' + str(int(myAge) + 1) + ' in a year.') # str(int(myAge) + 1), vai pegar a variavel 'myAge' vai transformar em inteiro para somar com o 1 e depois vai voltar para string para concatenar com as outras strings.

# str(): transformara o valor recebido em string
# float(): transformara o valor recebido em float
# int(): transformara o valor recebido em inteiro, sempre que for usado em um valor do tipo float, irá arredonda-lo para baixo.
