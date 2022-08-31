from turtle import Turtle , Screen 


t = Turtle()
s = Screen()


def move_fwd():
    t.fd(10)

def move_bwd():
    t.backward(10)

def clock(a,b):
    def draw():
        t.circle(a,b)
    return draw

s.onkey(move_fwd,'w')

s.onkey(move_bwd,'s')
s.onkey(clock(80,30),'a')
s.onkey(clock(-80,30),'d')
s.listen()
s.exitonclick()