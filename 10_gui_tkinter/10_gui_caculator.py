from tkinter import *

class Application(Frame):
    def __init__(self,tk):
        self.__tk =tk
        self.__init_tk()
        self.__init_widget()
        self.__tk.mainloop()

        pass
    def __init_tk(self):
        # self.__tk.geometry("160x300+100+100")
        pass
    def __init_widget(self):
        tp_widgets = (
            ("MC","M+","M-","MR"),
            ("C","+","/","x"),
            ("7","8","9","-"),
            ("4","5","6","+"),
            ("1","2","3","="),
            ("0",".")

        )

        for i,row_widget in enumerate(tp_widgets):
            for j,wid in enumerate(row_widget):
                btn = Button(self.__tk,text=wid)
                btn.config(relief="groove")

                entry_input = Entry(self.__tk, bg="tan")
                entry_input.grid(row=0, column=0, columnspan=4)
                if i==0:
                    btn.grid(row=i + 1, column=j, ipadx=6)
                    btn.config(bg="skyblue")
                elif wid =="0":
                    btn.grid(row = 6,column = 0,columnspan=2,sticky = NSEW)
                    pass
                elif wid ==".":
                    btn.grid(row =6,column=2)
                    pass
                elif wid =="=":
                    btn.grid(row=5,column=3,rowspan=2,sticky=NSEW)
                    pass
                else:
                    btn.grid(row=i+1, column=j,ipadx=6)

                    pass
                pass
            pass


        pass

    pass


tk = Tk()

app = Application(tk)