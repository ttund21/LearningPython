def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for item, amount in inventory.items():
        total += amount
        print(f'{amount}  {item}')
    print(f'Total number of items: {total}')

def addToInventory(loot, inventory):
    for item in loot:
        inventory.setdefault(item, 0)
        inventory[item] += 1 


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(dragonLoot, inv)
displayInventory(inv)
