def leet(palavra):
    leet ={'A':'4', 'B':'13', 'C':')', 'D':'[)', 'E':'3', 'F':'|=', 'G':'6', 'H':'|-|', 'I':'|', 'J':']', 'K':'|<', 'L':'1', 'M':'|Y|', 'N':'/\/', 'O':'0', 'P':'|>',
            'Q':'0,', 'R':'|2', 'S':'5', 'T':'7', 'U':'[_]', 'V':'\/', 'W':'\\v/', 'X':'}{', 'Y':'`/', 'Z':'2'}
    listword = list(palavra)
    leetword = []
    for i in listword:
        try:
            leetword.append(leet[i.upper()])
        except KeyError:
            leetword.append(i)
    print(''.join(leetword))

palavra = input('Escreva uma palavra ou frase: ')

leet(palavra)
