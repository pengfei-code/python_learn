
#lambda args:expression
#lambda x,y:x*y

#you must treat the lambda as a function

# have args

t = lambda x,y:x*y


print(t(2,3))


def add(x,y):
    return x+y
    pass

#no args
t = lambda:add(2,3)

print(t())


#any args

def sum(*kwargs):
    print(kwargs)
    pass


sum(1,2,3,4)
from tkinter import *

tk = Tk()
def btn_click(num):
    print(f"btn is clicked{num}")
    pass

btn = Button(tk,command = btn_click(32),text="click me",fg = "skyblue")
btn.pack()

#use the lambda

btn_lambda = Button(tk,command=lambda:btn_click(44),text="lambda",fg ="cyan")
btn_lambda.pack()
tk.mainloop()


