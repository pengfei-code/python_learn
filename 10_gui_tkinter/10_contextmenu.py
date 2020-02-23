#contextmenu

#implement notpad

from tkinter import *
from tkinter.filedialog import  *



class Application(Frame):
    def __init__(self,tk):
        self.__tk = tk
        super().__init__(tk)

        self.__init_tk()
        self.__init_widget()
        self.__tk.mainloop()

        pass
    def __init_tk(self):
        self.__tk.geometry("300x300+100+100")

        pass
    def save_file(self):
        savefile = asksaveasfile(filetypes=[("文本文件",".txt")])
        with savefile as ff:
            # print(self.text.get(1.1,END))
            ff.write(self.text.get(1.0,END))
        ff.close()
        # with open()

        pass
    def open_file(self):
        openfile = askopenfile()
        with  openfile as ff:
            content = ff.read()
            self.text.insert(INSERT,content)
            # self.text.insert(1.1,)
        ff.close()

        pass

    def __init_widget(self):
        #create the menu
        rootMenu = Menu(tk)

        fileMenu =Menu(rootMenu)
        fileMenu.add_command(label="打开",accelerator="ctrl+o",command=self.open_file)
        fileMenu.add_command(label="关闭",accelerator="ctrl+c",command="tk.quit")
        fileMenu.add_command(label="保存",accelerator="ctrl+s",command=self.save_file)
        rootMenu.add_cascade(label="文件(file)",menu = fileMenu)

        tk["menu"] = rootMenu

        self.text = Text(self.__tk,bg = "skyblue",width="300",height="300",fg="snow")
        self.text.pack(side="left")

        pass

    pass


tk = Tk()
tk.title("pengfei editor")
app = Application(tk)


