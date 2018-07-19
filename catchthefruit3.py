s = 0 
class gameObject():
    
    def __init__(self, c, xpos, ypos, velocity, lives):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.vel = velocity
        self.lives = lives
    
        
class Basket(gameObject):
    
    # drawing the basket
    def display(self):
        
        stroke(self.c)
        fill(self.c)
        rect(self.xpos , height - 10, 80, 10)
        rect(self.xpos , height - 20, 10, 15)
        rect( self.xpos + 70 , height - 20, 10, 15)
                
                
    def move(self):
        
        if keyPressed:
            if keyCode == RIGHT:
                self.xpos = (self.xpos + 10) % width
            
            if keyCode == LEFT:
                self.xpos = (self.xpos -10) % width
            
    def intersect(self):
        return self.xpos
    
    def life(self):
        
        if self.lives > 1:
            self.lives = self.lives - 1
            return False
        
        else:
            return True
            #if true the game will end 
        

class Ball(gameObject):
    
    def display(self):
        fill (self.c)
        noStroke()
        ellipse (self.xpos,self.ypos,20,20)
        
        
    def fall (self):
        
        if s+1 % 2 == 0:
            self.vel += 0.5
            
        if height - 10 <= self.ypos <= height:
            self.ypos = random(-500,-50)
            self.xpos = random (width)
            
        self.ypos = self.ypos + self.vel
    
    def xposition(self):
        return self.xpos
    
    def yposition(self):
        return self.ypos

    
class Score():  
    def check (self,b,y,x):
   
        if height - 10 <= y <= height :
            if b < x < b + 70:
                global s
                s += 1
                return True
            return False
        return True
    
    
basket = Basket(color(0), 0, 100, 5, 3)
ball = Ball(color(255, 0, 0), 100, 100, 3,3) 
balls = []
score = Score()
    
def setup():
    size(450,400)
    frameRate(30)
    for i in range (0,3):
        balls.append(ball)
    
def draw():
    background(255)
    for i in range(0,len(balls)):
            balls[i].fall()
            balls[i].display()

    if score.check(basket.intersect(),ball.yposition(),ball.xposition()) :
        background(255)
        fill(0, 102, 153)
            
        text('score:', 10, 30)
        text(s, 10, 50)
    
        text('lives left:', 80, 30)
        text(basket.lives, 80, 50)
    
        for i in range(0,len(balls)):
            balls[i].fall()
            balls[i].display()
        
        basket.display()
        basket.move()

    else:
    
        if basket.life():
            background(0)
            fill(255)
            textSize(32)
            textAlign(CENTER, BOTTOM)
            text("Game over", 0.5*width, 0.5*height) 

                
        else:
            ball.display()
            ball.fall()
            basket.display()
            basket.move()
