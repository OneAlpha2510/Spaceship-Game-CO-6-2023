import random

from game.utils.constants import ENEMY_2
from game.components.enemies.ship import Ship
from game.components.enemies.enemy import NewEnemy


class EnemyHandler:
    def __init__(self):
        self.enemies = []
    
    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_visible:
                self.remove_enemy(enemy)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        if len(self.enemies) < 5:
            # Use random.choice to add all types of enemies
            enemy_type = random.choice([1, 2])
            if enemy_type == 1:
                self.enemies.append(Ship())
            elif enemy_type == 2:
                width = 50
                height = 50
                self.enemies.append(NewEnemy(ENEMY_2, width, height))

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
