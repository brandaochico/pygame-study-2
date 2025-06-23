import pygame.sprite

from settings import *
from os.path import join
from random import randint

from player import Player
from sprites import *

class Game:
    def __init__(self):
        # setup
        pygame.init()
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Vampire Survivors')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # sprites
        self.player = Player((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), self.all_sprites, self.collision_sprites)
        for i in range(6):
            x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            w, h = randint(60, 100), randint(50, 100)
            ColissionSprite((x,y), (w, h), (self.all_sprites, self.collision_sprites))


    def run(self):
        while self.running:
            # delta time
            dt = self.clock.tick() / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            self.all_sprites.update(dt)

            # draw
            self.display.fill('darkgray')
            self.all_sprites.draw(self.display)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
