from tkinter import Tk, Label, PhotoImage

# Frame
root = Tk()
root.title("Images")
root.resizable(False, False)

# Var
img = PhotoImage(master=root, file="images/estante.png")
root.iconphoto(False, img)

# Label
lblImage = Label(root, image=img)

# Grid
lblImage.grid()


root.mainloop()