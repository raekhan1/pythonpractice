class gameObject():
    
    def __init__(self, c, xpos, ypos, velocity):
        
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.vel = velocity
   
    
        
class Basket(gameObject):
    # using inheritance for the object
    
    # drawing the basket
    def display(self):
        
        stroke(self.c)
        fill(self.c)
        rect(self.xpos , height - 10, 80, 10)
        rect(self.xpos , height - 20, 10, 15)
        rect( self.xpos + 70 , height - 20, 10, 15)
                
                
    def move(self):
    # moving with wrap around effect (may change later)
    
        if keyPressed:
            if keyCode == RIGHT:
                self.xpos = (self.xpos + (10 * self.vel)) % width 
            
            if keyCode == LEFT:
                self.xpos = (self.xpos - (10 * self.vel)) % width
            
    def intersect(self, bally,ballx):
        
    #checking to see if the basket and ball intersect 
    
        if height - 20 <= bally <= height :
            if self.xpos < ballx < self.xpos + 70:
                return True
            return False
        return False
       

        

class Ball(gameObject):
    
    def __init__(self, c, xpos, ypos, velocity):
        gameObject.__init__(self, c, xpos, ypos, velocity)
        #using the super class so that I still inherit the game object
        self.create()
    
    
    def display(self):
        
        fill (self.c)
        noStroke()
        ellipse (self.xpos,self.ypos,20,20)
        
        
    def fall (self):    
        self.ypos = self.ypos + self.vel
        
    def create (self):
        self.ypos = random(-1000,-200)
        self.xpos = random(width)
        
    def check(self):
    
        if  height - 10 <= self.ypos <= height:
            self.create()
            return True
        return False

    
    def xposition(self):
        return self.xpos
    
    def yposition(self):
        return self.ypos

    
class Score():  
    def __init__(self):
        self.score = 0 
    
    def addScore(self):
        self.score += 1

class Life():
    def __init__(self):
        self.lives = 5
        self.back = 255
    
        
    def removeLife(self):
        if self.lives > 1:
            
            self.lives = self.lives - 1
            return False
        
        elif self.lives == 1:
            
            self.back = 0 
            self.lives = 0
            
        else:
            return True
        
    def gameOver(self):
        if self.lives == 0:
            return True
        return False
        
    
    
basket = Basket(color(0), 0, 100, 2) 
score = Score()
life = Life()
balls = []
    
def setup():
    size(450,400)
    frameRate(30)
    for i in range(int(random(1,3))):
        balls.append(Ball(color(255, 0, 0), 100, 100, 5) )
   


def draw():

    background(life.back)
    
    textSize(12)
    fill(0)
    
    text('score:',20,30)
    text(score.score,20,50)
    
    text('lives Left:',100,30)
    text(life.lives,100,50)

    if life.gameOver():
        fill(255)
        textSize(60)
        textAlign(CENTER, BOTTOM)
        text("Game over", 0.5*width, 0.5*height) 
        del balls[:]
    
    for ball in balls:
        ball.display()
        ball.fall()
        
        if basket.intersect(ball.yposition(),ball.xposition()):
        #Every time a ball is caught a new ball is added to the array
            ball.create()
            score.addScore()    
            balls.append(Ball(color(random(255),random(255),random(255)), 100, 100, random(5,10)))
            
        if ball.check():
            life.removeLife()    
            
    basket.move()
    basket.display()
