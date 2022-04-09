from tkinter import Tk, Label, Entry, Frame

class MeuFrame(Frame):
    def __init__(self, master, labelname="Caixa"):
        super().__init__()

        # Frame
        self["relief"] = "solid"
        self["bd"] = 2

        # Label
        legenda = Label(self, text=labelname)

        # Entry
        caixa = Entry(self)

        # Pack
        legenda.grid(row=0, column=0) # Lbl
        caixa.grid(row=0, column=1) # Entry


    
# Frame

root = Tk()

frm1 = MeuFrame(root, "Nome").pack()
frm2 = MeuFrame(root, "Senha").pack()




root.mainloop()