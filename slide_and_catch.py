import simpleGE, pygame, random

class Bubble(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("bubble.png")
        self.setSize(30, 30)
        self.reset()
        
    def reset(self):
        self.y = 0
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)
    
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class LabelScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score = 0"
        self.center = (100, 30)
        
class LabelTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time = 0"
        self.center = (500, 30)
            
class Sword(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("fire_sword.png")
        self.setSize(50, 70)
        self.position = (300, 400)
        self.moveSpeed = 5

    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("cosmos.jpg")
        
        self.sword = Sword(self)
        self.numBubbles = 10
        self.bubble = []
        for i in range(self.numBubbles):
            self.bubble.append(Bubble(self))
            
        self.score = 0
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        
        self.labelScore = LabelScore()
        self.labelTime = LabelTime()
        
        self.bubblePop = simpleGE.Sound("bubble-pop.mp3")
        
        self.sprites = [self.sword,
                        self.bubble,
                        self.labelScore,
                        self.labelTime]
        
        
        
    def process(self):
        for bubble in self.bubble:
            if self.sword.collidesWith(bubble):
                self.bubblePop.play()
                self.score += 1
                self.labelScore.text = (f"Score = {self.score}")
                bubble.reset()
        
        self.labelTime.text = (f"Time = {self.timer.getTimeLeft():.2f}")
        if self.timer.getTimeLeft() < 0:
            print(f"If this ran, the final score should be {self.score}")
            self.stop()

class Instructions(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("bubble.png")
        self.sprites = []
    
def main():
    instructions = Instructions()
    instructions.start()
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    