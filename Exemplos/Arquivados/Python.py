"""
from random import randint as rand

lista = list()

def populate(x):
    n = 0
    while (n := n + 1) <= x:
        lista.append(rand(1, 100))

def listmax(lista):
    numero = int()
    maxi = int()
    for n in lista:
        numero = n
        if numero > maxi:
            maxi = numero
            
    return maxi
    
def listmin(lista):
    numero = int()
    mini = listmax(lista)
    for n in lista:
        numero = n
        if mini > numero:
            mini = numero          
            
    return mini
    
def listar(lista):
    for n in lista:
        print(n, end=" ")
        


populate(50)
print("Lista:", end=" ")
listar = listar(lista)
print(f"\nMax: {listmax(lista)}\nMin: {listmin(lista)}")
"""

"""
def division(x, y):
    return x / y
 
try: # Tratamento de erro
    print(division(int(input("X: ")) , int(input("Y: "))))

except ZeroDivisionError: # Se dar esse erro vai executar esse bloco
    print("Zero é o caraio")

except ValueError:
    print("Botando a porra do valor errada ai caraio")
    
finally: # Garante que sempre execute esse bloco
    raise ZeroDivisionError # Levanta um erro
 """
 
"""
def namevalidator(name):
    nameList = [str(0), str(1), str(2), str(3), str(4), str(5), str(6), str(7), str(8), str(9)]
    
    for i in name:
        if i not in nameList:
            continue
        else:
            raise NameError("Não pode numero! ")
            
namevalidator(input("Nome: "))
"""

"""
def namevalidator(name):
    nameList = [str(0), str(1), str(2), str(3), str(4), str(5), str(6), str(7), str(8), str(9)]
    
    for i in name:
        assert i not in nameList, "Não pode numero" # Ele checa uma condiçao e se for False ele é executado.
            
namevalidator(input("Nome: "))
"""

"""
# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")
"""

"""
file = open("Example.txt", "r")
print(read := file.read(3))
file.close()
"""

"""
arquivo = open("Example.txt", "r")
ler = arquivo.readlines() # Transforma cada linha do arquivo em um item da lista
print(ler) 
arquivo.close()
"""

"""
arquivo = open("Example.txt", "r")

for i in arquivo:
    print(f"- {i}")

arquivo.close()
"""

"""
with open("Texto.txt", "r") as arquivo: # Com o WITH não precisa fechar o arquivo, pois ele garante o fechamento do arquivo e simplifica o codigo, pois não usa o try e finally
    texto = arquivo.read()

try:
    arquivo = open("Example.txt", "w")
    teste = arquivo.write(texto) # Vai registrar na variavel teste o numero de bytes escritos
    print(f"Bytes: {teste}")
finally:
    arquivo.close()

with open("Example.txt", "r") as arquivo:
    msg = arquivo.read()
    linhas = arquivo.readlines
    print(f"Msg: {msg}\nLen: {len(msg)}")
"""

"""
assert 2 + 2 == 5 # Testa a linha se False, gerará um AssertionError
"""

"""
def linhas(arq):
    return len(arq.readlines())

def peso(arq):
    return arq.read()

with open(s := input("Caminho: "), "r") as arq:
    if (pergunta := input("Mostrar conteudo [y/n] \n")) == "y" or pergunta == "Y":
        print(f"Conteudo: {peso(arq)}")

with open(s , "r") as arq:
    print(f"Tamanho: {len(peso(arq))} bytes")

with open(s , "r") as arq:
    print(f"Linhas: {linhas(arq)} linhas")
"""

"""
with open("Example.txt", "r") as arq:
    print(f"{arq.read().splitlines()}") # Transforma tambem em lista mas diferente do readlines(), o splitlines() remove o \n
"""

"""
with open("Example.txt", "a") as arq: # Adiciona 10 linhas a um arquivo já populado
    for i in range(10):
        arq.write(f"\n{i + 1})New Line")
"""

