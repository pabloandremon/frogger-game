from Graphics import *

#Settings for the window
win = GraphWin("Frogger", 500, 700, autoflush=False)
win.setBackground('Black')

#Drawing the player here

#Register the player
win.Image("frog.gif")
win.Image("car_left.gif")
win.Image("car_right.gif")

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
class Player(Stuff):
    def __init__(self, x, y, width, height, image):
        Stuff.__init__(self, x, y, width, height, image)
    
    def up(self):
        self.y += 40
    
    def right(self):
        self.x += 40

    def down(self):
        self.y -= 40

    def left(self):
        self.x -= 40

class Car(Stuff):
    def __init__(self, x, y, width, height, image, dx):
        Stuff.__init__(self, x, y, width, height, image)
        self.dx = dx

    def update(self):
        self.x += self.dx
        #Check borders of the game windows
        if self.x < -400:
            self.x = 400
        
        if self.x > 400:
            self.x = -400

#Creating the objects
player = Player(0, -200, 40, 40, "frog.gif")
car_left = Car(0, -150, 40, 121, "car_left.gif", -0.1)
car_right = Car(0, -100, 40, 121, "car_right.gif", 0.1)

#Keyboard binding
win.getKey()
win.checkKey(player.up, "Up")
win.checkKey(player.down, "Down")
win.checkKey(player.left, "Left")
win.checkKey(player.right, "Right")

while True:
    #Render
    player.undraw()
    car_left.undraw()
    car_right.undraw()
    #Update the objects
    car_left.update(30)
    car_right.update(30)
    #Update the screen
    player.draw(win)
    car_left.draw()
    car_right.draw()

update(30)