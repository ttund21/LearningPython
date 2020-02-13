import re

def regex(me):
    er = re.compile(r'\b\d{3}-?\d{4}\b')
    erSearch = er.search(me)
    return erSearch

def fix(me):
    sep = list(me)
    sep.insert(0, '3')
    return print(''.join(sep))

while True:
    number = input('Número do telefone: ')

    resp = regex(number)

    if resp == None:
        print('Número Inválido!')
        continue
    else:
        print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
        fix(number)
        break
