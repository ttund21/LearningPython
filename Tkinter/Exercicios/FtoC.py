# Transformar Farenheit para Celsius

from tkinter import Tk, Label, Entry, Button

root = Tk()
root.title("FtoC")

# Função
def farenheit_celsius(farenheit):
    celsius = (float(farenheit) - 32) / 1.8
    saida["text"] = f"Celsius: {round(celsius, 2)}"

# Label
legenda = Label(root, text="Farenheit:")
saida = Label(root, pady=4)

# Entry
entrada = Entry(root)

# Button
botao = Button(root, text="Executar", command=lambda: farenheit_celsius(entrada.get()))

# Packing
legenda.grid(row=0)
saida.grid(row=2)

entrada.grid(row=1)

botao.grid(row=3)


root.mainloop()