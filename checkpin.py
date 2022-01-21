import tkinter as tk
import bcrypt
typestat = ""
salt = b'$2b$12$rgCYFuE.etnPBnQdd3fiSO'
root = tk.Tk()
root.title("Enter PIN")
root.iconbitmap("app.ico")
root.geometry("600x120")
mainlbl = tk.Label(text="Enter PIN: ......", font=("Consolas", 24))
mainlbl.pack()
mainlbl.place(x=12, y=12)
def kpress(_):
    global typestat
    if len(typestat) == 6:
        pass
    else:
        typestat += _.char
        mainlbl.config(text="Enter PIN: " + "-" * (len(typestat) - 1) + typestat[-1:] + "." * (6-len(typestat)))
        root.update()
def rmkey(_=any):
    global typestat
    typestat = typestat[:-1]
    mainlbl.config(text="Enter PIN: " + "-" * (len(typestat) - 1) + typestat[-1:] + "." * (6-len(typestat)))
    root.update()
def next(_=any):
    global typestat
    if len(typestat) != 6:
        for i in range(4):
            root.configure(background="black")
            mainlbl.configure(background="black")
            mainlbl.configure(foreground="#f0f0ed")
            root.after(80)
            root.update()
            root.configure(background="#f0f0ed")
            mainlbl.configure(background="#f0f0ed")
            mainlbl.configure(foreground="black")
            root.after(80)
            root.update()
    else:
        hashed = bcrypt.hashpw(typestat.encode(), salt).decode()
        with open("pin.data", "r") as f:
            _hashed = f.read()
        if hashed == _hashed:
            mainlbl.config(text="Unlocked. ")
            root.update()
        else:
            mainlbl.config(text="Wrong PIN. ")
            typestat = ""
            root.update()
for i in range(10):
    root.bind(str(i), kpress)
root.bind("<BackSpace>", rmkey)
root.bind("<Return>", next)
root.mainloop()