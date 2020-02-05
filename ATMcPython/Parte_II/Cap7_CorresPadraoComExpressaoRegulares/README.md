# Correspondência De Padrões Com Expressões Regulares

## Anotações:

## Encontrando padrões de texto sem usar expressões regulares

+ Suponha que você quer encontrar um número de telefone em uma string;
+ O padrão de telefone você já sabe: 4 números, 1 hifen e 4 números;
+ Vamos criar uma função básica para identificar esse padrão:
  ```telefone
  def telephone(tel):
  	if len(tel) != 9:
        	return False
  	for i in range(4):
        	if not tel[i].isdecimal():
            		return False
  	if tel[4] != '-':
        	return False
  	for i in range(5, 9):
        	if not tel[i].isdecimal():
            		return False

  return True



  print(telephone('3245-2455'))
  print(telephone('Water'))

  # Saída:
  # True
  # False
  ```
+ Uma aplicação prática:
  ```telefonePratica
  def telephone(tel):
  	if len(tel) != 9:
        	return False
  	for i in range(4):
        	if not tel[i].isdecimal():
            		return False
  	if tel[4] != '-':
        	return False
  	for i in range(5, 9):
        	if not tel[i].isdecimal():
            		return False

  return True

  message = 'Call me at 3258-8899 tomorrow. 4845-5862 is my office.'
  for i in message.split():
  	if telephone(i):
        	print(f'Telephone: {i}')

  for i in range(len(message)):
  	strings = message[i:i + 9]
    	if telephone(strings):
        	print(f'Telefone: {strings}')
  
  # Saída:
  # Telephone: 3258-8899
  # Telephone: 4845-5862
  # Telefone: 3258-8899
  # Telefone: 4845-5862
  ```

## Encontrando padrões de texto com expressões regulares

### Criando objetos Regex

+ Todas as funções **regex** estão no módulo **re**:
  ```re
  import re
  ```
+ Criando um objeto que corresponda a um padrão com o método *compile()*:
  ```compile
  import re

  message = 'Call me, 3258-8899.'

  telRegex = re.compile(r'\d{4}-\d{4}')
  ```
+ Ponto foi criado um objeto que quando chamado ele irá buscar um objeto que corresponda ao valor de 4 digitos, 1 hifen e 4 digitos, ele poderia ser escrito também desse jeito **telsearch = re.compile(r'\d\d\d\d-\d\d\d\d')**;
+ É utilizada uma string com uma marcação **r** de **rawstring**, para facilitar a escrita, pois em vez de escrever *telsearch = re.compile('\\d{4}-\\d{4}')* escrevemos com o **r** para evitar o caractere de escape.

### Objetos Regex de correspondência

+ O método *search()* pesquisa na string que foi passada uma correspondência com a regex, que foi criada com o compile();
+ O search() retornará None caso não encontre nenhuma correspondência;
+ Caso encontre ele retornará um objeto Match;
+ Os **objetos Match** tem um método **group()** que retornará a string que o objeto search() encontrou;
+ Exemplo:
  ```searchMatch
  import re

  message = 'Call me, 3258-8899.'

  telRegex = re.compile(r'\d{4}-\d{4}')
  telSearch = telRegex.search(message)

  print(telSearch)
  print(f"Telephone: {telSearch.group()}")
  
  # Saída:
  # <re.Match object; span=(9, 18), match='3258-8899'>
  # Telephone: 3258-8899
  ```
+ Observe que foi criado um padrão com o **telRegex = re.compile(r'\d{4}-\d{4}')**, após criarmos o padrão usamos ele para procurar o **Match** na variável *message*, na linha de código **telSearch = telRegex.search(message)**;
+ Depois apenas para exibir didáticamente o *Match*, **print(telSearch)** e para mostrar qual string correspondeu o padrão do **compile()**, usamos **print(f"Telephone: {telSearch.group()}")**.

### Revisão de correspondência com expressão regular

+ Passos para usar ERs:
  1. Importe o módulo usando **import re**;
  2. Crie um objeto Regex usando a função **re.compile()**(Usando Raw String);
  3. Passe a string que você quer pesquisar usando o método **search() do objeto Regex**, lembre que se search() encontrar retornará um Match, caso não encontre retornará um None;
  4. Chame o método **group()** do objeto Match, para retorna a string que deu Match.

## Mais correspondência de padrões com expressõoes regulares

### Agrupando com parênteses

+ Nas expressões podemos agrupar caracteres com o parênteses "()", após a abertura e o fechamento do parênteses é criado 1 grupo;
+ Então no python você poderá usar o método *group()* para trazer o correspondente ao casamento;
+ Exemplo 1:
  ```erGrupo1
  import re

  message = 'Call me, 3258-8899.'

  telRegex = re.compile(r'(\d{4}-?){2}')
  telSearch = telRegex.search(message)

  print(telSearch.group())

  # Saída:
  # 3258-8899
  ```
+ Observe o agrupamento de caracteres *(\d{4}-?){2}*, veja que o \d\d\d\d-? fica como se fosse um caractere só, um grupo;
+ Exemplo 2:
  ```erGrupo2
  import re

  message = 'Call me, 3258-8899.'

  telRegex = re.compile(r'(\d{4})-(\d{4})')
  telSearch = telRegex.search(message)

  print(telSearch.group())
  print(f"Grupo 1: {telSearch.group(1)}")
  print(f"Grupo 2: {telSearch.group(2)}")

  # Saída:
  # 3258-8899
  # Grupo 1: 3258
  # Grupo 2: 8899
  ```
+ Podemos também chamar todos os grupos de uma vez em forma de tupla, exemplo:
  ```erGrupo3
  import re

  message = 'Call me, 3258-8899.'

  telRegex = re.compile(r'(\d{4})-(\d{4})')
  telSearch = telRegex.search(message)

  print(telSearch.groups())

  # Saída:
  # ('3258', '8899')
  ```
+ Caso seja necessário o uso do parenteses na ER só é necessário escapa-lo com a barra invertida i\\, exemplo:
  ```erGrupo4
  import re

  message = 'Call me, (79)3258-8899.'

  telRegex = re.compile(r'(\(\d{1,3}\))(\d{4}-?){2}')
  telSearch = telRegex.search(message)

  print(telSearch.group())
  ```
+ Observe que ficará (**\\(**\d{1,3}**\\)**).

### Fazendo a correspondência de vários grupos com pipe

+ O caractere pipe(**|**) na ER significa **ou**;
+ Um exemplo de uso:
  ```erPipe
  import re

  me = "Vou levar suco!"

  regex = re.compile(r"suco|refrigerante")
  regexSearch = regex.search(me)

  print(regexSearch.group())
  
  # Saída:
  # suco
  ```
+ Então nesse caso nossa ER ia casar ou com suco ou com refrigerante;
