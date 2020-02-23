from tkinter import *
from tkinter.messagebox import *

tk = Tk()

def show_info():
    print("enter")
    info = showinfo(message="hello")
    print(info)
    pass

btn = Button(tk,text="show info",command=lambda:show_info())
btn.pack()

tk.mainloop()


