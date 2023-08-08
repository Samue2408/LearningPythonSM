from turtle import *

getscreen()

bgcolor('light pink')

color('red')


begin_fill()
pensize(3)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

penup()
goto(0, 100)
pendown()
style = ('Courier', 15, 'bold')
color('white')
write('Me encantas', font=style, align='center')

penup()
goto(0, 85)
pendown()
style = ('Courier', 10, 'bold')
write('Mi princesa', font=style, align='center')

hideturtle()

done()

