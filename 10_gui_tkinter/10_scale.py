from tkinter import *


#scale

tk = Tk()

lbl_show = Label(tk,text="hello world 大家好",fg="ivory",bg = "indigo")
lbl_show.pack()

def scale_font(t):
    newfont= ("宋体",f"{t}")
    print(newfont)
    lbl_show.config(font=newfont)
    pass

scale = Scale(tk,from_=50,to=100,tickinterval=5,length=200,orient=VERTICAL,command=scale_font)

scale.pack()
tk.mainloop()