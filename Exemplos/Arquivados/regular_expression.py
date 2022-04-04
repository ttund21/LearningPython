"""
import re

texto = "spamspamspamspamspamspam"
padrao =  r"am"

if re.match(padrao, texto): # Match a regular expression pattern to the beginning of a string.
    print("Match") 
else:
    print("No match")

if re.search(padrao, texto): # Search a string for the presence of a pattern.
    print("Match") 
else:
    print("No match")

print(re.findall(padrao, texto)) # Return an iterator yielding a Match object for each match.
"""

"""
import re

texto = "Ser bom é fácil. O difícil é ser justo."
padrao = r"difícil"

match = re.search(padrao, texto)

if match:
    print(match) # Vai retornar o objeto 'match'
    print(match.group()) # Vai retornar o match
    print(match.span()) # Vai retornar em uma tupla a posição inicial e final do match
    print(texto[match.start()]) # Vai retornar a primeira posição do match
    print(texto[match.end() - 1]) # Vai retornar a final posição do match
"""

"""
import re

texto = "Um dia spam, foi um stam legal spam"
padrao = r"s.am" # '.' dar match em qualquer caractere e r antes deixa a string raw 

# Quando dar match no padrao, será substituido por maps, pode ser configurado o número de sub.
novoTexto = re.sub(padrao, "maps", texto, 2)
print(novoTexto)
"""

"""
import re

padrao = r"^s.am$" # Irá dar match em um sequencia que tem começar com 's', qualquer caratere depois
# do s, e terminar com 'm'

if re.match(padrao, "stam"):
    print("Match")

if re.match(padrao, "slam"):
    print("Match")

if re.match(padrao, "sitiam"):
    print("Match")
"""

"""
import re

padrao = r"s[t,p,l]am" # Cria uma lista de caracteres aceitos

if re.match(padrao, "slam"):
    print("Match")

if re.match(padrao, "spam"):
    print("Match")

if re.match(padrao, "slam"):
    print("Match")

if re.match(padrao, "svam"):
    print("Match")
"""

"""
import re 

texto = "Hoje é dia 22"
padrao = r"[0-9][0-9]"

match = re.search(padrao, texto)

print(match.group())
"""

"""
import re

padrao = r"[A-Za-z]a[a-z]a"

if re.match(padrao, "Casa"):
    print("Match")

if re.match(padrao, "lava"):
    print("Match")

if re.match(padrao, "8asa"):
    print("Match")
"""

"""
import re

padrao = r"[^a-zA-Z][^0-9]"

if re.match(padrao, "0A"):
    print("Match")

if re.match(padrao, "11"):
    print("Match")
"""

"""
import re

texto = "Boa Tarde, meu email é l0g1su1@hotmail.com, me mande os arquivos para imprimir."
padrao = r"[A-Za-z0-9]*@.*\.com"

match = re.search(padrao, texto)

if match:
    print(match.group())
"""

"""
import re

padrao = r"egg(spam)*"

if re.match(padrao, "eggspamspamspamspam"):
    print("Match")

if re.match(padrao, "eggspamspamspamspamegg"):
    print("Match")

if re.match(padrao, "egg"):
    print("Match")
"""

"""
import re

padrao = r"egg(spam)+"

if re.match(padrao, "eggspamspamspam"):
    print("Match 1")

if re.match(padrao, "egg"):
    print("Match 2")

if re.match(padrao, "eggspamspamspamspamegg"):
    print("Match 3")
"""

"""
import re

texto = "[@outlook.com] Boa Tarde, meu email é l0g1_su1@hotmail.com."
padrao = r"[a-zA-Z0-9\-\_]+@[a-z]+\.com"

match = re.findall(padrao, texto)

print(match)
"""

"""
import re

padrao = r"arco(-)?[íi]ris"

if re.match(padrao, "arcoiris"):
    print("Match 1")

if re.match(padrao, "arco-íris"):
    print("Match 2")
"""

"""
import re

padrao = r"(spam){1,3}$"

if re.match(padrao, "spam"):
    print("Match 1")

if re.match(padrao, "spamspamspamspam"):
    print("Match 2")

if re.match(padrao, "spamspamspam"):
    print("Match 3")
"""

"""
import re

padrao = r"(spam)(egg)" # Dois grupos

match = re.match(padrao, "spamegg")

print(match.group(1)) # exbindo grupos
print(match.group(2))
"""

"""
import re 
# (?P<nome_do_grupo>...) cria um grupo nomeado, (?:...) não acessivel pelo .group()
padrao = r"(?P<grupo1>[Aa]rco)(?:-)?(curvo)"

match = re.match(padrao, "Arco-curvo")

print(match.group("grupo1"))
print(match.group(2))
"""

"""
import re

# Ou a ou e
padrao = r"gr(a|e)y"

if re.match(padrao, "grey"):
    print("Match 1")

if re.match(padrao, "gray"):
    print("Match 2")
"""

"""
import re

padrao = r"^(quero)(-| )\1$" # \1 repete o grupo 1 que no caso seria (spam)

if re.match(padrao, "quero quero"):
    print("Match 1")

if re.match(padrao, "quero"):
    print("Match 2")

if re.match(padrao, "quero-quero"):
    print("Match 3")
"""

"""
import re

texto = "Bom Dia,\nSegue os contatos,\nChico, chico-cimavel@gmail.com;\nAna, ana_lucia@outlook.com."
padrao = r"[\w\-]+@\w+.com"

print(texto)

match = re.findall(padrao, texto, 0)

print(f"\n{match}")
"""

"""
import re

padrao = r"(\d){1,2}"

if re.match(padrao, "spam"):
    print("Match 1")

if re.match(padrao, "88"):
    print("Match 2")
"""

"""
import re

texto = "Um gato de botas!"
padrao = r"\b(gato)\b"

match = re.search(padrao, texto)

print(match)
"""