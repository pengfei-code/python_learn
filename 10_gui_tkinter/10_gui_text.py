#multiple text

from tkinter import *
from tkinter import  messagebox
import webbrowser
class Application(Frame):
    def __init__(self,tk):
        self.__tk = tk
        super().__init__(tk)
        self.__init_tk()
        self.__init_widget()
        self.__tk.mainloop()

        pass

    def __init_tk(self):
        self.__tk.geometry("400x300+100+100")

        pass
    def __init_widget(self):
        self.btn01 = Button(self.__tk,text = "repeat insert text")
        self.btn02 = Button(self.__tk,text = "return text")
        self.btn03 = Button(self.__tk,text = "add a photoimage")
        self.btn04 = Button(self.__tk,text = "add widget")
        self.btn05 = Button(self.__tk,text = "control the text by tag")
        self.btn01.pack(side="left")
        self.btn02.pack(side="left")
        self.btn03.pack(side = "left")
        self.btn04.pack(side="left")
        self.btn05.pack(side="left")

        self.btn01.bind("<Button-1>",self.repeat_insert)
        self.btn02.bind("<Button-1>",self.return_text)
        self.btn03.bind("<Button-1>",self.add_a_photoimage)
        self.btn04.bind("<Button-1>",self.add_widget)
        self.btn05.bind("<Button-1>",self.control_text_by_tag)


        self.text = Text(self.__tk,width="50",height="20",background="#336699",foreground="purple")


        self.text.pack()
        self.text.insert(1.1,"asdfffffffffff\nabcde")
        self.text.insert(2.3,"你好")



    pass

    def repeat_insert(self,event):
        self.text.insert(INSERT,"insert")
        self.text.insert(END,"ends")
        pass
    def return_text(self,event):
        messagebox.showinfo("title",self.text.get(1.1,END))

        pass
    def add_a_photoimage(self,event):
        self.pi = PhotoImage(file="avatar.gif")
        self.text.image_create(END,image = self.pi)

        pass

    def add_widget(self,event):
        b_temp = Button(tk,text = "b_temp",background="brown")
        self.text.window_create(END,window=b_temp)

        pass
    def control_text_by_tag(self,event):

        #If you want to insert the word in the specific line,the line should better have the word

        self.text.insert(1.1,"good good")
        self.text.insert(2.1,"百度good")
        self.text.insert(3.1,"hello")
        self.text.tag_add("browser",2.1,2.3)
        self.text.tag_add("good",1.1,1.11)
        self.text.tag_configure("good",background="yellow")

        self.text.tag_add("baidu",2.1,2.3)
        self.text.tag_configure("baidu",underline=True)

        self.text.tag_bind("browser","<Button-1>",self.open_browser)


        pass
    def open_browser(self,event):
        webbrowser.open("http://www.baidu.com")

        pass


tk = Tk()
app = Application(tk)

