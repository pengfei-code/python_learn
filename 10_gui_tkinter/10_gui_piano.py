from tkinter import *

#create mutiple button


tk = Tk()
btn_text_list = ["流行风","中国风","日本风","重金属","轻音乐"]

tk.geometry("300x700+100+100")

frame_btn = Frame(tk)
frame_btn.pack()

frame_piano = Frame(tk)
frame_piano.pack()


for btn_text in btn_text_list:
    btn = Button(frame_btn,text=btn_text,fg="cyan")
    btn.pack(side = "left",fill="y")
    pass

for x in  range(15):
    lbl = Label(frame_piano,relief="groove",bg="black" if x%2==0 else "snow",width=4,height=15)
    lbl.pack(side="left",fill="y")


tk.mainloop()