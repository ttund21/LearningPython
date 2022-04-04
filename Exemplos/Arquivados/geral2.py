# ------------------------------- Funções -------------------------------

"""
def numbers(*args): # O argumento "*args" passa um "infinito" número de argumentos.
    return args

print(numbers(1,2,3,4,5,6,7,8,9,10))
"""

"""
def func(*ala): # O que sinaliza um "argumento infinito" é o "*", pode-se escrever qualquer nome
    return ala  # para a variavel.

print(func(5,8,9,"Hop"))
"""

"""
def func(x, y, food="Banana"): # Pode-se definir um calor default a um argumento.
    return f"X: {x}, Y: {y}, Comida: {food}"

print(func(4, 5))
print(func(4, 5, "Arroz"))
"""

"""
def func(x,  y=7, z): # Argumentos com um valor padrão deve-se declarado por último, ou irá gerá um
    return x, y, z    # erro. Error: Non-default argument follows default argument

print(func(4, 6, 8))
"""

"""
def func(x, y=8, *arg, **kwarg): # O opereador "**" faz com que a variavel receba argumentos com
    return f"X: {x}, Y: {y}, *ARG: {arg}, **KWARG: {kwarg}" # chave e valor. Ex: var1="Variavel 1"

print(func(8, 3, "A", "B", "C", var1="Variavel 1", var2="Variavel 2")) # E retornará um dict
"""

# ------------------------------- Tuple Unpack -------------------------------

"""
numbers = (1, 2, 3) # A descompactação de tuplas permite que você atribua cada item em um iterável
a, b, c = numbers # (geralmente uma tupla) a uma variável.A descompactação de tuplas permite que você
# atribua cada item em um iterável (geralmente uma tupla) a uma variável. 

print(f"numbers: {numbers}, a: {a}, b: {b}, c: {c}")
"""

"""
lista = [i for i in range(1, 11)]
a, b, *c, d = lista # Uma variável que é precedida por um asterisco (*) recebe todos os valores do
# iterável que sobraram das outras variáveis.

print(f"lista: {lista}")
print(f"a: {a}, b: {b}, c: {c}, d: {d}")
"""

"""
a, b, *c, d = range(1, 11) 

print(f"a: {a}, b: {b}, c: {c}, d: {d}")
"""

# ------------------------------- Ternary Operator -------------------------------

"""
a = 5
b = 1 if a >= 5 else 42 # Pode se passar um if diretamente na variavel, mas não deve-se usar em
# excesso, pois atrapalha a legibilidade do código
print(b)
"""

"""
a = [i for i in range(1, 11)]
b = 1 if all([i > 11 for i in a]) else "Erro" # se todos os números da "var a" for maior que 11
# b = 1, se não b = "Erro"

print(b) # Output: Erro
"""

# ------------------------------- More on else Statements -------------------------------

"""
for i in range(10):
    if i < 20: # True
        break # Break executado

else: # O else no loop, só será executado se o loop for finalizado normalmente, ou seja, sem o break
    print("Break 1")

for i in range(10):
    if i > 20: # False
        break # Break não executado

else: 
    print("Break 2") # Output: Break 2
"""

"""
try: # O else no try é executado quando não houver nenhum erro;
    a = 5 / 0 # Erro

except ZeroDivisionError:
    print("Try 1: ZeroDivisionError")

else:
    print("Try 1: Else") # Não vai ser executado;

try:
    a = 4 / 2 # Nenhum erro;

except ZeroDivisionError:
    print("Try 2: ZeroDivisionError")

else:
    print("Try 2: Else") # Vai ser executado.
"""

# ------------------------------- __main__ -------------------------------

"""
if __name__ == "__main__": # Esse if statement é usado para executar esse bloco, somente se for 
    print("Execuntado neste mesmo arquivo.") # executado por esse arquivo;
    print(f"Variavel __name__: {__name__}")

else:
    print("Execuntado de um arquivo diferente.") # Esse bloco será executado, somente se o arquivo
    print(f"Variavel __name__: {__name__}") # for executado atraves de uma importação em outro arq.
"""