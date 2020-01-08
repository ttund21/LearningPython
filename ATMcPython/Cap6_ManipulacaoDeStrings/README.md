# MANIPULAÇÃo DE STRINGS

## Anotações:

## Trabalhando com strings

### Strings literais

+ São strings usadas com aspas simples, exemplo:
  ```literais
  print('Hello World')

  # Saída:
  # Hello World
  ```

### Aspas Duplas

+ Strings começadas por aspas duplas, exemplo:
  ```aspasDuplas
  print("That is Alice's Cat")

  # Saída:
  # That is Alice's Cat
  ```
+ Perceba que com o uso das aspas duplas, podemos usar aspas simples para ser ser exibida junto com a string.

### Caracteres de escape

+ Permite utilizar caracteres que não poderiam ser inseridos de outra maneira;
+ É constituido de uma barra invertida ( \ ), seguida do caractere que você quer incluir;
+ Exemplo:
  ```escape
  print('That is Alice\'s Cat')
  
  # Saída:
  # That is Alice's Cat 
  ```
+ Lista de caracteres escapes que podem ser usados:
  
  | Caractere de escape |         Exibido como        |
  |         ---         |            ---              |
  |          \'         |  Aspas simples              |
  |          \"         |  Aspas duplas               |
  |          \t         |  Tabulação                  |
  |          \n         |  Quebra ou mudança de linha |
  |          \\         |  Barra invertida            |

### Strings puras

+ Pode-se inserir um r antes das aspas para ignorar todos os caracteres de escape, exemplo:
  ```pura
  print(r'That is Alice\'s Cat')
  
  # Saída:
  # That is Alice\'s Cat
  ```

### Strings de múltiplas linhas com aspas triplas