"""
dic = {"Int":[0,1,2,3,4], 
"Float":5.0, 
"Boo":False}

dic["Casa"] = "Azul"
print("Int" in dic)
print(5.0 in dic)
print(dic.get("Int"))
print(dic.get(5.0))
"""
"""
# 7. Elabore um algoritmo que preencha uma matriz 4 X 4 de inteiros e depois faça:
# Imprimir toda a matriz. X
# Trocar a segunda linha pela terceira.
# Trocar a primeira pela quarta coluna.
# Imprimir novamente a matriz

from random import randint as rand

def matrizgen():
    matriz = {}
    index = ("a", "b", "c", "d") # tupla

    for i in index:
        for j in range(4):
            matriz[i + str(j + 1)] = rand(0, 100)

    return matriz

def matrizmud(matriz):
    index = ["b", "c"]
    reserva = None

    for i in index:
        for j in range(4):
            reserva = matriz[index[0] + str(j +1)]
            matriz[index[0] + str(j + 1)] = matriz[index[1] + str(j + 1)]
            matriz[index[1] + str(j + 1)] = reserva

    return print(matriz)

matriz = matrizgen()

while (opc := None) != 0:
    try:
        opc = int(input("0 - Sair\n1 - Exibir\n2 - B->C\n>>> "))
        if opc == 0:
            break
        elif opc == 1:
            print(matriz)
        elif opc == 2:
            matrizmud(matriz)
        else:
            print("Opção Inválida!")

    except ValueError:
        print("Opção Inválida!")
        continue
"""

"""
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista[:5])
print(lista[1:])
print(lista[0:5])
print(lista[1::2])
print(lista[::-1])
"""

"""
# Criar uma lista com multiplos de 9
# Criar lista só com pares
# Criar lista só com impares

def listanov():
    lista = [i * 9 for i in range(11)]

    return lista

def listapar():
    lista = [i for i in range(11) if i % 2 == 0 and i != 0]

    return lista

def listaimpar():
    lista = [i for i in range(11) if i % 2 != 0]

    return lista

print(f"Lista Nove: {listanov()}\nLista Par: {listapar()}\nLista Impar: {listaimpar()}")
"""

"""
# Pedir uma palavra e mostrar ela inversa

def reversor(palavra):
    revert = palavra[::-1]

    return revert

word = input("Palavra: ")
print(f"Revertida: {reversor(word)}")
"""

"""
print("{0}{1}{0}".format("abra", "cad"))
"""

"""
# Gera uma lista e sepera o resultado por -

from random import randint as r

def sep():
    lista = [str(i) for i in range(r(0,100))]

    return print(" - ".join(lista)) # Junta a lista em uma só string

sep()
"""

"""
# Separa as palavras de um arquivo em uma lista
# Transformar a palavras do arquivo em Uppercase
# Transformar a palavras do arquivo em Lowercase
# Substituir a palavra personagem por PERSONAGEM
# Testa se começa com NPC e termina com .

def sep(arq):
    return arq.split(" ")

def upper(arq):
    return arq.upper()

def lower(arq):
    return arq.lower()

def pers(arq):
    return arq.replace("personagem", "personagem".upper())

def begend(arq):
    if arq.startswith("NPC") and arq.endswith("."):
        return "Começa com NPC e termina com ."

with open("Example.txt", "r") as arq:
    arquivo = arq.read()

print(f"Lista: {sep(arquivo)}\n\nMaiusculo: {upper(arquivo)}\n\nMinusculo: {lower(arquivo)}\n\nSubstituição: {pers(arquivo)}\n\nTeste: {begend(arquivo)}")
"""

"""
# Descobre o maior numero da lista
# Descobre o menor numero da lista
# Testa quanto o primeiro item da lista falta pra chegar em 0
# Soma total da lista

from random import randint as r

lista = [i * r(1, 100) for i in range(1, 11)]

print(f"Lista: {lista}\nMax: {max(lista)}\nMin: {min(lista)}\nTeste: {abs(lista[0])}\nSoma: {sum(lista)}")
"""

"""
# Testa se todos os números da lista são maiores que 5
# Testa sem tem números pares
# Enumera itens da lista

from random import randint as r

lista = [i * r(1, 100) for i in range(1, 11)]

print(lista)

if all([i > 5 for i in lista]):
    print("Todos os números da lista é maior que 5.")

if any([i % 2 == 0 for i in lista]):
    print("Contém número(s) par(es)") 

for i in enumerate(lista):
    print(i)
"""

"""
# Given a text as input, find and output the longest word.
def contador(txt):
    txtList = txt.split(" ")
    registro = ""

    for word in txtList:
        if len(word) > len(registro):
            registro = word
        else:
            continue
    return registro



txt = input()
print(contador(txt))
"""

"""
lista = [1,1,1,2,3,4,5,6]

porcentagem = lambda a: (a * 100) / len(lista) # lambda cria pequenas funções, antes dos ":" vc cria os argumentos da função, na função normal seria def f(arg):

print(str(porcentagem(lista[0])) + "%")
"""

