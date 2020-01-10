pet = []

while True:
    print('\n1 - To add pet name on your list.\n2 - To search pet name on your list.\n3 - To show all names on your list.\nEnter - To exit the program.')
    resp = input('>>> ')
    
    if resp == '1':
        while True:
            print('\nAdd pet name:')
            addPet = input('>>> ')
            if addPet == '':
                break
            else:
                pet += [addPet]
    
    elif resp == '2':
        while True:
            print('\nEnter pet name:')
            searchPet = input('>>> ')
            if searchPet == '':
                break
            elif searchPet in pet:
                print(f'{searchPet} is in your list.')
            elif searchPet not in pet:
                print(f'{searchPet} is not on your list')
           
    elif resp == '3':
        for i in range(len(pet)):
            print(f'{i + 1}º name: {pet[i]}')

    elif resp == '':
        break

    else:
        print('\nWrong Command')
        
