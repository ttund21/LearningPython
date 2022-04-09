from tkinter import Button, Tk, Label, StringVar
from funcGui import Teste

# Janela
janela = Tk()
janela.title("Primeiro App")
#janela.geometry(newGeometry="600x500")
janela.resizable(width=False, height=False)

# Labels
texto = StringVar()
texto.set("Label")

legenda01 = Label(janela,
                  anchor='center',
                  textvariable=texto,
                  bg="yellow",
                  fg="green",
                  font="Times 20 bold",
                  bd=2, relief="solid",
                  )

legenda02 = Label(janela,
                  anchor='center',
                  text="Label",
                  bg="blue",
                  fg="black",
                  font="Times 20 bold",
                  bd=2, relief="solid",
                  )

legenda03 = Label(janela,
                  anchor='center',
                  text="Label",
                  bg="green",
                  fg="white",
                  font="Times 20 bold",
                  bd=2, relief="solid",
                  )

legenda01.grid(row=0, column=0)
#legenda01.pack()
legenda02.grid(row=1, column=1)
#legenda02.pack()
legenda03.grid(row=2, column=2)

# Botão
botao = Button(janela, width=5, height=1, text="Next", command=lambda: Teste.ola_mundo())
botao.grid(row=3, column=1)
#botao.pack()

#Packs

janela.mainloop()