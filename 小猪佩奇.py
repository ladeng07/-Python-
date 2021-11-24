from turtle import *
import threading

class pig:
    def __init__(self):
        setup(700,700)
        colormode(255)
        hideturtle()
        
        self.body()
        self.nose()
        self.head()
        self.eyes()
        self.mouth()

        self.ears()

        self.hands()
        self.feet()
        self.tail()

        penup()
        goto(-170, -300)
        write('你是猪???吗...', font=('微软雅黑', 10, ''))
        pendown()

        done()

    def nose(self):
        pensize(5)
        penup()
        goto(-120, 120)
        setheading(-20)
        pendown()

        color((229,114,171),(244,179,211))
        begin_fill()
        init_num = 0.7
        for i in range(120):
            if 0 <= i < 30 or 60 <= i <90:
                init_num += 0.06
            else:
                init_num -= 0.06
            left(3)
            forward(init_num)
        end_fill()

        color((172,80,126),(172,80,126))
        pensize(1)

        penup()
        setheading(90)
        forward(40)
        setheading(180)
        forward(2)
        setheading(90)
        pendown()

        begin_fill()
        circle(-6)
        end_fill()

        penup()
        setheading(0)
        forward(20)
        setheading(270)
        forward(5)
        setheading(90)
        pendown()

        begin_fill()
        circle(-6)
        end_fill()

    def head(self):
        pensize(5)
        color((229, 114, 171), (244, 179, 211))
        penup()
        goto(-94, 188)
        setheading(-2)
        pendown()

        begin_fill()
        circle(-225, 35)
        circle(-55, 10)
        circle(-165, 12)
        circle(-108, 80)
        circle(-75, 45)
        circle(-119, 35)
        circle(-65, 50)
        circle(-75, 45)

        setheading(165)
        circle(-70, 60)
        goto(-120, 120)
        setheading(-20)
        init_num = 0.7
        for i in range(60):
            if 0 <= i < 30 or 60 <= i <90:
                init_num += 0.06
            else:
                init_num -= 0.06
            left(3)
            forward(init_num)

        end_fill()

        penup()
        goto(25, 37)
        setheading(145)
        pensize(1)
        color((229, 114, 171),(229, 114, 171))
        pendown()
        begin_fill()
        circle(-25)
        end_fill()


    def eyes(self):
        pensize(5)
        color((229, 114, 171),(255, 255, 255))
        penup()
        goto(-56, 150)
        setheading(90)
        pendown()

        begin_fill()
        circle(-14)
        end_fill()

        penup()
        goto(-14, 128)
        pendown()

        begin_fill()
        circle(-14)
        end_fill()

        penup()
        goto(-51,150)
        color('black','black')
        pensize(1)
        pendown()
        begin_fill()
        circle(-5)
        end_fill()

        penup()
        goto(-9, 128)
        pendown()
        begin_fill()
        circle(-5)
        end_fill()
        
    
    def ears(self):
        penup()
        goto(2, 163)
        pensize(5)
        color((222,118,174),(241,174,205))
        pendown()
        begin_fill()
        setheading(106)
        circle(-50,50)
        circle(-15, 140)
        circle(-50,58)
        goto(2, 163)
        end_fill()

        penup()
        goto(37, 142)
        pendown()
        begin_fill()
        setheading(80)
        circle(-40, 60)
        circle(-15, 140)
        circle(-50, 47)
        goto(37, 142)
        end_fill()
        

    def mouth(self):
        penup()
        goto(-7, 35)
        color((254,54,131),(33,29,30))
        pensize(5)
        setheading(28)
        pendown()
        begin_fill()
        circle(50, -90)
        setheading(-120)
        circle(40, 208)
        goto(-7, 35)
        end_fill()

    def body(self):
        pensize(5)
        penup()
        goto(50,-22)
        setheading(-60)
        pendown()

        pencolor((238,28,16))
        fillcolor((250,76,67))
        begin_fill()
        circle(-300, 28)
        setheading(180)
        forward(217)
        setheading(85)
        circle(-300, 28)
        setheading(-30)
        pencolor((229, 114, 171))
        pensize(0)
        circle(175,23)
        circle(65,63)

        end_fill()


    def hands(self):
        penup()
        goto(-95,-44)
        pensize(10)
        pencolor((234,157,193))
        pendown()

        setheading(200)
        circle(500, 10)

        penup()
        setheading(90)
        forward(14)
        setheading(0)
        pendown()

        circle(-14, 130)

        penup()
        goto(-95,-44)
        setheading(0)
        forward(160)
        pendown()

        setheading(-20)
        circle(-500, 10)

        penup()
        setheading(90)
        forward(14)
        setheading(0)
        pendown()
        circle(-14, -130)

    def feet(self):
        penup()
        goto(-56, -167)
        pensize(10)
        pencolor((234,157,193))
        setheading(-90)
        pendown()

        forward(43)

        pencolor('black')
        setheading(180)
        pensize(15)
        forward(35)

        penup()
        goto(-56, -167)
        setheading(0)
        forward(93)
        pensize(10)
        pencolor((234, 157, 193))
        setheading(-90)
        pendown()

        forward(43)

        pencolor('black')
        setheading(180)
        pensize(15)
        forward(35)


    def tail(self):
        penup()
        goto(89, -124)
        pencolor((233, 154, 193))
        pendown()
        pensize(5)
        setheading(0)
        circle(70, 12)
        circle(6, 350)
        circle(30, 35)


if  __name__ == '__main__':
    pig()
        
    
