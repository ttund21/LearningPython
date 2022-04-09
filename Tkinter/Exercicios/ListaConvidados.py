# Criar uma lista de convidados com a função de add, remover, limpar toda a lista e salvar lista

from tkinter import Tk, Button, Label, Listbox, Entry


# Frame
root = Tk()
root.title("Lista de Convidados")
root.resizable(False, False)

# Funções
def adicionar_convidado(li):
    if nomeConvidado.get() != "":
        li.insert("end", nomeConvidado.get())

def remover_convidado(li):
    listaDump = li.get(0, "end")
    ativo = li.get("active")

    li.delete(listaDump.index(ativo))

def limpar_convidados(li):
    li.delete(0, "end")

def salvar_convidados(li):
    with open("convidados.txt", "a") as arq:
        index = 1
        for item in li.get(0, "end"):
            arq.write(f"{index}. {item}\n")
            index += 1


# Listbox
lista = Listbox(root)

# Label
titulo = Label(root, text="Lista de Convidados", font="Times 13 italic")

# Entry
nomeConvidado = Entry(root, font="Times 12 italic")

# Buttons
adicionar = Button(root, text="Adicionar", command=lambda: adicionar_convidado(lista))
remover = Button(root, text="Remover", command=lambda: remover_convidado(lista))
limpar = Button(root, text="Limpar", command=lambda: limpar_convidados(lista))
salvar = Button(root, text="Salvar", command=lambda: salvar_convidados(lista))


# Grid
titulo.grid(row=0, columnspan=2, sticky="ew") # Lbl

lista.grid(row=1, columnspan=2, sticky="ew") # Lbox

nomeConvidado.grid(row=2, columnspan=2, sticky="ew") # Entry

adicionar.grid(row=3, column=0, sticky="e") # Btn
remover.grid(row=3, column=1) # Btn
limpar.grid(row=4, columnspan=2, sticky="ew") # Btn
salvar.grid(row=5, columnspan=2, sticky="ew") # Btn

root.mainloop()