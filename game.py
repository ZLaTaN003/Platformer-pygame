import pygame
import sys
from src.characters import PhysicsBase
from src.utils import load_image


class Game:
    def __init__(self, width: int = 1280, height: int = 720) -> None:
        pygame.init()
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.display = pygame.Surface((self.screen_width / 2, self.screen_height / 2))
        self.clock = pygame.time.Clock()
        self.data = {"player": load_image("entities/player.png")}
        self.player = PhysicsBase(game=self,c_type="idk",pos=(50,100))
        self.movement = [0, 0] # move left or right [left,right]  r - l = +ve 

    def run(self) -> None:
        """Main Game loop here"""

        while True:
            self.display.fill("purple")
            self.player.draw(self.display)
            moved = self.movement[1] - self.movement[0]
            self.player.make_movement_frame((moved,0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = 1
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = 0
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = 0
            
            self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size()),(0,0)) # scale the display to screen size so pixel effect

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
