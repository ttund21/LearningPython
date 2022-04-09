# Fazer uma caixa que mostre a entrada do usuário

from tkinter import Tk, Entry, Label, Button

# Frame
root = Tk()
root.title("Caixa")

# Funções
def executar():
    saida["text"] = entrada.get()

# Legendas
info = Label(root, text="Texto:", font="Times 15 italic")
saida = Label(root, font="Times 15 italic bold")

# Caixa de entrada
entrada = Entry(root)

# Botões
botao = Button(root, text="Executar", command=executar)

# Packing
info.grid(row=0, column=0, sticky="w")
saida.grid(row=1, columnspan=2, sticky="ew")

entrada.grid(row=0, column=1)

botao.grid(row=2, columnspan=2, sticky="ew")

root.mainloop()