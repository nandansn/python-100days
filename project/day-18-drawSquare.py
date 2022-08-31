from turtle import Turtle, Screen

class MyGui:
    def __init__(self, color='red',shape='circle'):
      
      self.aamai = Turtle()
      self.aamai.shape(shape)
      self.aamai.color(color)
    #   self.screen = Screen()
    #   self.screen.exitonclick()

    def draw_square(self, distance):
        print('hello')
        self.aamai.forward(distance)
        self.aamai.left(90)
        self.aamai.forward(distance)
        self.aamai.left(90)
        self.aamai.forward(distance)
        self.aamai.left(90)
        self.aamai.forward(distance)

    def dotted_line(self, distance):
       for i in range(0, distance, 10):
            self.aamai.pendown()
            self.aamai.forward(15)
            self.aamai.penup()
            self.aamai.forward(10)
            
    def draw_square_dotted(self, distance):
        print('hello')
        self.dotted_line(distance)
        self.aamai.left(90)
        self.dotted_line(distance)
        self.aamai.left(90)
        self.dotted_line(distance)
        self.aamai.left(90)
        self.dotted_line(distance)     

        self.aamai.penup()
        self.aamai.forward(20)
        
        


    
classic_gui = MyGui('blue','turtle')
# classic_gui.draw_square(250)
# classic_gui.dotted_line(100)

classic_gui.draw_square_dotted(100)

Screen().exitonclick()