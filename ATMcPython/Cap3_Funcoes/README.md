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

