#label

from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self,tk=None):
        self.__tk =  tk
        super().__init__(tk)

        self.__init_tk(self.__tk)

        self.__init_widget(self.__tk)

        self.__tk.mainloop()
        print(pi)

        pass
    def __init_tk(self,tk):
        self.pack()
        tk.title("title")
        tk.geometry("400x300+100+100")

        pass
    def __init_widget(self,tk):

        self.__lb1 = Label(tk,text = "label1",width =10,height = 3,bg = "#336699",fg = "brown")
        self.__lb1.pack()

        self.__lb2 = Label(tk,text = "label2",borderwidth="3",width=10,height=3,bg="#336699",fg="blue")
        self.__lb2.pack()

        self.__lb3 = Label(tk,text ="label3",justify="right",relief="solid",width=10,height=3,bg="#336699",fg="yellow")
        self.__lb3.pack()

        self.__lb4 = Label(tk,text = "label4",relief="groove",width=10,height=3,bg="#336699",fg="red")
        self.__lb4.pack()

        self.__lb5 = Label(tk,text="label5",relief="raised",width=10,height=3,bg="#336699",fg = "purple",font={"黑体",100})
        self.__lb5.pack()

        global pi
        pi = PhotoImage(file="avatar.gif")


        self.__lb6 = Label(tk,image=pi)
        self.__lb6.pack()



        pass

    pass

tk = Tk()
app = Application(tk)