"""
def funcao(a, b):
    return a * b

lista1 = [i for i in range(1, 11)]
lista2 = [i for i in range(10, 0, -1)]


o = map(lambda a , b: a * b , lista1, lista2) # map faz a interação de uma função em um valor com multiplos itens, tipo lista, tupla e dict
p = map(funcao, lista2 , lista1) # lista2 e lista1 são argumentos da função
q = list(filter(lambda x: x%2 == 0, lista1)) # filter, filtra cada item de acordo com uma condição

print(list(o))
print(list(p))
print(q)
"""

"""
# Crie uma lista com 10 números aleatorios e exiba;
# Multiplique todos os items por 5 e exiba;
# Crie um lista apenas com os numeros pares dos items multiplicados e exiba.

from random import randint as r

lista = [ r(1, 100) for i in range(2, 12)]
mult = list(map(lambda x : x * 5, lista))
pares = list(filter(lambda x : x % 2 == 0, mult))

print(f"Lista com 10 numeros: {lista}\nLista multiplicada por 5: {mult}\nPares dos multiplicados: {pares}")
"""

"""
# Crie uma função que gera 10 pares

def contagem():
    for i in range(1, 1):
        if i % 2 == 0:
            yield i # diferente do return ele retorna uma sequencia de valores.


for i in contagem():
    print(i)
"""

"""
def decor(func):
    def teste():
        print("--------------")
        func()
        print("--------------")
    return teste

@decor
def frase():
    print ("Hello World!")

a = frase
print(a())
"""

"""
# Fazer um programa que imprima uma borda ao em cima e em baixo do resultado
# e deixe o resultado miausculo.

def formatador(funcao):
    def wrap(word):
        print("+--------------+")
        print(funcao(word).upper())
        print("+--------------+")
    return wrap

@formatador
def palavra(word):
    return word

t = input("Palavra: ")
palavra(t)
"""

"""
# Um exemplo de recursividade

def factorial(x): 
    print(x)
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))
"""

"""
def is_even(x): # Vamo dizer que x é tres 
    if x % 2 == 0: # A condição vai ser False pula pro else
        return True
    else:
        return is_odd(x - 1) # ele vai acionar a função is_odd com 3 - 1 entao vai ficar is_odd(2) 

def is_odd(x): # is_odd vai jogar o valor dois pro is_even e o mesmo vai retornar True
    return not is_even(x) # entao vai ficar "return not True" e retornara False

print(is_odd(2))
print(is_even(3))
"""

"""
# Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

def fibonacci(pos):
    if pos <= 1: # Essa condição será usada, pois os primeiros valores do fibonacci são previsiveis 0 e o 1
        return pos 

    else: # Aqui sera executada a lógica do fibonacci, ex: 5 é o resultado 3 + 2, os dois numeros anteriores
        return  fibonacci(pos - 1) + fibonacci(pos - 2) # de 5

num = 6 # Resultado 8

for i in range(num + 1):
    print(fibonacci(i), end = " ")

# fibonacci(6) -> fibonacci(5) + fibonacci(4) -> 5 + 3 = 8
# fibonacci(5) -> fibonacci(4) + fibonacci(3) -> 3 + 2 = 5
# fibonacci(4) -> fibonacci(3) + fibonacci(2) -> 2 + 1 = 3
# fibonacci(3) -> fibonacci(2) + fibonacci(1) -> 1 + 1 = 2  --> 0, 1, 1, 2, 3, 5, 8
# fibonacci(2) -> fibonacci(1) + fibonacci(0) -> 1 + 0 = 1
# fibonacci(1)                 =                         1  
# fibonacci(0)                 =                         0
"""

"""
def cont(x):

    if x == 0:
        return 0

    else:       
        return cont(x - 1)

print(cont(4))
"""

"""
t = {1,2,3,4,5}

t.add(1) # Adiciona o 1, mas o tipo set() não aceita valores repetidos
t.remove(4) # Remove 4
t.pop() # Remove um número arbitrario
print(len(t))
print(t)
"""

"""
t = {1, 3, 5, 6}
p = {2, 4, 6, 8}

print(t | p) # Combina dois conjuntos para formar um novo contendo itens em qualquer um;
print(p & t) # Obtem valores iguais nos dois sets;
print(p - t) # Remove os iguais do segundo no primeiro;
print(t ^ p) # Remove os iguais e adiciona os diferentes em um novo set.
"""

