from turtle import *

pensize(5)
getscreen()

bgcolor("black")

def go(x, y):
    penup()
    goto(x, y)
    pendown()

pencolor("#008000")
fillcolor("#00FF00")

go(0, -250)
seth(90)

begin_fill()
circle(200, 70)
circle(-200, 45)
seth(270)
circle(298, 80)
end_fill()

go(0, -250)

begin_fill()
seth(90)
circle(-200, 70)
circle(200, 45)
seth(270)
circle(-298, 80)
end_fill()

go(-10, -190)

begin_fill()
seth(90)
goto(-10, 70)
seth(0)
goto(10, 70)
seth(270)
goto(10, -190)
goto(0, -225)
goto(-10, -190)
end_fill()

pencolor("#800000")
fillcolor("#FF0000")

seth(90)
go(-80, 270)
begin_fill()
circle(-120, 45)
seth(320)
circle(-120, 45)
end_fill()

seth(90)
go(-6, 270)
begin_fill()
circle(-120, 45)
seth(320)
circle(-120, 45)
end_fill()

seth(90)
go(-45, 270)
begin_fill()
circle(-120, 45)
seth(320)
circle(-120, 45)
goto(30, 220)
end_fill()

seth(0)
go(-10, 70)
begin_fill()
goto(15, 70)
circle(71, 80)
seth(80)
circle(400, 33)
seth(225)
circle(300, 25)
end_fill()

seth(0)
go(-10, 70)
begin_fill()
circle(20, 40)
circle(60, 50)
seth(90)
circle(300, 50)
seth(250)
circle(400, 33)
circle(71, 90)
end_fill()

hideturtle()

done()