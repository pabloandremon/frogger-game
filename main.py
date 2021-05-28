
from graphics import *
from enemy import Enemy

#Settings for the screen
class Launcher:

    def __init__(self, win):
        self.car = Image(Point(-100, 550), 'car_right.gif')
        self.car.draw(win)
        self.win = win
        self.vel = 60.0
        self.redraw()

    def redraw(self):
        self.car.undraw()
        #pt2 = Point(self.vel)
    
    def carRespawn(self):
        return EnemyTracker(self.win, self.vel, 0.0)        

class EnemyTracker:
    def __init__(self, win, velocity, height):
        self.proj = Enemy(velocity = 55, height = 550)
        self.marker = Image(Point(-100, 550), 'car_right.gif') 
        self.marker.draw(win)

        #second car:
        self.proj2 = Enemy(velocity = 67, height = 500)
        self.marker2 = Image(Point(-100, 500), 'car_right.gif') 
        self.marker2.draw(win)

        self.proj3 = Enemy(velocity = 53, height = 115)
        self.marker3 = Image(Point(-100, 115), 'wood.gif') 
        self.marker3.draw(win)

        self.proj4 = Enemy(velocity = 67, height = 150)
        self.marker4 = Image(Point(-100, 150), 'wood.gif') 
        self.marker4.draw(win)

    def update(self, dt):
        self.proj.update(dt)
        center = self.marker.getAnchor()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx,dy) 

        #update second car:
        self.proj2.update(dt)
        center2 = self.marker2.getAnchor()
        dx2 = self.proj2.getX() - center2.getX()
        dy2 = self.proj2.getY() - center2.getY()
        self.marker2.move(dx2,dy2) 

        #update tree trunk
        self.proj3.update(dt)
        center3 = self.marker3.getAnchor()
        dx3 = self.proj3.getX() - center3.getX()
        dy3 = self.proj3.getY() - center3.getY()
        self.marker3.move(dx3,dy3)

        #update second tree trunk
        self.proj4.update(dt)
        center4 = self.marker4.getAnchor()
        dx4 = self.proj4.getX() - center4.getX()
        dy4 = self.proj4.getY() - center4.getY()
        self.marker4.move(dx4,dy4)

    def getX(self):
        #return the current x coordinate of the shot's center 
        return self.proj.getX()#, self.proj2.getX()

    def getY(self):
        #return the current y coordinate of the shot's center
        return self.proj.getY()#, self.proj2.getY()

    def undraw(self):
        #undraw the shot
        self.marker.undraw()
        self.marker2.undraw()
        

class Player:
    def __init__(self, win):
        #Registration of the Player (frogger)
        self.win = win
        self.player = Image(Point(250, 650), "frog.gif")
        self.player.draw(win)

    #Keyboard binding
    def up(self): return self.player.move(0,-35)
    def down(self): return self.player.move(0,50)
    def right(self): return self.player.move(50,0)
    def left(self): return self.player.move(-50,0)

def squares(win, x1, y1, x2, y2, color):

    p1 = Point(x1 , y1)
    p2 = Point(x2 , y2)

    r = Rectangle(p1, p2) 
    r.setFill(color) 
    r.setWidth(1)
    r.draw(win)

def line(win, x1, y1, x2, y2):

    p1 = Point(x1 , y1)
    p2 = Point(x2 , y2)

    l = Line(p1, p2)
    l.setWidth(9)
    l.setFill('white')
    l.draw(win)

def intro(win):

    squares(win, 0, 0, 500, 700, 'black')

    #Instructions:
    t = Text(Point(250,300), '''
    Welcome to our frogger game!
    Please enter your username (in the above box) 
    that you will be using during the game. After 
    writing your username Click anywhere to start.
    Control keys to move are: w, s, a and d.
    
    HAVE FUN!''')
    t.setTextColor("green4")
    t.setSize(13)
    t.draw(win)

    inputBox = Entry(Point(250,50), 19)
    inputBox.draw(win)
    win.getMouse()
    inputstr = inputBox.getText()     
    inputBox.undraw()    

    #Blue backgound
    square = Rectangle(Point(0, 0), Point(500, 700))
    square.setFill(color_rgb(51, 153, 255))
    square.draw(win)

    squares(win, 0, 0, 501, 35, 'black')#black rectangle in superior part of window for username and info.
    #Finish line:
    squares(win, 0, 33, 200, 110, 'lime green')
    squares(win, 300, 33, 505, 110, 'lime green')
    squares(win, 200, 33, 300, 55, 'lime green')
    t = Text(Point(250,44), 'FINISH LINE')
    t.setTextColor("red")
    t.setSize(11)
    t.draw(win)   

    #username box
    squares(win, 330, 0, 475, 25, 'gray')
    t2 = Text(Point(395, 12), inputstr)
    t2.setTextColor('white')
    t2.draw(win)

    #middle grass section:
    squares(win, 0, 430, 501, 350, 'olive')
    #road:
    square2 = Rectangle(Point(0, 430), Point(501, 625))
    square2.setFill(color_rgb(96, 96, 96))
    square2.draw(win)
    line(win, 10, 545, 60, 545) #start of first row of lines
    line(win, 90, 545, 140, 545)
    line(win, 170, 545, 220, 545)
    line(win, 250, 545, 300, 545)
    line(win, 330, 545, 380, 545)
    line(win, 410, 545, 460, 545)
    line(win, 490, 545, 540, 545)

    line(win, 10, 495, 60, 495) #start of second row of lines
    line(win, 90, 495, 140, 495)
    line(win, 170, 495, 220, 495)
    line(win, 250, 495, 300, 495)
    line(win, 330, 495, 380, 495)
    line(win, 410, 495, 460, 495)
    line(win, 490, 495, 540, 495)        
    #bottom grass section:
    squares(win, 0, 625, 501, 700, 'olive')




    



class FroggerApp:
    def __init__(self):
        self.win = GraphWin('Frogger Game by Xadiel & Pablo', 500, 700)
        

        #introduction, background and design of the game:
        intro(self.win)

        #Launcher and player instance:
        self.launcher = Launcher(self.win)
        self.player = Player(self.win)
        self.cars = []
        self.cars2 = []
    
    def updateCars(self, dt):
        alive = []
        alive2 = []
        for car in self.cars:
            car.update(dt)
            if car.getY() >= 0 and car.getX() < 515:
                alive.append(car)
                self.cars.pop(0) #pops the first object on list afteradding another one, creating an ilution of a moving object.
            else:
                car.undraw()
        self.cars = alive

        

    def run(self):
        while True:
            
            
            key = self.win.checkKey()
            if key in ['q', 'Q']: #EXIT
                break
            if key == "w":
                self.player.up()
            elif key == "s":
                self.player.down()
            elif key == "a":
                self.player.left()
            elif key == "d":
                self.player.right()

            self.updateCars(1/4)
            self.cars.append(self.launcher.carRespawn())
            
            
              
            update(5)
        self.win.close()

if __name__ == "__main__":
    FroggerApp().run()

#TO-DO LIST:    
#if frog_point == car_point
#frog dead 


