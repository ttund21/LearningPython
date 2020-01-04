def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for item, amount in inventory.items():
        total += amount
        print(f'{amount}  {item}')
    print(f'Total number of items: {total}')


inventory = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

displayInventory(inventory)