"""
import itertools

#for i in itertools.count(3): # Conta de 3 ao infinito
#    print(i)

#for i in itertools.repeat(5): # Repete 5 infinita vezes
#    print(i)

#for i in itertools.cycle(range(1, 4)): # Faz um ciclo de 1 a 3 infinita vezes
#    print(i)

# print(list(itertools.accumulate(range(6)))) # Vai somando item por item aumentado na ordem

l = ["A", "B"]

print(list(itertools.product(l, range(2)))) # [('A', 0), ('A', 1), ('B', 0), ('B', 1)]
print(list(itertools.permutations(l))) # [('A', 'B'), ('B', 'A')]
"""

"""
def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
		
print(power(2, 3))
"""

"""
class Cat:
    catSound = "Miau!"
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("preto", 4)
popo = Cat("branco",3)

print(f"{felix.color} {felix.catSound}")
"""

"""
class Car:
    roda = 4
    def __init__(self, nome, marca, velocMax, portas, cor):
        self.nome = nome
        self.marca = marca
        self.velocMax = velocMax
        self.portas = portas
        self.cor = cor

def decor(funcao):
    def wrap(arg):
        cabec = 9
        final = 23
        print("+" + "-" * cabec + arg.nome +"-" * cabec + "+")
        print(funcao(arg))
        print("+" + final * "-" + "+" + "\n")
    return wrap


uno = Car("Uno", "Fiat", "532", "2", "branco")
fusca = Car("Fusca", "Wolskvagen", "150", "2", "azul")
vitrine = (uno, fusca)

@decor
def loja(carro):
    return f"Marca: {carro.marca}\nVelocidade Máxima: {carro.velocMax}\nPortas: {carro.portas}\nCor: {carro.cor}"

for carro in vitrine:
    loja(carro)
"""

"""
class Animal:
    sound = "Mal!"
    def __init__(self, name, legs, color):
        self.name = name
        self.legs = legs
        self.color = color


class Dog(Animal): # Cria uma herança da classe Animal na classe Dog
    sound = "Roof!"

class Cat(Dog): # Pode-se criar heranças de sub classes tb
    pass

ralf = Dog("Ralf", 4, "Branco")
chico = Cat("Chico", 4, "Cinza")

print(f"{ralf.name}, {ralf.sound}")
print(f"{chico.name}, {chico.sound}")
"""

"""
class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam() # Super Classe

B().spam()
"""

"""
class Teste:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Teste(self.x + other.x, self.y + other.y)

primeiro = Teste(2, 4)
segundo = Teste(6, 8)

resultado = primeiro + segundo

print(resultado.x, resultado.y)
"""

"""
class Pessoa:
    def __init__(self, name, kilos, age):
        self.name = name
        self.kilos = kilos
        self.age = age

    def __add__(self, other):
        return Pessoa(self.kilos + other.kilos, self.age + other.age)

jao = Pessoa("Jao", 55, 23)
chico = Pessoa("Chico", 60, 24)

resultado = jao + chico

print(resultado.kilos, resultado.age)
"""

"""
from re import A

a = 42

print(a)

del a # Destroi a instacia

print(a)
"""

"""
class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def correr(self):
        print("Correndo")

    def entregar_cpf(self):
        return self.__cpf


class Blits(Pessoa):
    def __init__(self, numPoliciais):
        self.numPoliciais = numPoliciais

chico = Pessoa("Chico", 21, "555.887.965-26")
blits = Blits(4)

print(f"/""{chico.nome}, voltando para casa é parado por uma blits;
Blits era composta por {blits.numPoliciais} policiais;
{chico.nome} entregou seus documentos e falou sua idade, - Tenho {chico.idade};
Policial checa seu cpf e pede para ele falar seu cpf, - Meu cpf é {chico.entregar_cpf()};
Então {chico.nome} continuou seu caminho para casa...""/")
"""

"""
# Diferença entre usar um underscore vs em usar dois underscore

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self._cpf = cpf # Na var _cpf é usado 1 underscore mais como um acordo de que essa variavel
# tem que ser privada, ou seja, não deve ser acessada fora da classe;


class People:
    def __init__(self, name, id):
        self.name = name
        self.__id = id # Já na var __id é usado 2 underscore e isso faz com que a var seja PRIVADA e nenhum
# código externo tenha acesso.

joao = Pessoa("João", "111.111.111-11")
john = People("John", "222.222.222-22")

print(joao._cpf)
print(john.__id)
"""

"""
class People:
    def __init__(self, nome):
        self.nome = nome

    def __documentos(self): # Um metodo sinalizado como privado so pode ser usado dentro da classe
        cpf = 555
        return cpf

class Exibir(People):
    def exibir_documentos(self):
        exCpf = self.__documentos
        return exCpf


chico = People("Chico")
ex = Exibir("teste")
print(ex.exCpf)
"""

