import pygame


class Game:
    def __init__(self, width, height):
        pygame.init()
        pygame.mixer.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self.fps = 60

    def run_game(self):
        while True:
            self.clock.tick(self.fps)
