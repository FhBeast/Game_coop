import pygame
from entity import Entity


class Door(Entity):

    def __init__(self, x, y, player_id, is_locked):
        Entity.__init__(self, x, y, 100, 100, 2, "Door", False)
        self.player_id = player_id
        self.is_locked = is_locked
