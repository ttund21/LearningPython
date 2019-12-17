# FUNÇÕES

## Anotações:

+ O objetivo de toda função é o processamento de alguma informação e o retorno do dado processado;
+ Função é como se fosse um miniprograma dentro de um programa;
+ Blocos de códigos que podemos reutilizar;
+ Umas das melhores práticas é evitar sempre a duplicação de códigos;
+ Constituida por:
  + Palavra-chave **def**;
  + Um nome para função seguido de parenteses;
  + E opcionalmente nome do parâmetro da sua função na ordem de execução;
  + Dois-pontos;
  + E um bloco de código indentado.
+ Exemplo sem o uso de função:
  ```exemplosemfuncao
  print('Howdy!')
  print('Howdy!!!')
  print('Hello There.')
  print('Howdy!')
  print('Howdy!!!')
  print('Hello There.')
  print('Howdy!')
  print('Howdy!!!')
  print('Hello There.')
  ```
+ Exemplo usando função:
  ```exemplocomfuncao
  def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello There.')
    
  hello()
  hello()
  hello()
  ```

### Instruções def com parâmetros

+ Nas funções também podem ser criadas parâmetros;
+ Um valor é esquecido quando a função retorna;
+ Exemplo:
  ```exemplodefparametro
  def imc(valor):
  	if valor < 17.0:
        	return 'Muito abaixo do peso'
  	elif valor <= 18.49:
        	return 'Abaixo do peso'
  	elif valor <= 24.99:
        	return 'Normal'
  	elif valor <= 29.99:
        	return 'Acima do Peso'
  	elif valor <= 34.99:
        	return 'Obesidade I'
  	elif valor <= 39.99:
        	return 'Obesidade II'
  	else:
        	return 'Obesidade III'

  peso = float(input('Peso >>> '))
  altura = float(input('Altura >>>'))
  valorImc = peso / altura**2
  respImc = imc(valorImc)
  print('Seu IMC é:' + str(respImc))
  ```

### Valores de retorno e instruções return

+ Usada para declarar a informação a ser retornada pela função;
+ E também podem ser utilizadas para finalizar a execução da função;
+ Exemplo de um valor sendo retornado a função:
  ```returnvalor
  def soma():
  	return 10

  num = soma()
  print(num)
  ```
+ Exemplo de finalização de função com o **return**:
  ```returnbreak
  def soma(x, y):
  	num = x * y
  	return num
  	print('Testing...')

  print(soma(10, 20))
  ```

### Valor None

+ O **none** ele representa a ausência de um valor;
+ É o único valor do tipo NoneType;
+ Em outras linguagens é chamado de null, nil ou undefined;
+ Deve ser sempre digitado com letra maiúscula, **None**;
+ Exemplo de saída com valor None:
  ```exemplonone
  def teste():
  	hello = "Hello World"

  print(teste())

  # A saída desse código será 'None';
  # Pois a função teste() não retorna valor nenhum.
  ```

### Argumentos nomeados(keyword arguments) e print()

+ Os **keyword arguments** geralmente são usados para parâmetros opcionais;
+ Usaremos de explicação a função **print()**, que possui os parâmetros opcionais **end e sep**;
+ Um exemplo do **keyword end=**:
  ```keywordend
  print('Hello', end=' Keyword End ')
  print('World')

  # Em vez do print() usar o seu default que seria quebrar linha;
  # Com o END alteramos esse default para 'Keyword End'.
  ```
+ Um exemplo do **keyword sep=**:
  ```keywordsep
  print('Hello', 'World', sep=',')

  # Outra vez o print() não utilizara o seu default que seria fazer o espaçamento entre as palavras;
  # Com o SEP definimos que em vez do espaçamento usaremos vírgula.
  ```
+ **Keyword Arguments** também podem ser utilizados nas funções que criamos, mas só sera visto mais pra frente nos tipos de dados lista e dicionário.

### Escopo Local e Global

+ Variáveis e parâmetros atribuídos em uma função chamada existem no **escopo local** dessa função;
+ Variáveis que existem fora de todas as funções existem no **escopo global**, e são chamadas de **variáveis globais**;
+ Exemplo:
  ```escopos
  greeting = "Hello My Friend" # Uma variável global, em um escopo global.

  def hello(x, y): # Uma variável/parâmetro local, em um escopo local.
  	return (x * y)

  print(greeting)
  print(hello(4, 4))
  ```
+ Uma variável ou é global ou local, **nunca os dois juntos**;
+ Um **escopo global** é iniciado junto com o programa e é esquecido junto com a finalização do mesmo;
+ Já o **escopo local** se inicia quando uma função é chamada e é esquecido quando a função retorna;
+ Motivos porque entender escopo é importante:
  + O código em um escopo global **não pode** usar variáveis locais;
  + Mas um escopo local **pode usar** variáveis globais; 
  + Um código no escopo local de uma função **não pode** usar variáveis de nenhum outro escopo local;
  + Pode-se usar variáveis com o mesmo nome desde que elas estejam em escopos diferentes.
+ Um motivo para o python ter seperação de escopo, é para evitar um número crescente de variáveis globais, assim evitando bugs, erros por valor inadequado e etc.

#### Variáveis locais não podem ser usadas no escopo global

