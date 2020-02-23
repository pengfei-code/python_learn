from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self,tk):
        self.__tk = tk
        self.__init_tk()
        self.__init_widget()
        self.__tk.mainloop()


        pass
    def __init_widget(self):
        self.canvas = Canvas(self.__tk,width="600",height="600",bg ="pink")
        self.canvas.pack()
        self.canvas.create_line(10,10,40,40,80,80,fill="purple",dash=(4,4),width=5)
        self.canvas.create_line(20,20,50,70,90,100,fill="yellow",width=7)
        self.canvas.create_line(30,30,79,105,fill="purple",width=10)

        self.canvas.create_rectangle(30,30,50,50,fill="cyan",outline ="red")
        self.canvas.create_rectangle(70,70,90,90,fill="grey")
        self.canvas.create_rectangle(100,100,120,120,fill="gray")
        self.canvas.create_rectangle(125,125,145,145,fill="olive")
        self.canvas.create_rectangle(150,150,170,170,fill="green")
        self.canvas.create_rectangle(150,150,170,170,fill="skyblue")
        self.canvas.create_rectangle(170,170,190,190,fill="deepskyblue")

        self.canvas.create_oval(260,260,400,400,fill="hotpink")
        self.canvas.create_rectangle(170,190,190,210,fill="dimgrey")
        self.canvas.create_rectangle(170,210,190,230,fill="linen")
        self.canvas.create_rectangle(170,230,190,250,fill="bisque")
        self.canvas.create_rectangle(170,250,190,270,fill="tan")

        self.canvas.create_rectangle(170,270,190,290,fill="lime")
        self.canvas.create_rectangle(170,290,190,310,fill="green")
        self.canvas.create_rectangle(170,310,190,330,fill="yellow")

        self.canvas.create_rectangle(170,330,190,350,fill="blue")
        self.canvas.create_rectangle(170,350,190,370,fill="indigo")
        self.canvas.create_rectangle(170,370,190,390,fill="purple")


        self.canvas.create_rectangle(170,390,190,410,fill="burlywood")
        self.canvas.create_rectangle(170,410,190,430,fill="tan")


        self.canvas.create_rectangle(170,430,190,450,fill="violet")
        self.canvas.create_rectangle(170,450,190,470,fill="indigo")




        global pi
        pi = PhotoImage(file="avatar.gif")

        self.canvas.create_image(450,450,image=pi)


        self.canvas.create_rectangle(100,100,120,120,fill="mediumblue")




        pass

    def __init_tk(self):
        self.__tk.geometry("600x600+100+100")
        pass

    pass

tk = Tk()
app = Application(tk)

