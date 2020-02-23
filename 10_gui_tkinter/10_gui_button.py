#gui graphics user interface
from tkinter import *
root = Tk()

def btn_click():
    m = Message(root,text = "This is a message")
    print("hello world!")
    print(Button.mro())
    pass



btn01 = Button(root)
btn01["text"] = "click me"
btn01.pack()

def btn_click1(event):
    print("ted")
    pass

# btn01.bind("<Button-1>",btn_click1())

btn01.bind(sequence = "<Button-1>",func=btn_click1)

root.mainloop()



# btn01.bind(command=btn_click)
# print("thank you")











