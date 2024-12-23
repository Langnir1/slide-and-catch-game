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
    def __init__(self, score):
        super().__init__()
        self.setImage("bubble.png")
        
        self.response = "Play"
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
            "Welcome to bubble pop simulator!",
            "In this game, you control a sword that pops bubbles",
            "Such an original name, I know. " 
            "Using the arrow keys,",
            "move the sword left and right popping bubbles.",
            "Do your best to get the highest score within the time limit.",
            "GOOD LUCK!!!"]
        
        self.lastScore = score
        self.labelScore = simpleGE.Label()
        self.labelScore.text = (f"Last score: {self.lastScore}")
        self.labelScore.center = (330, 300)
        
        self.instructions.center = (320, 150)
        self.instructions.size = (600, 200)
        
        self.buttonPlay = simpleGE.Button()
        self.buttonPlay.text = "Play"
        self.buttonPlay.center = (100, 300)
        
        self.buttonQuit = simpleGE.Button()
        self.buttonQuit.text = "Quit"
        self.buttonQuit.center = (540, 300)
        
        self.sprites = [self.instructions,
                        self.labelScore,
                        self.buttonPlay,
                        self.buttonQuit]
        
    def process(self):
        if self.buttonPlay.clicked:
            self.response = "Play"
            self.stop()
        if self.buttonQuit.clicked:
            self.response = "Quit"
            self.stop()
            
    
def main():
    keepGoing = True
    score = 0
    
    while keepGoing:
        instructions = Instructions(score)
        instructions.start()
        
        if instructions.response == "Play":
            game = Game()
            game.start()
            score = game.score
        else:
            keepGoing = False
    
if __name__ == "__main__":
    main()
    