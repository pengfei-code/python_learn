from tkinter import *


#optionmenu
tk = Tk()

select_sv = StringVar()
select_sv.set("百度")
om = OptionMenu(tk,select_sv,"百度","谷歌","bing")
om.pack()

def optionMenuValue():
    print(select_sv.get())

    pass

btn_aquire_om_value = Button(tk,text="aquire",fg="olive",command=optionMenuValue)
btn_aquire_om_value.pack()





tk.mainloop()

