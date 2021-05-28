

class Enemy:

    def __init__(self, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        self.xvel = velocity 
        self.yvel = velocity 

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel * time
        self.ypos = self.ypos + time * self.yvel
        self.yvel = yvel1

    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos
        