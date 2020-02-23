from tkinter import *

class Application(Frame):


    def __init__(self,tk):
        self.__tk = tk
        super().__init__(self.__tk)
        self.__init_tk()
        self.__init_widget()
        self.__tk.mainloop()
        pass
    def __init_widget(self):
        colorlist = ["tomato","red","orange","yellow","green","cyan","blue","purple","pink","hotpink","deeppink"]
        colorlist.extend(["bisque","brown","tan","linen","ivory","burlywood","dimgrey","grey","gray","violet","indigo","olive"])
        colorlist.extend(["skyblue","navy","peru"])

        canvas = Canvas(self.__tk,width="900",height="900",bg="white")
        for color in colorlist:
            print(color)

        x,y = 0,0

        radius = 20
        for i in range(len(colorlist)):

            canvas.create_oval(x,y,x+20,y+20,fill=colorlist[i])
            x=x+20
            y=y+20
            pass
        canvas.pack()
        









        pass

    def __init_tk(self):
        tk.geometry("900x900+100+100")
        pass

    pass

tk = Tk()
app = Application(tk)

