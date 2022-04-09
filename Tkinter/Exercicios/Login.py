# Criar uma tela de login
from tkinter import Tk, Label, Button, Entry


# Frame
janela = Tk()
janela.title("Login")

# Legendas
login = Label(janela,
              text="Login:",
              font="Times, 15",
              anchor="w")

password = Label(janela,
                 text="Password:",
                 font="Times, 15")

# Botões
loginBtn = Button(janela, text="Login", anchor="center")

# Caixa de entrada
loginBox = Entry(janela)
passwordBox = Entry(janela)

# Packing
login.grid(row=0, column=0, sticky="w")
password.grid(row=1, column=0, sticky="w")

loginBtn.grid(row=2, column=1, sticky="e")

loginBox.grid(row=0, column=1)
loginBox.focus()
passwordBox.grid(row=1, column=1)

janela.mainloop()