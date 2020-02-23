from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self,tk = None):
        self.tk = tk
        super().__init__(tk)
        self.__init_tk(tk)
        self.__init_widget(tk)
        tk.mainloop()


        pass
    def __init_tk(self,tk=None):
        self.pack()
        tk.title("tk title")
        tk.geometry("400x300+100+100")



        pass

    def __init_widget(self,tk=None):
        btn01 = Button(tk)
        btn01["text"] = "click me"
        btn01.bind("<Button-1>",self.__btn01_click)
        btn01.pack()

        pass

    def __btn01_click(self,event):
        messagebox.showinfo("msg title","msg content")
        print("btn01_click")
        pass

    pass

tk = Tk()

app = Application(tk)