+ Começam e termina com três aspas simple ( ''' ), qualquer espaço e tabulção será considerado nela e regras de indentação não se aplica aqui.
+ Exemplo:
  ```multipla
  print(r'''Ola
  	Mundo \'
  teste ''')

  # Saída:
  # Ola
  # 	Mundo \'
  # teste
  ```

### Comentários de múltiplas linhas

+ Comentários de múltiplas linhas é usado para comentários em massa, é constituido por três aspas duplas ( """ ) no ínicio e no fim, exemplo:
  ```comentMassa
  """comentario
  print('Ola Mundo')
  print('Ola Mundo')
  print('Ola Mundo')
  """
  print('Ola Mundo')
  ```

### Indexação e slicing de strings 

+ Strings assim como listas também pode ser usado indexação e slice;
+ Exemplo:
  ```stringSliceIndex
  h = 'hello world'

  print(h[0])
  print(h[0:5])

  # Saída:
  # h
  # hello
  ```

### Operadores in e not in com strings

+ Operadores in e not in podem ser usados com strings, assim com em valores de lista;
+ Exemplo:
  ```inNotIn
  h = 'hello world'

  print('o' in h)
  print('o' not in h)
  
  # Saída:
  # True
  # False
  ``` 

## Métodos úteis de string

### Métodos de string upper(), lower(),l isupper() e islower()

#### Métodos upper() e lower()

+ Os métodos upper() e lower() vão retornar toda string em maiúscula, no caso do upper(), e minúscula, no caso do lower();
+ Os caracteres que não são letras não serão alterados;
+ Eles não alteram a variável apenas exibem;
+ Exemplo:
  ```upperLower
  h = 'Hello World 1*'

  print(h.upper())
  print(h.lower())
  print(h)

  # Saída:
  # HELLO WORLD 1*
  # hello world 1*
  # Hello World 1*
  ```
+ Exemplo Prático:
  ```pratico1
  h = input('Escreva Sim: ')

  if h.lower() == 'sim':
  	print('hello world')
  ```

#### Métodos isupper() e islower()

+ São métodos que retornam valores booleanos, retornará True caso todos caracteres estejam maiúsculo, no caso do isupper(), e minúsculo, no caso do islower();
+ Caracteres que não sejam letras são ignorados;
+ Exemplo: 
  ```isUpperIsLower
  h = 'HELLO 1*'
  o = 'Hello 1*'

  print(h.isupper())
  print(h.islower())

  print(o.isupper())
  print(o.islower())

  # Saída:
  # True
  # False
  # False
  # False
  ```

### Método de string isX

+ Existem vários métodos que começam com *is*, esses métodos retornam um valor boobleano que descreve a natureza da string;
+ Alguns desses métodos:
  + isalpha(): True se a string for constituida somente de letras e não houver não um valor vazio;
  + isalnum(): True se a string for constituida somente de letras ou numeros e não houver não um valor vazio;
  + isdecimal(): True se a string conter apenas valores númerico e não houver não um valor vazio;
  + issapce(): True se a string for constituida apenas por espaço ou tabulação e não estiver vazio;
  + istitle(): True se a string for constituida apenas de palavras que comecem com letra maiúscula; 
+ Métodos bastante úteis para fazer a validação de uma string;
+ Exemplo prático:
  ```pratico2
  while True:
  	password = input('Create a password(letters and numbers only):\n> ')
    
  	if password.isalnum():
        	print('Password Created!')
        	break
    	else:
        	print('Letters and Numbers')
  ```

### Métodos de string startswith() e endswith()

+ Esse métodos retornarão True se a string comoçar com letra especificada, no caso do startswith(), ou terminar, no caso do endswith();
+ Exemplo:
  ```startsEnds
  h = 'Helloo'

  print(h.startswith('H'))
  print(h.endswith('O'))

  # Saída:
  # True
  # False
  ```

### Métodos de string join() e split()

#### join()

+ É um método usado para unir valores de lista em uma única string;
+ Ele recebe um valor que vai ficar entre cada item da lista;
+ Exemplo:
  ```join
  h = ['a', 'b', 'c']

  print('-'.join(h))

  # Saída:
  # a-b-c 
  ```

#### split()

+ O split faz um inverso é chamado em uma string e retorna uma lista;
+ Ele vai receber um valor no qual irá cortar da string e mandar para uma lista;
+ Exemplo:
  ```split
  h = 'Hello World'

  print(h.split(' '))
  
  # Saída:
  # ['Hello', 'World']
  ``` 

### Justificando texto com rjust(), ljust() e center()

#### rjust()

+ Usado para justificar um texto a direita, exemplo:
  ```rjust
  print('hello'.rjust(20, '='))

  # Saída:
  # ===============hello
  ```

#### ljust()

+ Justifica o texto a esquerda, exemplo:
  ```ljust
  print('hello'.ljust(20, '='))
  
  # Saída:
  # hello===============
  ```

#### center()

+ Justifica o texto para o meio, exemplo:
  ```center
  print('hello'.center(20, '='))
  
  # Saída:
  # =======hello========
  ```

### Removendo espaços em branco com strip(), rstrip() e lstrip()

#### lstrip()

+ Remove espaços em branco do lado esquerdo, exemplo:
  ```lstrip
  h = '       Hello World        '

  print(h.rstrip())

  # Saída:
  # Hello World 
  ```

#### rstrip()

+ Remove espaços em branco do lado direito, exemplo:
  ```rstrip
  h = '       Hello World        '

  print(h.rstrip())

  # Saída:
  #        Hello World
  ```

#### strip()

+ Remove espaços em branco dos dois lados, exemplo:
  ```strip
  h = '       Hello World        '

  print(h.strip())

  # Saída:
  # Hello World
  ```

+ Todas as funções strip() aceitam argumento do tipo string que especificará qual caractere vai ser removido, exemplo:
  ```charStrip
  h ='Hello World'

  print(h.strip('World'))

  # Saída:
  # Hello
  ```

### Copiando e colando strings com o módulo pyperclip

+ Primeiro passo para usar este módulo é instalar ele no seu pc:
  + sudo pip install pyperclip
+ Após instalção basta importa-lo e usa-lo;
+ O módulo *pyperclip* tem funções para trabalhar com sua área de transferencia do seu computador;

#### pyperclip.copy()

+ Esta função copia o dado para sua área de transferencia, exemplo:
  ```copy
  import pyperclip

  pyperclip.copy('Hello')

  # Hello foi copia do para sua área de transferencia
  ```

#### pyperclip.paste()

+ Esta função cola o dado que está na sua área de transferencia, exemplo:
  ```paste
  import pyperclip

  print(pyperclip.paste())

  # Será colado no programa o que está na sua area de transferencia
  ```
