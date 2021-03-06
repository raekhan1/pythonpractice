class gameObject():
    
    def __init__(self, c, xpos, ypos, velocity):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.vel = velocity
        self.score = 0 
    
        
class Basket(gameObject):
    
    def display(self):
        
        stroke(self.c)
        fill(self.c)
        rect(self.xpos, height - 10, 80, 10)
        rect(self.xpos, height - 20, 10, 15)
        rect( self.xpos +70, height - 20, 10, 15)

    def move(self):
        
        if keyPressed:
            if keyCode == RIGHT:
                self.xpos = self.xpos + 10
                
            if keyCode == LEFT:
                self.xpos = self.xpos - 10
                
    def intersect(self):
        return self.xpos

class Ball(gameObject):
    
    def display(self):
        fill (self.c)
        ellipse(self.xpos,self.ypos,20,20)
        
    def fall (self):
        
        if self.score+1 % 2 == 0:
            self.vel += 10
            
        if height - 10 <= self.ypos <= height:
            self.ypos = 20
            self.xpos = random (width)
            
        self.ypos = self.ypos + self.vel
        
    
    def check (self):
        
        b = basket.intersect()
            
        if height - 10 <= self.ypos <= height :
            if b < self.xpos < b + 70:
                self.score += 1
                return True
            return False
        return True
    
    
basket = Basket(color(0), 0, 100, 5)
ball = Ball(color(255, 0, 0), 100, 100, 3) 
    
def setup():
    size(450,400)
    frameRate(10)


def draw():
    if ball.check() :
        background(255)
        text('score:', 10, 30)
        text(ball.score, 10, 50)
        fill(0, 102, 153)
        
        ball.display()
        ball.fall()
        
        basket.display()
        basket.move()
         
        
    else:
        textSize(32)
        textAlign(CENTER, BOTTOM)
        text("Game over", 0.5*width, 0.5*height) 
        fill(0, 102, 153)
