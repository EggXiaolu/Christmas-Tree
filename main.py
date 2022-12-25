import random
from playsound import playsound
from turtle import *
import pygame

import pygame

file = r'MerryChristmas.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()

# playsound('MarryChristmas.mp3')
width, height = 500, 600
title("Merry Christmas")
screen = Screen()  # 创建窗口对象
screen.setup(width, height)  # 设置窗口的宽高
screen.delay(0)  # 设置无延时绘画
screen.bgcolor('black')
colormode(255)
pencolor(0, 140, 0)
pensize(10)
penup()
# hideturtle()
goto(0, 150)
pendown()
shape(name="classic")

colors = ["purple", "red", "blue", "orange"]


def dots(radius):
    pencolor(colors[random.randint(0, 3)])
    dot(radius)
    pencolor(0, 140, 0)


# 1
seth(-120)
for i in range(10):
    fd(12)
    right(2)
penup()
goto(0, 150)
seth(-60)
pendown()
for i in range(10):
    fd(12)
    left(2)

dots(20)
penup()
fd(10)
seth(-155)
fd(10)
pendown()
for i in range(3):
    for j in range(5):
        fd(10)
        right(15)
    dots(20)
    seth(-154)
    penup()
    fd(8)
    pendown()
penup()

# 2
penup()
goto(-55, 34)
pendown()
seth(-120)
for i in range(10):
    fd(8)
    right(5)
penup()
goto(55, 34)
seth(-60)
pendown()
for i in range(10):
    fd(8)
    left(5)
dots(20)
penup()
fd(10)
seth(-145)
fd(5)
pendown()
for i in range(4):
    for j in range(5):
        fd(12)
        right(15)
    dots(20)
    penup()
    fd(8)
    seth(-145)
    pendown()

# 3
penup()
goto(-90, -35)
seth(-120)
pendown()
for i in range(10):
    fd(7)
    right(4)
penup()
goto(90, -35)
seth(-50)
pendown()
for i in range(10):
    fd(7)
    left(4)

dots(20)
penup()
fd(5)
seth(-150)
fd(10)
pendown()
for i in range(5):
    for j in range(5):
        fd(11)
        right(12)
    dots(20)
    penup()
    fd(8)
    seth(-151)
    pendown()
# 4
penup()
goto(-110, -95)
seth(-130)
pendown()
for i in range(7):
    fd(11)
    right(5)
penup()
goto(110, -95)
seth(-50)
pendown()
for i in range(7):
    fd(11)
    left(5)
dots(20)
penup()
seth(-120)
fd(5)
seth(-145)
pendown()
for i in range(6):
    for j in range(6):
        fd(9)
        right(12)
    dots(20)
    penup()
    fd(9)
    seth(-145)
    pendown()
# 5
colormode(255)
pencolor(128, 64, 0)
penup()
goto(-70, -155)
seth(-85)
pendown()
for i in range(3):
    fd(5)
    left(3)
penup()
goto(70, -155)
seth(-95)
pendown()
for i in range(3):
    fd(5)
    right(3)
seth(-170)
penup()
fd(10)
pendown()
for i in range(10):
    fd(12)
    right(2)

# 6
pencolor('white')


def guest(x, y, z):
    penup()
    goto(x, y)
    seth(-z)
    pendown()
    for angel in range(5):
        fd(10)
        right(10)


def guet(x, y, z):
    penup()
    goto(x, y)
    seth(-z)
    pendown()
    for angel in range(5):
        fd(10)
        left(10)


def qu(x, y, z):
    penup()
    goto(x, y)
    seth(-z)
    pendown()
    for angel in range(5):
        fd(6)
        right(10)
    seth(-150)
    fd(20)


#
def hdj(x, y):
    penup()
    goto(x, y)
    seth(80)
    pendown()
    pensize(2)
    circle(5)
    seth(10)
    fd(15)
    seth(120)
    fd(20)
    seth(240)
    fd(20)
    seth(180)
    fd(20)
    seth(-60)
    fd(20)
    seth(50)
    fd(20)
    seth(-40)
    fd(30)
    seth(-130)
    fd(5)
    seth(135)
    fd(30)
    seth(-60)
    fd(30)
    seth(-150)
    fd(6)
    seth(110)
    fd(30)


def uit(x, y):
    penup()
    goto(x, y)
    pendown()
    pensize(2)
    circle(5)
    seth(-10)
    fd(15)
    seth(90)
    fd(15)
    seth(200)
    fd(15)
    seth(160)
    fd(15)
    seth(-90)
    fd(15)
    seth(10)
    fd(15)
    seth(-60)
    fd(20)
    seth(-180)
    fd(5)
    seth(110)
    fd(20)
    seth(-90)
    fd(20)
    seth(-180)
    fd(6)
    seth(70)
    fd(15)
    hideturtle()


def yut(x, y, z):
    penup()
    goto(x, y)
    pendown()
    seth(z)
    for po in range(5):
        fd(4)
        left(36)


