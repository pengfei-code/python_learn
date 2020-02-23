from tkinter import *
from tkinter.colorchooser import  *

tk = Tk()
lbl_color = Label(tk,text="color",width="300",height="30")
lbl_color.pack()

def show_color():
    color = askcolor(color="magenta",title="askcolor for color")
    print(color[1])
    lbl_color.config(bg = color[1])
    pass


btn_color = Button(tk,text="pick color",command=show_color)
btn_color.pack()

tk.mainloop()


