import pygame
from entity import Entity


class Door(Entity):

    def __init__(self, x, y, playerId, is_locked):
        Entity.__init__(self, x, y, 100, 100, 1, "Door", False)
        self.playerId = playerId
        self.is_locked = is_locked