def ytu(x, y, z):
    penup()
    goto(x, y)
    pendown()
    seth(z)
    for kk in range(5):
        fd(4)
        left(36)


# 小蝴蝶结
pencolor("pink")
seth(0)
uit(40, -160)
hdj(-80, -120)
yut(-67, -115, 120)
yut(-86, -123, 150)
hdj(40, -50)
yut(52, -45, 130)
yut(34, -55, 160)
seth(0)
uit(-20, -60)
ytu(-4, -60, 100)
ytu(-20, -60, 120)
hdj(-30, 20)
yut(-15, 25, 130)
yut(-40, 20, 180)
uit(30, 70)
ytu(45, 70, 100)
ytu(30, 70, 120)


def koc(x, y, s_seth, size):
    seth(s_seth)
    pensize(2)
    pencolor("yellow")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    fillcolor("yellow")
    for i in range(5):
        left(72)
        fd(size)
        right(144)
        fd(size)
    end_fill()


# 星星
koc(-30, 100, -15, random.randint(8, 12))
koc(10, 90, 10, random.randint(8, 12))
koc(30, 30, -10, random.randint(8, 12))
koc(-70, 0, 30, random.randint(8, 12))
koc(-80, -60, 0, random.randint(8, 12))
koc(0, -70, 20, random.randint(8, 12))
koc(80, -50, 10, random.randint(8, 12))
koc(-120, -120, 0, random.randint(8, 12))
koc(-10, -120, 20, random.randint(8, 12))
koc(90, -110, 10, random.randint(8, 12))
koc(0, 150, 144, 20)


# 爱心
# def heart(x, y, size):
#     pu()
#     pencolor("red")
#     fillcolor("red")
#     goto(x, y - size / (2 ** 0.5))
#     seth(45)
#     pd()
#     begin_fill()
#     fd(size)
#     circle(size / 2, 180)
#     seth(135)
#     circle(size / 2, 180)
#     fd(size)
#     end_fill()
#     pu()
#
#
# heart(0, 150, 50)
# 袜子
seth(-20)
pensize(2)
penup()
goto(-20, 80)
pencolor("black")
begin_fill()
fillcolor("white")
pendown()
fd(25)
circle(4, 180)
fd(25)
circle(4, 180)
end_fill()
penup()
goto(-15, 80)
pendown()
begin_fill()
fillcolor("red")
seth(-120)
fd(20)
seth(150)
fd(5)
circle(7, 180)
fd(15)
circle(5, 90)
fd(30)
seth(160)
fd(18)
end_fill()
penup()
seth(0)
goto(100, -230)
pendown()
pencolor("white")


def snow():
    hideturtle()
    speed(100)
    pensize(2)
    for i in range(50):
        pencolor("white")
        penup()
        setx(random.randint(-350, 350))
        sety(random.randint(-300, 300))
        pendown()
        dens = random.randint(5, 10)
        snowsize = random.randint(5, 8)
        for j in range(dens):
            forward(snowsize)
            backward(snowsize)
            right(360 / dens)


class Snow:
    def __init__(self, x, y, size):
        self.size = size  # 雪花大小
        self.speed = size * 3  # 移动速度根据大小变化
        t = Turtle(visible=False, shape='circle')
        t.shapesize(size, size)
        t.pencolor("white")
        t.fillcolor("white")
        t.penup()
        self.snow = t.clone()
        self.snow.goto(x, y)
        self.snow.showturtle()


def move(self):
    self.snow.sety(self.snow.ycor() - self.speed)


def moveTo(self, x, y):
    # 隐藏形状后再移动防止看到移动轨迹
    self.snow.hideturtle()
    # 移动到指定位置
    self.snow.goto(x, y)
    # 恢复显示
    self.snow.showturtle()


def main():
    snows = []
    for i in range(100):
        snow = Snow(random.randint(-width / 2, width / 2),
                    height + random.randint(1, height), random.random())
        snows.append(snow)
    while True:
        for snow in snows:
            move(snow)
            if snow.snow.ycor() < -height / 2:
                moveTo(snow, random.randint(-width / 2, width / 2),
                       height + random.randint(1, height))


# 创建雪地函数
def ground(ground_line_count):  # 雪地个数
    hideturtle()
    speed(600)
    for i in range(ground_line_count):
        pensize(random.randint(5, 10))
        x = random.randint(-400, 350)
        y = random.randint(-200, -180)
        pencolor("white")  # 颜色为白色基调
        penup()
        goto(x, y)  # 让画笔移动到 x,y位置
        pendown()
        forward(random.randint(40, 100))  # 眼当前画笔方向向前移动40~100距离


snow()
ground(50)  # 调用雪地函数
color("dark red")  # 定义字体颜色
penup()
goto(0, -260)
write("Merry Christmas", align="center", font=("Comic Sans MS", 40, "bold"))  # 定义文字、位置、字体、大小
goto(25, -290)
color("yellow")
write("from:EggyXiaolu", font=("Comic Sans MS", 18, "bold"))  # 定义文字、位置、字体、大小
main()

playsound('MerryChristmas.mp3')
done()
