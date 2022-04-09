from tkinter import Label, Tk, IntVar, Checkbutton


# Frame
root = Tk()
root.title("Check Button")
root.resizable(False, False)

# Btn
checkValue = IntVar()
check = Checkbutton(root, text="Primeiro", variable=checkValue)

# Label
legenda = Label(root, text="Check Buttons:")
status = Label(root, textvariable=checkValue)

# Grid
legenda.grid(row=0, column=0) # Lbl
check.grid(row=1, columnspan=2, sticky="ew") # ChkBtn
status.grid(row=3, columnspan=2, sticky="ew") # Lbl


root.mainloop()