from Graphics import *

#Settings for the window
win = GraphWin("Frogger", 500, 700, autoflush=False)
win.setBackground('Black')

#Drawing the player here


#Creating the parent class
class Stuff():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    #def WinMotion(self):


#Creating the child class
class Player(Stuff):
    def __init__(self, x, y, width, height, image):
        Stuff.__init__(self, x, y, width, height, image)


#Creating the objects
player = Player(0, -200, 40, 40, "frogger.gif")