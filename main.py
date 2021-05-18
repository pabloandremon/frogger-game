from graphics import *

#Settings for the screen
win = GraphWin("Frogger", 500, 700, autoflush=True)
win.setBackground('black')

#Player Class
class Player(object):
    def __init__(self, startX, startY):
        self.x = startX
        self.y = startY

        self.frog = Image(Point(startX, startY), "frog.gif")
        self.frog.draw(win)
    
      #Keyboard binding
    def Movement(self):
        if self.win.keys.get("d"):
            self.frog.move(50, 0)
        if self.win.keys.get("a"):
            self.frog.move(-50, 0)
        if self.win.keys.get("s"):
            self.frog.move(0, 50)
        if self.win.keys.get("w"):
            self.frog.move(0, -50)

#spawn player at 250, 650
player_spawn = [Player(250, 650)]
        
#Enemy that moves created here
class Enemy(object):
    def __init__(self, speed, startXpos, startYpos):
        self.speed = speed
        self.x = startXpos
        self.y = startYpos

        self.car_right = Image(Point(startXpos, startYpos), "car_right.gif")

        self.car_right.draw(win)
        

    def move(self):
        self.x += self.speed
        self.car_right.move(self.speed, 0)

#Print enemy on different road lanes 
enemy_line1 = [Enemy(30, 10, 600)] 
enemy_line2 = [Enemy(30, 60, 560), Enemy(30, 200, 560)]
enemy_line3 = [Enemy(30, 140, 520), Enemy(30, 250, 520), Enemy(30, 400, 520)]

#Enemy animation
for i in range(1000):  # main animation loop
    for enemy in enemy_line1:  # loop through the enemy list
        enemy.move()
        time.sleep(1)  # wait a second...
    
    for enemy in enemy_line2:  
        enemy.move()
        time.sleep(1)  
    
    for enemy in enemy_line3:  
        enemy.move()
        time.sleep(1)  

while not win.isClosed():
    player_spawn.move()
    win.update()
    time.sleep(.1)

win.close()

#TO-DO LIST:
#if car reaches position 500, 500
#then undraw car and reset position
    
#if frog_point == car_point
#frog dead 