import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SPACESHIP_TYPE

class Spaceship:
    WIDTH = 40
    HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = (SCREEN_HEIGHT) - HEIGHT

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.is_firing = False
        self.can_shoot = True
        self.fire_cooldown_timer = 0

    def update(self, game_speed, user_input, bullet_handler):
        if user_input[pygame.K_LEFT]:
            self.move_left(game_speed)
        elif user_input[pygame.K_RIGHT]:
            self.move_right(game_speed)
        elif user_input[pygame.K_UP]:
            self.move_up(game_speed)
        elif user_input[pygame.K_DOWN]:
            self.move_down(game_speed)
        if user_input[pygame.K_SPACE] and self.can_shoot:
            self.shoot(bullet_handler)
            self.fire_cooldown_timer = 20  # Establecer el tiempo de enfriamiento en un valor adecuado (puedes ajustarlo)
            self.can_shoot = False  # Desactivar la capacidad de disparar hasta que pase el tiempo de enfriamiento

        # Actualizar el tiempo de enfriamiento del disparo
        if not self.can_shoot:
            if self.fire_cooldown_timer > 0:
                self.fire_cooldown_timer -= 1
            else:
                self.can_shoot = True
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self, game_speed):
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        self.rect.x -= game_speed

    def move_right(self, game_speed):
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        self.rect.x += game_speed
    
    def move_up(self, game_speed):
        if self.rect.top > SCREEN_HEIGHT // 2:
            self.rect.y -= game_speed

    def move_down(self, game_speed):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += game_speed

    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_SPACESHIP_TYPE, self.rect.center)

