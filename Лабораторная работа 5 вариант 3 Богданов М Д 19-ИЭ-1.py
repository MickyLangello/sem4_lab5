"""
 - образная фигура перемещается сверху вниз на 400 пикселей со
скоростью 25 пикселей/сек. и шагом в 1 пиксель, а прямая в это
время вращается по часовой стрелке со скоростью 200/сек. и шагом
в 1 градус относительно собственного центра. Запуск/остановка
движения – двойной щелчок мыши.
"""

from tkinter import *
from time import *
from math import *

root = Tk()
root.resizable(0, 0)
root.geometry('504x854+80+80')
root.title('Лабораторная работа №4')


X = 250
Y = 250
flag = 1

def stop(*args):
    #print("stop")
    c.update()
    sleep(0.2)
    c.unbind('<Double-Button-1>')
    c.bind('<Double-Button-1>', start)
    stop()

def start(*args):
    #print("start")
    global flag, x1, x2, y1, y2, L, angle
    c.unbind('<Double-Button-1>')
    sleep(0.04) # =1/25
    c.bind('<Double-Button-1>', stop)
    if (flag==1):
        c.move("oval", 0, 1)
        c.move("line1", 0, 1)
        c.move("line2", 0, 1)
        y1+=1
        y2+=1
    if (c.coords("oval")[1]==480):
        flag=0
        
    if (flag==0):
        c.move("oval", 0, -1)
        c.move("line1", 0, -1)
        c.move("line2", 0, -1)
        y1-=1
        y2-=1
    if (c.coords("oval")[1]==80):
        flag=1
    
    for i in range (8): # =200/25
        angle+=1 #шаг
        
        angle+=180
        rad=angle*pi/180
        xNew1=x1+130+L*cos(rad)
        yNew1=y1+130+L*sin(rad)
        c.coords("line1", x1+130, y2-130, xNew1, yNew1)
    
        angle-=180
        rad=angle*pi/180
        xNew2=x1+130+L*cos(rad)
        yNew2=y1+130+L*sin(rad)
        c.coords("line2", x2-130, y2-130, xNew2, yNew2)
    
    c.update()
    start()

           

x1=120
y1=80
x2=380
y2=340
L = sqrt(33800) #гипотенуза по Пифагору
angle=-225

c = Canvas(width = 500, height = 850, bg = 'lightgrey')
c.place(x = 0, y = 0)
c.create_oval(x1, y1, x2, y2, tag = 'oval')
c.create_line(x1, y2, x2-130, y1+130, tag = 'line1')
c.create_line(x1+130, y2-130, x2, y1, tag = 'line2')

c.bind('<Double-Button-1>', start)

root.mainloop()

