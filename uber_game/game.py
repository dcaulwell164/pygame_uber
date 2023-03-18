import pygame
from utils import load_sprite
from models import Rider

class Game:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800,600))
        self.background = load_sprite("road", False)
        self.clock = pygame.time.Clock()
        self.rider = Rider((400,300))

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("space game")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit() 
        is_key_pressed = pygame.key.get_pressed()

        if is_key_pressed[pygame.K_d]:
            self.rider.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_a]:
            self.rider.rotate(clockwise=False)
        if is_key_pressed[pygame.K_w]:
            self.rider.accelerate()
        elif is_key_pressed[pygame.K_s]:
            self.rider.deccelerate()


    def _process_game_logic(self):
        self.rider.move(self.screen)
        # self.asteroid.move()

    def _draw(self):
        self.screen.blit(self.background, (0,0))
        self.rider.draw(self.screen)
        # self.asteroid.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)