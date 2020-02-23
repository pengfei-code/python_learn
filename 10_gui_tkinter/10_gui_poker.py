from tkinter import *

#If you want to install the Pillow ,you may need to install zlib with brew

from PIL import Image,ImageTk

# from tkinter import event





tk = Tk()
tk.geometry("500x500+100+100")

#1 spade
#2 heart
#3 club
#4 diamond

frame_crop_show = Frame(tk,width="1000",height="500",bg="violet")
frame_crop_show.pack()

pi_original = PhotoImage(file="poker.gif")

label_original = Label(frame_crop_show,image = pi_original)
label_original.place(relx=0.3,rely=0.1)

poker_strs,poker_strs_1,poker_strs_2,poker_strs_3,poker_strs_4,poker_strs_5=[],[],[],[],[],[]

poker_strs_1.extend(["s3","22","32","43","54","64","73","81","92","t4","j4"])
poker_strs_2.extend(["s1","23","33","41","51","61","74","84","91","t2","j1"])
poker_strs_3.extend(["s2","21","31","44","52","62","71","83","94","t3","j3"])
poker_strs_4.extend(["s4","24","34","44","53","63","72","82","93","t1","j2"])
poker_strs_5.extend(["q1","q3","q2","q4","k2","k4","k3","k1","e2","e1"])

poker_strs.append(poker_strs_1)

poker_strs.append(poker_strs_2)

poker_strs.append(poker_strs_3)

poker_strs.append(poker_strs_4)

poker_strs.append(poker_strs_5)


poker_img = Image.open("poker.gif")

t = poker_img.size

top_border = 6
row_border = 5

column_middle_gap = 3
row_middle_gap = 6

poker_width = 51
poker_height = 76
poker_interval = 20

pi_crops = []


poker_imgs = []


for row in range(5):
    pi_row = []
    if row <4:
        for column in  range(11):
                # column = 10
                img_x = row_border + column_middle_gap * (column) + column * poker_width
                img_y = top_border+row_middle_gap*(row) + row*poker_height
                img_x1 = img_x+51
                img_y1 = img_y+76
                # img_crop = poker_img.crop((img_x, img_y, img_x1, img_y1))
                img_crop = poker_img.crop((img_x, img_y, img_x1, img_y1))

                poker_pi = ImageTk.PhotoImage(img_crop)
                pi_row.append(poker_pi)

                lbl = Label(frame_crop_show,image=poker_pi)
                lbl.pack()
                lbl.place(x=column + column * poker_interval,y=5+row*poker_height)

                sv = StringVar()
                sv.set( poker_strs[row][column])
                poker_pi.sv = sv

                poker_imgs.append(poker_pi)
                pi_crops.append(pi_row)

                pass
    else:
        print(row)
        column_middle_gap = column_middle_gap + 6
        row_border = row_border + 2
        for column in range(10):
            img_x = row_border + column_middle_gap * (column) + column * poker_width

            img_y = top_border + row_middle_gap * (row) + row * poker_height

            img_x1 = img_x + 51
            img_y1 = img_y + 75

            # print(f"(img_x,img_y) (img_x1),(img_y1) is ({img_x},{img_y},{img_x1},{img_y1})")

            # img_crop = poker_img.crop((img_x, img_y, img_x1, img_y1))
            img_crop = poker_img.crop((img_x, img_y, img_x1, img_y1))
            poker_pi = ImageTk.PhotoImage(img_crop)
            pi_row.append(poker_pi)
            lbl = Label(frame_crop_show,image =poker_pi)

            lbl.pack()
            lbl.place(x=column + column * poker_interval, y=5 + row * poker_height)
            sv = StringVar()
            sv.set(poker_strs[row][column])

            poker_pi.sv = sv

            poker_imgs.append(poker_pi)
            # lbl.place(x=20, y=5 + row * poker_height)




            pi_crops.append(pi_row)
            pass
        pass
    pass

lbl_tip = Label(tk,text ="shufle the poker and deal cards",background="skyblue",foreground="snow")
lbl_tip.pack()
import random







# for x in poker_lbls:
#     print(x.sv.get())

frame_shuffle = Frame(tk,bg = "black",width="900",height="200")
frame_shuffle.pack()

def poker_click(e):
    x =e.x
    y=e.y
    wid = e.widget
    print(e.widget.winfo_geometry())
    print(e.widget.winfo_x())
    print(e.widget.winfo_y())
    if wid.winfo_y()==40:
        wid.place(x=wid.winfo_x(),y=wid.winfo_y()-10)
    else:
        wid.place(x=wid.winfo_x(),y=40)

    pass


def create_shuffle_poker():
    for i in range(14):
        print(poker_imgs[i].sv.get())
        pi = poker_imgs[i]

        lbl_shuffle = Label(frame_shuffle, image=pi)
        lbl_shuffle.place(x=300 + i * 20, y=40)
        lbl_shuffle.bind("<Button-1>", poker_click)

    pass


def shuffle_poker(e):
    list_value =[]
    for key,value in frame_shuffle.children.items():
        # item[1].destroy()
        # print(value)
        list_value.append(value)
        # value.destroy()
    for value in list_value:
        value.destroy()

    random.shuffle(poker_imgs)
    create_shuffle_poker()


    pass

lbl_tip.bind("<Button-1>",shuffle_poker)



tk.mainloop()




