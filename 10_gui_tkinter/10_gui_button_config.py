from tkinter import *
from tkinter import  messagebox


class Application(Frame):
    def __init__(self,tk):
        self.__tk = tk
        super().__init__(tk)
        self.__init_tk(tk)
        self.__init_widget(tk)
        tk.mainloop()

        pass
    def __init_tk(self,tk):
        tk.geometry("400x300+100+100")
        pass

    def __init_widget(self,tk):

        self.__btn = Button(tk,width=20,height =5)
        self.__btn["text"] = "click me to show info"
        self.__btn.bind("<Button-1>",self.__btn_click)
        self.__btn.config(fg="red",anchor="nw",bg="purple")
        self.__btn.pack()


        pass
    def __btn_click(self,event):
        messagebox.showinfo("title","content")

        pass


    pass

tk = Tk()
app = Application(tk)
