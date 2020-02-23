from tkinter import *

tk = Tk()

canvas = Canvas(tk,width="300",height="300",bg="tan")
canvas.pack()




#bind the handler

#the left mouse button

def mouse_left(event):
    print("the left mouse button was clicked")
    print(f"event widget:{event.widget}")
    pass

canvas.bind("<Button-1>",mouse_left)


#the mouse motion

def mouse_motion(event):
    canvas.create_oval(event.x,event.y,event.x+1,event.y+1,fill="ivory")

    pass
canvas.bind("<B1-Motion>",mouse_motion)



#the key press

def key_press(event):
    print(f"keycode is {event.keycode}\tkeysym is {event.keysym}\t char is {event.char}")
    pass

tk.bind("<KeyPress>",key_press)


tk.mainloop()




