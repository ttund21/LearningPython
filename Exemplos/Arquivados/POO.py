"""
# Metodo de Classe

class Retangulo:
    def __init__(self, largura, altura):
       self.altura = altura # q1.altura = altura
       self.largura = largura # q1.largura = largura

    def calculo_area(self):
        return self.altura * self.largura

    @classmethod # esse metodo vai coletar um novo unico valor, e vai considerar como se fosse
    def quadrado(cls, lado): 
        return cls(lado, lado) # q1 = Retangulo(lado, lado)
    
q1 = Retangulo.quadrado(4)

print(f"Altura: {q1.altura} cm\nLargura: {q1.largura} cm\nArea: {q1.calculo_area()} cm")
"""

"""
from datetime import date

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def data_nascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano) # Calcula a idade atraves do ano des nascimento

    @staticmethod
    def maior_idade(idade):
        if idade >= 18:
            return "Maior de idade!"
        else:
            return "Menor de idade!"


p1 = Pessoa.data_nascimento("Jão", 2000)
p2 = Pessoa("Ana", 15)

print(f"Nome: {p1.nome}, Idade: {p1.idade}, {p1.maior_idade(p1.idade)}")
print(f"Nome: {p2.nome}, Idade: {p2.idade}, {p2.maior_idade(p2.idade)}")
"""

"""
class Carro:
    def __init__(self, meios):
        self.meios = meios

    def meio_agua(self):
        return False

    @property # Quando o atributo de instância com o mesmo nome do método for acessado, 
    def meio_ar(self): # o método será chamado em seu lugar.
        return False

srx = Carro(["Asfalto", "Terra"])

print(srx.meio_agua()) # Um metodo sem o property sendo chamado
print(srx.meio_ar) # Um metodo com o property sendo chamado
"""

"""
# Exemplo de como acessar um atributo privado fora da classe

class Test:
    __egg = 5

t = Test()

print(t._Test__egg)
"""


"""
class Produtos:
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco

    def desconto(self, porcentagem):
        return self.preco - (porcentagem * self.preco) / 100

    @property # Getter
    def produto(self): # Esse getter vai capturar o atributo produto e executar esse metodo sempre que ele for chamado
        return self._produto

    @produto.setter # Setter
    def produto(self, valor): # Esse setter vai aplicar um padrao de sempre começar a string com o primeiro caractere maiusculo
        self._produto = valor.title() # O getter 'self_produto' vai receber o valor definido tratado pelo metodo 'title()'

    @property # Getter
    def preco(self): # Esse getter vai capturar o atributo preco e executar esse metodo sempre que ele for chamado
        return self._preco
    
    @preco.setter # Setter
    def preco(self, valor): # Esse setter vai remover qualquer caractere que não seja numero, do atributo preco
        reg = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] # Lista de caracteres permitidos
        palavra = [] # Onde vai ser armazenado os caracteres permitidos

        if isinstance(valor, str):
            
            for letra in valor: # Sera testado letra por letra no valor passado
                if letra in reg: # Se a letra estiver em reg, adicione a lista palavra
                    palavra.append(letra)
            
            self._preco = float("".join(palavra)) 
        
        else:
            self._preco = valor
    

panela = Produtos("panela", "R$ dsajldkjasldkjsalkdjasl50")
caderno = Produtos("cAderno", 25)

print(f"Nome: {panela.produto}\nValor: R${panela.preco}\nC/ Desconto: R${panela.desconto(50)}")
print(f"\nNome: {caderno.produto}\nValor: R${caderno.preco}\nC/ Desconto: R${caderno.desconto(50)}")
"""

"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        valor -= 10
        self._idade = valor


p1 = Pessoa("Peter", 50)

print(f"Nome: {p1.nome}\nIdade: {p1.idade}")
"""

"""
class Sucos:
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade

    def __str__(self): # Metodo magico de exibição de objeto
        return f"{self.nome} ({self.capacidade}L)" # Essa vai ser a saida da chamada do objeto

    def __add__(self, self2): # Esse metodo vai somar dois objetos
        return f"{self.nome + '&' + self2.nome} ({self.capacidade + self2.capacidade}L)"


s1 = Sucos("Goiaba", 1)
s2 = Sucos("Maçã", 2)
total = s1 + s2 # Aqui o metodo __add__ será invocado e irá realizar a adição

print(f"Suco: {s1}") # Aqui é o resultado do dunder __str__, ele vai retorn o metodo
print(f"Suco: {s2}") # e observe que não é necessário invocar a função s2.__str__().
print(f"Mistura: {total}")
"""

"""
#You are given a Juice class, which has name and capacity properties.
#You need to complete the code to enable and adding of two Juice objects, resulting in a
#new Juice object with the combined capacity and names of the two juices being added.

#For example, if you add an Orange juice with 1.0 capacity and an Apple juice with 2.5 capacity, 
#the resulting juice should have:
#name: Orange&Apple
#capacity: 3.5

#The names have been combined using an & symbol.

# Expect output: Orange&Apple (3.5L)


class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')

    def __add__(self, self2):
        return f"{self.name}&{self2.name} ({self.capacity + self2.capacity}L)"


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)
"""
