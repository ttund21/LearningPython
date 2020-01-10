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
