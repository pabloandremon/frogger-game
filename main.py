from graphics import *

#Settings for the screen
win = GraphWin("Frogger", 500, 700, autoflush=True)

#xadi testing motion
car_right = []
for x in [-1, 1]:
    for y in [-1,1]:
        circle = Circle(Point(250, 250), 20)
        circle.draw(win)
        circle.append((circle, (x, y)))

for _ in range(250):
    for circle, (x, y) in car_right:
        circle.move(x, y)


#Register the player
#drawing the player here
frog_img = Image(Point(200, 600) ,"Frog.gif")
frog_img.draw(win)
carL_img = Image(Point(100, 500),"Car_left.gif")
carL_img.draw(win)
carR_img = Image(Point(50, 400), "Car_right.gif")
carR_img.draw(win)

#Creating the parent class
class Stuff():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def RenderMotion(self, pen):
        pen.setCoords(self.x, self.y)
        pen.draw(self.image)
        pen.update()


#Creating the child class
class Player:
    def __init__(self):
        self.frog_img = char
        self.win = window

#Creating the objects 1
    def create(self):
        self.frog_img.setFill('green')
        self.frog_img.draw(self.win)
    
    def Movement(self):
        #Keyboard binding
        if self.win.lastKey == "d":
            self.p1.move(40, 0)
        if self.win.lastKey == "a":
            self.p1.move(-40, 0)
        if self.win.lastKey == "s":
            self.p1.move(0, 40)
        if self.win.lastKey == "w":
            self.p1.move(0, -40)


#Creating the objects 2

#if frog_point == car_point
#frog dead 