+ Um programa com erro de escopo:
  ```escopoglobalerror
  def teste():
  	hello = "Hello World"
  	return hello
  print(hello)
  ```
+ Erro gerado após a execução:
  ```erroescopoglobal
  Traceback (most recent call last):
    File "teste.py", line 4, in <module>
      print(hello)
  NameError: name 'hello' is not defined
  ```
+ Esse erro ocorre porque a função **print()** que está no escopo global está tentando chamar variável local **hello** que está no escopo local da função **teste()**;

#### Escopos locais não podem usar variáveis de outros escopos locais

+ Lembrando que um novo escopo local é criado sempre que um nova função é criada;
+ Um exemplo de um função irá tentar acessar uma variavel local de outra função:
  ```escopolocalerror
  def test():
  	hello = "Hello Wrold"
  	return hello 

  def test01():
  	return hello

  print(test01())
  ```
+ Erro gerado após a execução:
  ```erroescopolocal
  Traceback (most recent call last):
    File "teste.py", line 9, in <module>
      print(test01())
    File "teste.py", line 6, in test01
      return hello
  NameError: name 'hello' is not defined
  ```
+ Um escopo local não pode acessar a variável local de outro escopo, então após a função **test01()** tentar retornar a variável **hello** da outra função, vai gerar o erro que esta variável não está definida.

#### Variáveis globais podem ser lidas a partir de um escopo local

+ Um exemplo de uso de variável global em escopo local:
  ```varGlobalEscpLocal
  def spam():
  	print(eggs)

  eggs = 49
  spam()

  # Saída: 49
  ```
+ Agora uma variável local sobrepõe uma global, exemplo:
  ```varGlobalEscpLocal2
  eggs = 49

  def spam():
  	eggs = 490
        return eggs
  
  print(eggs)
  print(spam())

  # Saída: 
  # 49
  # 490
  ```

#### Variáveis locais e globais com o mesmo nome

+ O python te dá a possibilidade de ter vaiáveis locais e globais com o mesmo nome, mas é bom evitar fazer isso, pois vai deixar seu código confuso.
+ Um exemplo de uso:
  ```varLocGloSameName
  eggs = "Global"

  def test01():
  	eggs = "test01 local"
  	return eggs

  def test02():
  	eggs = "test02 local"
  	return eggs

  print(eggs)
  print(test01())
  print(test02())

  # Saída:
  # Global
  # test01 local
  # test02 local
  ```

### Instrução global

+ Usado para transformar uma variável local em global;
+ Se quiser modificar um valor de uma variavel local, a transforme em global, usando a instrução **global** na função;
+ Para referenciar uma variável global que está no escopo local, é necessário refernciar a função antes;
+ Um exemplo:
  ```instucaoglobal
  def test():
  	global var
  	var = 500
  	return var

  test()
  print(var)
  var = 5 
  print(var)

  # Saída:
  # 500
  # 5
  ```
+ Regras para se dizer se uma variável está no escopo local ou global:
  1. Se uma variável estiver sendo usado em escopo global, ele sempre será uma variável global;
  1. Se houver a instrução global em uma variável local, ela se tornará uma variável global;
+ Em uma função uma variável vai ser global ou local, não há maneira ter uma variável que esteja nos dois tipos;

### Tratamento de exceções
+ Considere o seguinte código:
  ```ZeroDivisionError
  def test(division):
  	return 10 / division

  print(test(0))
  ```
+ Essa vai ser a saída do programa:
  ```ZeroDivisionErrorOut
  Traceback (most recent call last):
    File "teste.py", line 4, in <module>
      print(test(0))
    File "teste.py", line 2, in test
      return 10 / division
  ZeroDivisionError: division by zero
  ```
+ **ZeroDivisionError** uma *exceção* gerada, pois não podemos dividir números por zero;
+ Então quando uma *exceção* é gerada o programa é encerrado imediatamente, coisa que não queremos pra o nosso programa;
+ Então se quisermos evitar o encerramento do nosso programa usamos as instruções de tratamento de exceções **try** e **except**;
+ Forma de uso:
  + Palavra-chave **try**;
  + Em um bloco de código indentado, um argumento que pode gerar um exceção;
  + Uma linha abaixo na mesma indentação do try; Palavra-chava **except** seguido da exceção;
  + Em um bloco de código indentado, um bloco a ser executado caso a exceção ocorra.
+ Exemplo:
  ```TryExcept
  def test(division):
  	try:
        	return 10 / division
        except ZeroDivisionError:
        	print('Argumento invalido')

  print(test(10))
  print(test(2))
  print(test(5))
  print(test(0))

  # Dessa vez quando zero for executado, em vez do programa finalizar;
  # Executará o bloco 'print('Argumento invalido')';

  # Saída:
  # 1.0
  # 5.0
  # 2.0
  # Argumento invalido
  # None
  ```
+ Também pode ser usado na chamada das funções, exemplo:
  ```TryExecptCall
  def test(division):
  	return 10 / division

  try:
  	print(test(10))
  	print(test(5))
  	print(test(0))
  	print(test(2))
  except ZeroDivisionError:
  	print('Error')

  # Note que o 'print(test(2))' não sera executado;
  # Pois após a cláusula 'except', ela não retoma para cláusula try;
  # Ela continuará descendo.
  
  # Saída:
  # 1.0
  # 2.0
  # Error
  ```
