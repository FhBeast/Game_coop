import pygame
from entity import Entity

RUN_SPEED = 10
WIDTH = 52
HEIGHT = 90
JUMP_POWER = 17
GRAVITY = 0.7
ATTACK_COOLDOWN = 15


class Player(Entity):

    def __init__(self, x, y, playerID):
        Entity.__init__(self, x, y, WIDTH, HEIGHT, 2, "Player", True)
        self.rect.bottom += 100 - HEIGHT
        self.rect.centerx += 50 - (WIDTH / 2)
        self.playerID = playerID
        self.anim = 0
        self.speed = 0
        self.speedFall = 0
        self.__lookRight = True
        self.fall = True
        self.__attackNow = False
        self.__attackCooldown = 0
        self.__key = False

    def update(self, left, right, jump, attack, platforms):
        if jump:  # Прыжок
            if not self.fall:
                self.speedFall = -JUMP_POWER

        if left:  # идем влево
            self.__lookRight = False
            self.speed = -RUN_SPEED

        if right:  # идем вправо
            self.__lookRight = True
            self.speed = RUN_SPEED

        if not (left or right):  # стоим, когда не идем
            self.speed = 0

        if self.fall:  # Если падаем, то увеличиваем скорость падения
            self.speedFall += GRAVITY

        self.fall = True  # Падаем каждый раз. Если падать не нужно, коллайдеры это исправят

        self.__attackNow = False  # Обработка атаки
        if attack:
            if not self.__attackCooldown:
                self.__attackCooldown = ATTACK_COOLDOWN
                self.__attackNow = True
        if self.__attackCooldown > 0:
            self.__attackCooldown -= 1

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
