from tkinter import *

from tkinter import messagebox

class Application(Frame):
    def __init__(self,tk):
        self.__tk = tk

        self.__init_tk()
        self.__init_widget()

        self.__tk.mainloop()


        pass

    def __init_tk(self):
        self.__tk.geometry("400x300+100+100")
        pass

    def __init_widget(self):
        self.sexSV = StringVar()
        self.sexSV.set("f")

        self.rb_m = Radiobutton(self.__tk,value="m",text="男",variable=self.sexSV)
        self.rb_f = Radiobutton(self.__tk,value="f",text = "女",variable=self.sexSV)
        self.rb_f.pack()
        self.rb_m.pack()

        btn_sex = Button(tk,text="aquire the sex")
        btn_sex.bind("<Button-1>",self.aquire_sex)
        btn_sex.pack()

        self.label = Label(self.__tk,text="hobby",background = "purple" ,foreground= "white")
        self.label.pack()

        self.hobby1 = IntVar()
        self.hobby2 = IntVar()
        self.hobby1.set("0")
        self.hobby2.set("0")

        self.hobby_cb1 = Checkbutton(self.__tk,onvalue=1 ,offvalue= 0 ,variable=self.hobby1,text="basketball")
        self.hobby_cb2= Checkbutton(self.__tk,onvalue=1 ,offvalue=0,variable=self.hobby2,text="music")

        self.hobby_cb1.pack()
        self.hobby_cb2.pack()

        self.btn_hobby = Button(self.__tk,text = "aquire hobby")
        self.btn_hobby.bind("<Button-1>",self.aquire_hobby)
        self.btn_hobby.pack()


        pass

    def aquire_sex(self,event):
        messagebox.showinfo("sex",self.sexSV.get())


        pass
    def aquire_hobby(self,event):
        hobby_str = []

        if self.hobby1.get()==1:
            hobby_str.append("basket")
        if self.hobby2.get()==1:
            hobby_str.append("music")


        messagebox.showinfo("hobby",f"the hobby is {hobby_str}")

    pass

tk = Tk()
app = Application(tk)