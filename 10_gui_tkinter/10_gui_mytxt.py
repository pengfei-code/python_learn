from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *
from tkinter.font import *
class Application(Frame):
    is_append = False
    current_font_size = 8
    is_show_font_size = False

    def __init__(self,tk):
        self.__tk = tk
        super().__init__(tk)
        self.__init_tk()
        self.__init_widget()
        self.__tk.mainloop()

        pass
    pass

    def open_file(self):
        open_file = askopenfile(initialdir="/users/songpengfei/documents",filetypes=[("文本文档",".txt")])
        with open_file as ff:
            content=ff.read()
            if not Application.is_append:
                self.text.delete(1.0,END)
            self.text.insert(INSERT,content)

        ff.close()
        pass

    def save_file(self):
        save_file = asksaveasfile(initialdir="/users/songpengfei/downloads",filetypes=[("文本文件",".txt")])
        with save_file as ff:
            content=self.text.get(1.0,END)
            save_file.write(content)
        ff.close()


        pass
    def close_file(self):
        self.__tk.destroy()
        pass


    def choice_bg_color(self):
        color = askcolor(color="magenta")
        self.text.config(bg=color[1])
        pass

    def text_click(self,event):
        print("text_click")
        self.menuRight.post(event.x_root,event.y_root)


        pass
    def choice_fore_color(self):
        print("enter fore color")
        color = askcolor(color="dimgray")
        self.text.config(fg=color[1])


        pass
    def set_is_append(self):
        Application.is_append =not Application.is_append
        if Application.is_append:
            self.menuUnknow.entryconfig(1,label="(是)append")
        else:
            self.menuUnknow.entryconfig(1,label="(否)append")

        pass
    def scale_the_font(self,value):
        newfont = Font(family='GBK', size=value,weight=BOLD,slant=ITALIC,\
             underline=1,overstrike=1)
        self.text.config(font=newfont)

        pass
    def set_font(self):
        Application.is_show_font_size = not Application.is_show_font_size

        if Application.is_show_font_size :

            self.frame_scale = Frame(self.__tk, width="300", height="50")

            scale_font = Scale(self.frame_scale, from_=8, to=50, orient=HORIZONTAL, tickinterval="5",
                               command=self.scale_the_font)

            scale_font.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=1)

            self.frame_scale.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.2)

        else:
            if self.frame_scale is not None:
                self.frame_scale.destroy()



        pass

    def __init_widget(self):
        menuRoot = Menu(self.__tk)

        self.menuFile = Menu(menuRoot)
        self.menuFile.add_command(label="保存(save)",command=self.save_file)
        self.menuFile.add_command(label="打开(open)",command=self.open_file)
        self.menuFile.add_command(label="关闭(close)",command=self.close_file)
        menuRoot.add_cascade(menu=self.menuFile,label="File(文件)")

        self.menuUnknow = Menu(menuRoot)
        self.menuUnknow.add_command(label="字体大小",command=self.set_font,accelerator="")
        self.menuUnknow.add_command(label="(否)append",command=self.set_is_append,accelerator="")
        menuRoot.add_cascade(menu=self.menuUnknow,label="更多(m)")

        tk["menu"]=menuRoot

        self.text = Text(self.__tk,bg="linen",width="300",height="300")
        self.text.pack()



        self.menuRight = Menu(menuRoot)

        self.menuRight.add_command(label="backgroundcolor",command=self.choice_bg_color)
        self.menuRight.add_command(label="foregroundcolor",command=self.choice_fore_color)

        self.text.bind("<Button-2>",self.text_click)
        self.frame_scale = None
        #scale the font


        #shortcut key

        tk.bind("<Control-s>",lambda event:self.save_file())
        tk.bind("<Control-o>",lambda event:self.open_file())
        tk.bind("<Control-d>",lambda event:self.close_file())


        pass
    def __init_tk(self):
        self.__tk.geometry("300x300+100+100")
        pass



tk = Tk()
tk.title("文本编辑器(author=fei)")
app = Application(tk)
