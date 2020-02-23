#use turtle to draw many concentric circles

# import turtle
#
# pen  = turtle.Pen()
#
#
# pen.goto((0,0))
# # init the data
# radius = 8
# increment = 10
# point_circle_center = (0,0)
# point_circle_draw = (0,point_circle_center[1]-radius)
# colors = ("red","blue","yellow","green","gray","black")
# pen.width(3)
# pen.speed(0.2)
# for count in range(0,100):
#     pen.penup()
#     pen.goto(point_circle_draw[0],point_circle_draw[1]-count*increment)
#     pen.pendown()
#     pen.color(colors[count%(len(colors))])
#     pen.circle(radius+increment*count)
#
#
# turtle.done()

#draw a chessboard

import turtle

pen = turtle.Pen()

start_point = (-200,200)

chessboard_width  = 400
chessboard_gap_width = 20

chessboard_lines = 21
pen.speed(10)
pen.width = 3
colors = ("red","black","yellow","gray","green","pink","purple","brown","orange","silver")
for  count in range(0,chessboard_lines):
    # draw the row
    pen.penup()
    start_row_point = (start_point[0],start_point[1]-count*chessboard_gap_width)
    pen.goto(start_row_point)
    pen.color(colors[count%len(colors)])
    pen.pendown()
    pen.goto(start_row_point[0]+chessboard_width,start_row_point[1])

    # draw the column
    pen.penup()
    start_column_point =(start_point[0]+count*chessboard_gap_width,start_point[1])
    pen.goto(start_column_point)
    pen.pendown()
    pen.goto(start_column_point[0],start_column_point[1]-chessboard_width)


