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
  # inventory.py
  stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

  def displayInventory(inventory):
  	print("Inventory:")
  	item_total = 0
  	for k, v in inventory.items():
  		print(str(v) + ' ' + k)
  		item_total += v
  	print("Total number of items: " + str(item_total))
  
  displayInventory(stuff)
  ```
