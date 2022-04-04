# ------------------------------------------  Funções ------------------------------------------ 

def tratamento_letra(arq): # Vai tratar o arquivo removendo espaços e quebra linhas
    registro = arq.replace(" ", "").replace("\n", "")
    return registro

def tratamento_palavra(arq): # Vai tratar o arquivo removendo quebra linhas e seperando palavras em listas. Ex: ["Palavra1", "Palavra2"]
    registro = arq.replace("\n", " ").split(" ")
    return registro    

def contador_letras(arq, letPal): # Contador, conta quantos caracteres(var letPal) tem em um arquivo(var arq) 
    cont = 0
    for i in tratamento_letra(arq): # i vai receber letPal por letPal do arquivo 
        if letPal.lower() == i.lower(): # Vai comparar o caractere(var letPal) passada com os caracteres do arquivo(var i)
            cont = cont + 1
    return cont

def contador_palavras(arq, palavra): # Contador, conta um padrão de caracteres(var palavra), palavra, e compara com padrões de um arquivo(var arq) passado
    cont = 0
    for i in tratamento_palavra(arq): #  Vai comparar itens(var i) da lista(var listaarq) e vai soma no contador se o padrão bater
        if i.lower() == palavra.lower() or i.lower() == palavra.lower() + "'s" or i.lower() == palavra.lower() + "s" or i.lower() == palavra.lower() + ",": 
            cont += 1
    return cont

def calculo_porcentagem(arquivo, tipo = 0): # Vai tirar a porcentagem de ocupação de cada caractere
    reserva = "" # Var que vai armazenar o ultimo caractere utilizado na repetição
    percDict = {} # Dicionario a onde vai ficar armazenado as informações

    if tipo == 0:
        lista = tratamento_letra(arquivo)
        for letPal in lista:
            if reserva.lower() == letPal.lower(): # Condicional usada pra não gerá caracteres repetidos para o dicionario
                continue
            else:
                percDict[letPal.lower()] = str(round((contador_letras(lista, letPal) * 100) / len(lista), 2)) + "%" # Calculo de procentagem e armazenamento do dado no dict(var percDict)
                reserva = letPal
        return percDict
    else:
        lista = tratamento_palavra(arquivo)
        for letPal in lista:
            if reserva.lower() == letPal.lower():
                continue
            else:
                percDict[letPal.lower()] = str(round((contador_palavras(arquivo, letPal) * 100) / len(lista), 2)) + "%"
                reserva = letPal
        return percDict

def salvar_arquivo(func, nomeArq, modo, letPal = ""): # Essa função vai tratar o resultado(arg func) e realizar a saida para um arquivo
    name = nomeArq.replace(".txt","") # Vai remover a extensão e vai salvar na var
    
    with open(f"{name}log.txt", "a") as arq: # Vai abrir um arquivo no modo append
        arq.write(f"---{nomeArq}---\n")
        if type(func) == dict:
            arq.write(f"-{modo}-\n")
            for i in func: # Vai tratar o dicionario e realizar a saída pro arquivo
                arq.write(f"{i}: {func[i]}\n")
            arq.write(f"-----------------\n")          
        else:
            arq.write(f"-{modo}-\n")
            arq.write(f"O padrão {letPal.upper()} possui {func} match.\n")
            arq.write(f"-----------------\n")

def limpar_arquivo(arquivo):
    nomeArquivo = arquivo.replace(".txt", "")
    with open(f"{nomeArquivo}log.txt", "w") as arq:
        arq.write("")

# ------------------------------------------ Execução ------------------------------------------ 

while True:
    try:
        caminho = input("Caminho: ")
        with open(caminho, "r") as arq:
            arquivo = arq.read() 
        
        while True:
            escolha = input("""Opções:
    1 - Ocupação de caracteres
    2 - Ocupação de palavras
    3 - Contagem de letras
    4 - Contagem de palavras
    5 - Limpar arquivo
    9 - Outro Arquivo
    0 - Sair
    >>> """)
            if escolha == "1":
                salvar_arquivo(calculo_porcentagem(arquivo), caminho, "Ocupação de caractere")
                print("Arquivo salvo!")
            
            elif escolha == "2":
                salvar_arquivo(calculo_porcentagem(arquivo, 1), caminho, "Ocupação de palavras")
                print("Arquivo salvo!")
            
            elif escolha == "3":
                letPal = input("Letra: ")
                contagem = str(contador_letras(arquivo, letPal))
                salvar_arquivo(contagem, caminho, "Contagem de letras", letPal)
                print("Arquivo salvo!")
                
            elif escolha == "4":
                letPal = input("Palavra: ")
                contagem = str(contador_palavras(arquivo, letPal))
                salvar_arquivo(contagem, caminho, "Contagem de palavras", letPal)
                print("Arquivo salvo!")

            elif escolha == "5":
                limpar_arquivo(caminho)
                print("Arquivo limpo!")
            
            elif escolha == "9":
                raise FileNotFoundError
            
            elif escolha == "0":
                break
            
            else:
                continue
        break

    except FileNotFoundError:
        continue