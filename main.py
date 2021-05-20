from graphics import *


#Settings for the screen
win = GraphWin("Frogger", 500, 700, autoflush=False)
win.setBackground('black')

#Player Class
class Player(object):
    def __init__(self, startX, startY):
        self.x = startX
        self.y = startY       

        self.frog = Image(Point(startX, startY), "frog.gif")
        self.frog.draw(win)
    
      #Keyboard binding
    def movement(self):
        
        keyString = win.getKey()

        #win.getKey()
        #self.key = win.checkKey
        if keyString == "d":            
            self.frog.move(50, 0)
            return keyString

        elif keyString == "a":
            self.frog.move(-50, 0)
            return keyString

        while keyString == "s":            
            self.frog.move(0, 50)
            return keyString

        while keyString == "w":            
            self.frog.move(0, -35)
            return keyString

        while keyString == "space":                     
            return win.close()
            break       

        
#Enemy that moves created here
class Enemy(object):
    def __init__(self, speed, startXpos, startYpos):
        self.speed = speed
        self.x = startXpos
        self.y = startYpos
        self.p = Point(startXpos, startYpos)

        self.car_right = Image(self.p, "car_right.gif")

        self.car_right.draw(win)
        

    def move(self):
        self.x += self.speed
        self.car_right.move(self.speed, 0)

#method that returns the limit position of the car (cannot pass possition x == 500)
    #def limit_position(self):
        #self.position = Point(500, 600)
        #return self.position           


    #create a method to get the center of the Enemy object.    

#def Enemy_loop():
    #Print enemy on different road lanes  
    #enemy_line1 = [Enemy(30, 10, 600)]
    #enemy_line2 = [Enemy(30, 60, 560), Enemy(30, 200, 560)]
    #enemy_line3 = [Enemy(30, 140, 520), Enemy(30, 250, 520), Enemy(30, 400, 520)]


    #Enemy animation
    #for i in range(1000):  # main animation loop
        #for enemy in enemy_line1:  # loop through the enemy list
            #enemy.move()
            #time.sleep(1)  # wait a second...

        #for enemy in enemy_line2:  
            #enemy.move()
            #time.sleep(1)  

        #for enemy in enemy_line3:  
            #enemy.move()
            #time.sleep(1)
     



def main():

    enemy_line1 = [Enemy(30, 10, 600)]
    enemy_line2 = [Enemy(30, 60, 560), Enemy(30, 200, 560)]
    enemy_line3 = [Enemy(30, 140, 520), Enemy(30, 250, 520), Enemy(30, 400, 520)]
        #spawn player at 250, 650
    player_spawn = Player(250, 650)
    
    while True:

        for enemy in enemy_line1:  # loop through the enemy list
            enemy.move()
            time.sleep(1)  # wait a second...

        for enemy in enemy_line2:  
            enemy.move()
            time.sleep(1)  

        for enemy in enemy_line3:  
            enemy.move()
            time.sleep(1)

        player_spawn.movement()
        update(60)

main()


#TO-DO LIST:    
#if frog_point == car_point
#frog dead 