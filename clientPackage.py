import pygame


class ClientPackage:
    def __init__(self):
        self.control = pygame.key
        self.state = 1  # 1 - Loading, 2 - Running
        self.playerId = 0
