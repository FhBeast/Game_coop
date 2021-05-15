import pygame
from entity import Entity

RUN_SPEED = 10
WIDTH = 52
HEIGHT = 90
JUMP_POWER = 17
GRAVITY = 0.7
MAX_FRAME = 5
ANIMATION_DECELERATION = 3


class Player(Entity):

    def __init__(self, x, y, playerId):
        Entity.__init__(self, x, y, WIDTH, HEIGHT, 2, "Player", False)
        self.rect.bottom += 100 - HEIGHT
        self.rect.centerx += 50 - (WIDTH / 2)
        self.playerId = playerId
        self.anim = 0
        self.speed = 0
        self.speedFall = 0
        self.lookRight = True
        self.fall = True
        self.key = False
        self.state = 0  # 0 - default, 1 - jump, 2 - run
        self.frame = 0

    def update(self, left, right, jump, platforms):
        if not (left ^ right):
            self.state = 0
            self.frame = 0
            self.speed = 0
        else:
            self.state = 2
            if self.frame < MAX_FRAME:
                self.frame += 1 / ANIMATION_DECELERATION
            else:
                self.frame = 0
            if left:  # идем влево
                self.lookRight = False
                self.speed = -RUN_SPEED
            elif right:  # идем вправо
                self.lookRight = True
                self.speed = RUN_SPEED

        if jump:  # Прыжок
            self.state = 1
            if not self.fall:
                self.speedFall = -JUMP_POWER

        if self.fall:  # Если падаем, то увеличиваем скорость падения
            self.speedFall += GRAVITY

        self.fall = True  # Падаем каждый раз. Если падать не нужно, коллайдеры это исправят

        self.rect.y += self.speedFall  # Двигаемся по оси y
        self.collider(0, self.speedFall, platforms)  # Проверяем пересекаемся ли мы с чем-нибудь

        self.rect.x += self.speed  # Двигаемся по оси x
        self.collider(self.speed, 0, platforms)  # Проверяем пересекаемся ли мы с чем-нибудь

    def collider(self, speed_x, speed_y, platforms):
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform) and platform != self:  # Если есть пересечение

                if speed_x > 0:  # Если двигались вправо
                    self.rect.right = platform.rect.left  # То возвращаем игрока обратно

                if speed_x < 0:  # Если двигались влево
                    self.rect.left = platform.rect.right  # То возвращаем игрока обратно тоже

                if speed_y > 0:  # Если падали вниз
                    self.rect.bottom = platform.rect.top  # То возвращаем игрока на платформу
                    self.fall = False  # Отключаем падение
                    self.speedFall = 0  # Скорость падения обнуляется

                if speed_y < 0:  # Если двигались вверх
                    self.rect.top = platform.rect.bottom  # То не поднимаем игрока дальше
                    self.speedFall = 0  # Скорость падения обнуляется
