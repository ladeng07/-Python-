from turtle import *
speed (20)
penup ()
goto(-250,150)
pendown ()
def a ():
    forward (2)
    left (60)
    forward (2)
    right (120)
    forward(2)
    left (60)
    forward (2)
def b ():
    a ()
    left (60)
    a ()
    right (120)
    a ()
    left (60)
    a ()
def c ():
    b ()
    left (60)
    b ()
    right (120)
    b ()
    left (60)
    b ()
def d ():
    c ()
    left (60)
    c ()
    right (120)
    c ()
    left (60)
    c ()
def final ():
    d ()
    left (60)
    d ()
    right (120)
count = 0
while count != 6:
    final ()
    count += 1

    
