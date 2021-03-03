import pygame
from spriteManager import SpriteManager


class Game:
    def __init__(self, width, height):
        pygame.init()
        pygame.mixer.init()
        self.__width = width
        self.__height = height
        self.__screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
        self.__clock = pygame.time.Clock()
        self.__fps = 60
        self.__is_working = True

    def run_game(self):
        while self.__is_working:
            self.__clock.tick(self.__fps)
            control = self.__get_control()
            sprites = self.__update(control)
            self.__render(sprites)

    def __get_control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__close_game()
        return pygame.key.get_pressed()

    @staticmethod
    def __update(control):
        sprites = SpriteManager.update_objects(control)
        return sprites

    def __render(self, sprites):
        self.__screen.fill([0, 0, 0])
        sprites.draw(self.__screen)
        pygame.display.update()

    def __close_game(self):
        self.__is_working = False
