import math
from turtle import *


def xt(t):
    return 16*math.sin(t)**3

def yt(t):
    return 13*math.cos(t)-5*\
            math.cos(2*t)-2*\
            math.cos(3*t)-\
            math.cos(4*t)


speed(10000)
bgcolor('black')





for i in range(800):
    goto((xt(i)*20), yt(i)*20)
    pencolor('red')
    goto(0, 0)

penup()
goto(0, 0)
pendown()
style = ('Courier', 38, 'bold')
color('white')
write('Te quiero mucho', font=style, align='center')

penup()
goto(0, -25)
pendown()
style = ('Courier', 20, 'bold')
write('Mi princesa', font=style, align='center')

pencolor('red')
done()