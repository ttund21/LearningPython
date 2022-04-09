from tkinter import Tk, Listbox, Button


# Frame
root = Tk()
root.resizable(False, False)
root.title("List Box")

# Funções
def limpar_lista(li):
    li.delete(0, "end")

def exibir_item(li):
    print(li.get("active"))

# List Box
lista = Listbox(root, selectmode="extended") # extended faz selecionar mais de um item

"""
# Adicionando item por item
lista.insert(0, "Primeiro")
lista.insert(1, "Segundo")
lista.insert("end", "Ultimo")
lista.insert(2, "Terceiro")
lista.insert(3, "Quarto")
"""
# Adicionando a partir de uma lista

nomes = ["Primeiro", "Segundo", "Terceiro", "Quarto"]

for i in nomes:
    lista.insert("end", i)

# Button
limpar = Button(root, text="Limpar", command=lambda: limpar_lista(lista))
exibir = Button(root, text="Exibir", command=lambda: exibir_item(lista))

# Pack
lista.pack()
limpar.pack()
exibir.pack()

root.mainloop()