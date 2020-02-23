from tkinter import *

tk = Tk()

tk.geometry("600x600+100+100")
fra = Frame(tk,width="300",height="300",bg="indigo")
fra.pack()

btn_china = Button(fra,text="中国")

btn_china.place(relx=0.1,rely=0.1,relwidth=0.2,relheight=0.3)

lbl_england = Label(tk,text="英格兰",fg="cyan",background="navy")

lbl_england.place(relx=0.9,rely=0.9,relwidth=0.1,relheight=0.1)

lbl_peru = Label(tk,text="秘鲁",bg ="peru")
lbl_peru.place(relx=0.0,rely=0.0,relwidth=0.1,relheight=0.1)

lbl_wood = Label(tk,text="实木",bg="burlywood")
lbl_wood.place(relx=0.9,rely=0.0,relwidth=0.1,relheight=0.1)

lbl_bisque = Label(tk,text="黄褐色",bg="bisque")
lbl_bisque.place(relx=0.0,rely=0.9,relwidth=0.1,relheight=0.1)

lbl_violet = Label(tk,text="紫罗兰",bg="violet")
lbl_violet.place(relx=0.45,rely=0.45,relwidth=0.1,relheight=0.1)




tk.mainloop()



