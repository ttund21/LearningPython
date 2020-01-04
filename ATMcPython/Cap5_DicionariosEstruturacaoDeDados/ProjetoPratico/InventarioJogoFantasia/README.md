# Inventário de um jogo de fantasia

+ Você está criando um videogame de fantasia. A estrutura de dados para modelar o inventário do jogador será um dicionário em que as chaves são valores de string que descrevem o item do inventário e o valor será um inteiro detalhando quantos itens desse tipo o jogador tem. Por exemplo, o valor de dicionário {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} quer dizer que o jogador tem 1 corda (rope), 6 tochas (torches), 42 moedas de ouro(gold coins) e assim por diante.

+ Crie uma função chamada displayInventory() que possa receber qualquer “inventário” possível e exiba essas informações da seguinte maneira:
  ```invetario
  Inventory:
  12 arrow
  42 gold coin
  1 rope
  6 torch
  1 dagger
  Total number of items: 62
  ```
+ Dica: você pode utilizar um loop for para percorrer todas as chaves de um dicionário.
  ```inventario2
  def displayInventory(inventory):
  	total = 0
  	print('Inventory:')
  	for item, amount in inventory.items():
        	total += amount
        	print(f'{amount}  {item}')
  	print(f'Total number of items: {total}')


  inventory = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

  displayInventory(inventory)
  ```
