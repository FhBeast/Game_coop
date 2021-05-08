import pygame


class ClientPackage:
    def __init__(self):
        self.left = False
        self.right = False
        self.jump = False
        self.use = False
        self.attack = False
        self.state = 1  # 1 - Loading, 2 - Running
