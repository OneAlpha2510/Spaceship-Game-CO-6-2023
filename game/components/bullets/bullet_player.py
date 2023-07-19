import pygame
from game.utils.constants import BULLET

class BulletPlayer:
    WIDTH = 10
    HEIGHT = 30
    SPEED = 15

    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        self.rect.y -= self.SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_collision(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.is_visible = False
                return True
        return False
