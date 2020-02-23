#bind event

# one widget can be binded  multiple method

#1 command

from tkinter import *

tk = Tk()

def btn_command(x,y):

    print(f"x*y is : \t{x*y}")
    pass

btn_command = Button(tk, text="btn_command", command=lambda:btn_command(20, 30), fg ="dimgrey")

btn_command.pack(side="left")

#2 bind
def btn_bind_func(event):
    print(event.widget)
    pass

btn_bind = Button(tk,text="btn_bind",fg="olive")
btn_bind.bind("<Button-1>",btn_bind_func)
btn_bind.pack()
#2 bind class
def btn_class_func(event):
    print(event.widget.winfo_geometry())
    pass

tk.bind_class("Button","<Button-1>",btn_class_func)



tk.mainloop()




