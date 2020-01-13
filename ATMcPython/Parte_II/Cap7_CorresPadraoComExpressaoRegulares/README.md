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
