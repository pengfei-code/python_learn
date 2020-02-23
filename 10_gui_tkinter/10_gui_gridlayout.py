from tkinter import *


class Application(Frame):
    def __init__(self,tk):
        self.__tk = tk
        super().__init__()
        self.__init_tk()
        self.__init_widget()
        self.__tk.mainloop()

        pass
    def __init_widget(self):

        self.lbl_login = Label(self.__tk,text="login",foreground="snow",bg="skyblue",width=30)
        self.lbl_login.grid(columnspan=3,sticky=EW)

        self.lbl_username = Label(self.__tk,text="username:",bg="ivory",foreground="violet")
        self.lbl_username.grid(row=1,column=0)

        username_sv=StringVar()

        self.entry_username = Entry(self.__tk,textvariable=username_sv)
        self.entry_username.grid(row=1,column=1)

        self.lbl_username= Label(self.__tk,text="password:",bg="ivory",foreground="violet")
        self.lbl_username.grid(row=2,column=0)

        password_sv = StringVar()

        self.entry_pwd = Entry(self.__tk,textvariable=password_sv,show="*")
        self.entry_pwd.grid(row=2,column=1)

        self.lbl_image =Label(self.__tk)

        global pi
        pi = PhotoImage(file="avatar.gif")
        pi = pi.subsample(5,5)



        self.lbl_image.config(image=pi)
        self.lbl_image.grid(row = 1,column=2,rowspan=2)

        pass

    def __init_tk(self):
        self.__tk.geometry("400x300+100+100")

    pass

tk = Tk()
app = Application(tk)