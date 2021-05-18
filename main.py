from graphics import *

#Settings for the screen
win = GraphWin("Frogger", 500, 700, autoflush=True)
win.setBackground('black')

#xadi testing motion
car_right = []
for x in [-1, 1]:
    for y in [-1,1]:
        circle = Circle(Point(250, 250), 20)
        circle.draw(win)
        car_right.append((circle, (x, y)))

for _ in range(250):
    for circle, (x, y) in car_right:
        circle.move(x, y)


#Register the player
#drawing the player here
frog_img = Image(Point(200, 600) ,"frog.gif")
frog_img.draw(win)
carL_img = Image(Point(100, 500),"car_left.gif")
carL_img.draw(win)
carR_img = Image(Point(50, 400), "car_right.gif")
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

class Enemy(object):
    def __init__(self, speed, startXpos, startYpos):
        self.speed = speed
        self.x = startXpos
        self.y = startYpos

        self.graphic = Image(Point(startXpos, startYpos), "Car_left.gif")
        self.graphic.draw(win)

    def move(self):
        self.x += self.speed
        self.graphic.move(self.speed, 0)

myEnemies = [Enemy(40, 50, 100), Enemy(50, 50, 200), Enemy(60, 50, 300)]

for i in range(40):  # main animation loop
    for enemy in myEnemies:  # loop through the enemy list
        enemy.move()
        time.sleep(1)  # wait a second...


win.getMouse()

#if frog_point == car_point
#frog dead 