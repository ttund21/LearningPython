# Criar um formulario com nome, idade, cpf e telefone

from tkinter import Tk, Frame, Entry, Button, Label
from json import dump

# Custom widget
class CaixasFormulario(Frame):
    def __init__(self, master, boxName):
        super().__init__()

        cxName = Label(self, text=f"{boxName}:", font="Arial 15", anchor="w")
        self.cxEntrada = Entry(self)

        cxName.grid(row=0, column=0)
        self.cxEntrada.grid(row=0, column=1)


# Frame
root = Tk()
root.title("Formulario")
root.resizable(False, False)

# Funções
def salvar():
    dicio = {}

    dicio['nome'] = nome.cxEntrada.get()
    dicio['idade'] = idade.cxEntrada.get()
    dicio['cpf'] = cpf.cxEntrada.get()
    dicio['telefone'] = telefone.cxEntrada.get()

    with open("bd_formulario.json", "a") as arq:
        dump(dicio, arq)

# Corpo
nome = CaixasFormulario(root, "Nome")
idade = CaixasFormulario(root, "Idade")
cpf = CaixasFormulario(root, "Cpf")
telefone = CaixasFormulario(root, "Telefone")

btnSalvar = Button(root, text="Salvar", command=salvar)

# Pack
nome.grid(row=0, column=0, sticky="e")
idade.grid(row=1, column=0, sticky="e")
cpf.grid(row=0, column=1, sticky="e")
telefone.grid(row=1, column=1, sticky="e")

btnSalvar.grid(row=2, column=1, sticky="e")

root.mainloop()