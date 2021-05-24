# Timofte Robert Octavian - VR429581
# Elaborato Python A.A. 2020/2021
# Progetto Curve
import turtle

LATO = 200
RATIO = 1.65

def barnsley (lato, liv):
    if(liv > 0):
        lato2 = lato/RATIO
        t.fd(lato)
        t.lt(45)
        barnsley(lato2,liv-1)
        t.rt(90)
        barnsley(lato2,liv-1)
        t.lt(45)
        t.bk(lato)

def sierpinski (lato, liv):
    if liv==0:
        for i in range(0,3):
            t.fd(lato)
            t.lt(120)
    else:
        sierpinski(lato/2,liv-1)
        t.fd(lato/2)
        sierpinski(lato/2,liv-1)
        t.bk(lato/2)
        t.lt(60)
        t.fd(lato/2)
        t.rt(60)
        sierpinski(lato/2,liv-1)
        t.lt(60)
        t.bk(lato/2)
        t.rt(60)

def koch (lato, liv):
    if liv == 1:
        t.fd(lato)
    else:
        koch(lato/3, liv-1)
        t.lt(90)
        koch(lato/3, liv-1)
        t.rt(90)
        koch(lato/3, liv-1)
        t.rt(90)
        koch(lato/3, liv-1)
        t.lt(90)
        koch(lato/3, liv-1)

def fioccoDiNeve (lato, liv):
    for i in range(0,4):
        koch(lato,liv)
        t.rt(90)

def pitagora(ax, ay, bx, by, liv):
    if liv > 0:
        dx,dy = bx-ax, ay-by
        x3,y3 = bx-dy, by-dx
        x4,y4 = ax-dy, ay-dx
        x5,y5 = x4 + (dx - dy)/2, y4 - (dx + dy)/2
        t.goto(ax, ay)
        t.pd()
        for x, y in ((bx, by), (x3, y3), (x4, y4), (ax, ay)):
            t.goto(x, y)
        t.pu()
        pitagora(x4,y4, x5,y5, liv - 1)
        pitagora(x5,y5, x3,y3, liv - 1)

if __name__ == '__main__':
    curve = ['L’albero di Barnsley', 'Triangolo di Sierpinski', 'Fiocco di neve', 'L’albero di Pitagora']
    print ("--------------------------------------\nPROGETTO CURVE\n--------------------------------------")
    print ("Curve disponibili:")
    for i in range(0,len(curve)):
        print ('{}) {}'.format(i+1, curve[i]))
    print ("--------------------------------------")

    scelta = int(input("Scegli una curva(1-4): "))
    while scelta < 1 or scelta > len(curve):
        scelta = int(input("Scegli una curva(1-4): "))

    liv = int(input("Scegli una profondità(>0): "))
    while liv < 1:
        liv = int(input("Scegli una profondità(>0): "))

    colori = ['red', 'blue', 'lime green', 'brown', 'pink']
    print ("Colori disponibili:")
    for i in range(0,len(colori)):
        print ('{}) {}'.format(i+1, colori[i]))

    clr = int(input("Scegli un colore: "))
    while clr < 1 or clr > len(colori):
        clr = int(input("Scegli un colore: "))

    window = turtle.Screen()
    window.screensize()
    window.setup(width = 1.0, height = 1.0)
    t = turtle.Turtle() 
    t.speed(0)
    t.pencolor(colori[clr-1])
    t.pensize(5)

    if scelta == 1:
        t.pu()
        t.sety(-500)
        t.pd()
        t.lt(90)
        barnsley(LATO, liv)
    elif scelta == 2:
        t.pu()
        t.setx(-280)
        t.sety(-280)
        t.pd()
        sierpinski((LATO*liv)/2, liv)
    elif scelta == 3:
        t.pu()
        t.setx(-225)
        t.sety(250)
        t.pd()
        fioccoDiNeve((LATO*liv)/2, liv)
    elif scelta == 4:
        t.pu()
        pitagora(100, -500, -100, -500, liv)

    t.hideturtle()
    ts = t.getscreen()
    ts.getcanvas().postscript(file="output.eps")
    
    window.exitonclick()