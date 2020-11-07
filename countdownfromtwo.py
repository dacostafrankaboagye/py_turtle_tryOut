import turtle


def zero():
    r = turtle.Turtle()
    r1 = turtle.Turtle()
    r.ht()
    r1.ht()
    r.speed('fastest')
    r1.speed('fastest')

    r.fillcolor('yellow')
    r.begin_fill()


    r.up()
    r.goto(-100, 0)
    r.down()
    r.goto(-100,100)
    r.goto(-50,200)
    r.goto(50,200)
    r.goto(100,100)
    r.goto(100,-100)
    r.goto(50,-200)
    r.goto(-50,-200)
    r.goto(-100,-100)
    r.goto(-100,0)
    r.end_fill()

    r1.fillcolor('white')
    r1.begin_fill()
    r1.up()
    r1.goto(0,50)
    r1.down()
    r1.goto(-50,0)
    r1.goto(0,-50)
    r1.goto(50,0)
    r1.goto(0,50)
    r1.end_fill()

    def cls():
        for i in range(15):
            r.undo()
    def cls2():
        for i in range(10):
            r1.undo()
            
    ab = r.getscreen()
    ab2 = r1.getscreen()

    ab.ontimer(cls, t=500)
    ab2.ontimer(cls2, t=500)


    
    


def one():
    

    t2 = turtle.Turtle()
    t2.ht()
    t2.speed('fastest')


    t2.fillcolor('green') 
    t2.begin_fill()

    
    t2.seth(270)

    t2.fd(100)
    t2.rt(90)
    t2.fd(100)
    t2.lt(90)
    t2.fd(100)
    t2.lt(90)
    t2.fd(100 * 3)
    t2.lt(90)
    t2.fd(100)
    t2.lt(90)
    t2.fd(100)
    t2.rt(90)
    t2.fd(100)

    t2.up()
    t2.home()
    t2.down()
    t2.seth(90)

    t2.fd(100)
    t2.circle(100 , extent=-90)
    t2.goto((-100.00,100.00))
    t2.circle(100, extent=80)
    xval = t2.xcor()
    t2.seth(0)
    t2.fd((-1*xval) + 100)
    t2.goto(100, 0)

    t2.end_fill()

    def cls():
        for i in range(28):
            t2.undo()

        zero()
            
    ab = t2.getscreen()

    ab.ontimer(cls, t=500)

    


        


def two():

    t = turtle.Turtle()
    t.ht()
    t.begin_fill()
    t.speed('fastest')
    t.goto(0,100)
    t.goto(-100, 100)
    t.goto(-100, 150)
    t.goto(50,150)
    t.goto(50,-50)
    t.goto(-50,-50)
    t.goto(-50, -100)
    t.goto(50, -100)
    t.goto(50, -150)
    t.goto(-100, -150)
    t.goto(-100,0)
    t.home()
    t.end_fill()

    def cls():
        for i in range(15):
            t.undo()

        one()
            
    ab = t.getscreen()

    ab.ontimer(cls, t=500)
    

    




def numc():
    global a
    a.clear()
    two()



m = turtle.Turtle()
m.speed('fastest')
m.ht()
a = m.getscreen()


m.write('Press the >> s << key to start', align='center', font=('Arial', 20, 'normal'))


a.onkeypress( numc, 's')


a.listen()


user_input = input("Comments: ")
print('Noted')

