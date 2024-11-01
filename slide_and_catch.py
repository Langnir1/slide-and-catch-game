import simpleGE, pygame, random

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
        
        self.sprites = [self.sword]
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    