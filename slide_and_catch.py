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
    
    def check(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
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
        self.bubble = Bubble(self)
        
        self.bubblePop = simpleGE.Sound("bubble-pop.mp3")
        
        self.sprites = [self.sword, self.bubble]
        
    def process(self):
        if self.sword.collidesWith(self.bubble):
            self.bubblePop.play()
            self.bubble.reset()
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    