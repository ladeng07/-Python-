__author__ = 'leoyuan'
import turtle as t
import time
import random
import sys

def screenint():
    t.title("骰子游戏！")
    try:
        t.bgpic("touzi.gif")
    except:
        pass
    t.setup(width=570, height=350, startx=400, starty=300)
    t.screensize(500, 300)
#os->offset

def num(os):
    global one, two, three, four, five, six
    one = (1, (50 + os, -50))
    two = (2, (25 + os, -50), (75 + os, -50))
    three = (3, (50 + os, -25), (25 + os, -75), (75 + os, -75))
    four = (4, (25 + os, -25), (75 + os, -25),
           (25 + os, -75), (75 + os, -75))
    five = (5, (25 + os, -25), (75 + os, -25),
           (25 + os, -75), (75 + os, -75), (50 + os, -50))
    six = (6, (25 + os, -25), (75 + os, -25),
          (25 + os, -75), (75 + os, -75),
          (25 + os, -50), (75 + os, -50))

def user_int():
    global user_count, ai_count, name
    ai_count = random.choice(('one', 'two', 'three', 'four', 'five', 'six'))
    user_count = random.choice(('one', 'two', 'three', 'four', 'five', 'six'))
    name = t.textinput('完善信息', '输入姓名：')
    t.up()
    t.goto(-100, 30)
    try:
        t.write(name + "正在扔出骰子……", align='left', font=('微软雅黑', 14, 'normal'))
    except:
        sys.exit(0)
    time.sleep(2)
    t.clear()

def ai_int():
    t.up()
    t.goto(100, 30)
    t.write("电脑正在扔出骰子……", align='right', font=('微软雅黑', 14, 'normal'))
    time.sleep(2)
    t.undo()

def beauty():
    beauty_c = 0
    t.setx(-200)
    t.pensize(2)
    t.down()
    t.color('red', 'yellow')
    t.speed(8)
    t.begin_fill()
    while True:
        beauty_c += 1
        t.fd(200)
        t.lt(170)
        if beauty_c == 36:
            break
    t.end_fill()
    t.done()

def pk():
    u_count = int(eval(user_count)[0])
    a_count = int(eval(ai_count)[0])
    if u_count == a_count:
        t.write('打成平局！', align='right', font=('微软雅黑', 30, 'normal'))
    elif u_count > a_count:
        t.write('恭喜' + name + '胜利！', align='right', font=('微软雅黑', 30, 'normal'))
        beauty()
    else:
        t.write('好可惜！电脑赢了！', align='right', font=('微软雅黑', 30, 'normal'))
    time.sleep(2)
    t.bye()

def draw_dot(n):
    for d in range(n[0]):
        x = n[d + 1][0]
        y = n[d + 1][1]
        t.goto(x, y)
        t.dot(25, 'red')
        t.up()

def frame(dot, os):
    t.color('black')
    t.pensize(5)
    t.up()
    t.goto(0 + os, 0)
    t.down()
    t.speed(10)
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.up()
    draw_dot(dot)
    time.sleep(1)

screenint()
user_int()
num(-150)
frame(eval(user_count), -150)
ai_int()
num(100)
frame(eval(ai_count),100)
pk()
