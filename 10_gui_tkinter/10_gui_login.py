from tkinter import *
from tkinter import messagebox

class Application(Frame):

    def __init__(self,tk):
        self.__tk = tk
        super().__init__(self.__tk)
        self.__init_tk()
        self.__init_widget()

        self.__tk.mainloop()


        pass

    def __init_tk(self):
        self.__tk.geometry("400x300+100+100")

        pass

    def __init_widget(self):
        self.label_username = Label(tk,text = "用户名")
        self.label_username.pack()
        self.entry_username = Entry(tk)
        self.entry_username.pack()
        self.username_sv = StringVar()
        self.username_sv.set("admin")
        self.entry_username.config(textvariable=self.username_sv)

        self.label_pwd = Label(tk,text = "密码")
        self.label_pwd.pack()

        self.pwd_sv = StringVar()

        self.entry_pwd = Entry(tk)
        self.entry_pwd.pack()
        self.entry_pwd.config(show="*",background="purple",textvariable=self.pwd_sv)




        self.btn_login = Button(tk,text = "登录")
        self.btn_login.pack()
        self.btn_login.bind("<Button-1>",self.login)
        pass
    def login(self,event):
        username = self.entry_username.get()
        pwd = self.entry_pwd.get()

        print(f"username:{username},pwd :{pwd}")

        print(f"username:{self.username_sv.get()},pwd :{self.pwd_sv.get()}")

        if username == "songpengfei" and pwd == "123456":

            messagebox.showinfo("login success","congratulation to you")
        else:
            messagebox.showinfo("login failed","I am so sorry")
        pass
    pass

tk = Tk()
app = Application(tk)