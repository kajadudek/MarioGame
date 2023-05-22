from Background.Castle import Castle
from setup import *


class Collider:
    def __init__(self, screen, list_of_objects, player):
        self.screen = screen
        self.list_of_objects = list_of_objects
        self.player = player
        self.collected_coins = 0
        self.points = 0
        self.sound = SoundPlayer

    def check_if_collision(self):
        player_obj = self.player.rect

        if self.player.rect.y > WINDOW_HEIGHT - 20:
            self.player.game_over(self.screen)
            self.player.landed()

        for i, block in enumerate(self.list_of_objects):
            block_obj = block.rect
            collect = False

            if block_obj.colliderect(player_obj):

                # Collision from both sides of the object
                if abs(block_obj.left - player_obj.right) < FALL_COLLISION_TOLERANCE:
                    if block.collision:
                        self.player.move(-PLAYER_SPEED, 0)

                        # Only castle has interaction when hit from the side
                        if isinstance(block, Castle):
                            block.hit()
                            return True

                    else:
                        collect = True

                elif abs(block_obj.right - player_obj.left) < FALL_COLLISION_TOLERANCE:
                    if block.collision:
                        self.player.move(PLAYER_SPEED, 0)

                    else:
                        collect = True

                # Player hitting the top of the object
                elif abs(block_obj.top - player_obj.bottom) < FALL_COLLISION_TOLERANCE:
                    if block.collision:
                        player_obj.bottom = block_obj.top
                        self.player.landed()
                    else:
                        collect = True

                # Hitting object from the bottom
                elif abs(block_obj.bottom - player_obj.top) < COLLISION_TOLERANCE:
                    if block.collision:
                        player_obj.top = block_obj.bottom
                        self.player.hit_head()
                        self.collected_coins = block.update_coins(self.collected_coins)
                        self.points += block.points
                        block.hit()
                    else:
                        collect = True

                if collect:
                    self.collected_coins = block.update_coins(self.collected_coins)
                    self.list_of_objects.remove(block)

        return False

    def check_for_enemy_collision(self, enemy, screen_boundary):
        # Create temporary rect object, that allows us to use colliderect, that has borders of enemy
        # Due to enemy constantly moving and moving screen, we need to create such object
        enemy_obj = pygame.Rect(enemy.rect.x - screen_boundary,
                                enemy.rect.y,
                                enemy.rect.height,
                                enemy.rect.width)

        for i, block in enumerate(self.list_of_objects):
            block_obj = block.rect

            if block_obj.colliderect(enemy_obj):

                # Enemy hitting the top of the object - do not change direction because of the tile beneath
                if abs(block_obj.top - enemy_obj.bottom) < FALL_COLLISION_TOLERANCE:
                    if block.collision:
                        enemy.rect.bottom = block_obj.top
                        enemy.landed()

                # Collision from both sides of the object
                elif abs(block_obj.left - enemy_obj.right) < COLLISION_TOLERANCE:
                    if block.collision:
                        enemy.move(-ENEMY_SPEED, 0)
                        enemy.hit()

                elif abs(block_obj.right - enemy_obj.left) < COLLISION_TOLERANCE:
                    if block.collision:
                        enemy.move(ENEMY_SPEED, 0)
                        enemy.hit()

        player_obj = self.player.rect
        if enemy_obj.colliderect(player_obj) and enemy.active:

            # Player hitting the top of the enemy - enemy's death
            if abs(enemy_obj.top + 16 - player_obj.bottom) < COLLISION_TOLERANCE:
                enemy.active = False
                self.sound.play(self.sound.stomp)
                self.points += enemy.points
                player_obj.bottom = enemy_obj.top + 16
                self.player.landed()
                self.player.jump(2)
                return

            # Collision from both sides of the object - player's death
            elif abs(enemy_obj.left - player_obj.right) < COLLISION_TOLERANCE:
                self.player.game_over(self.screen)

            elif abs(enemy_obj.right - player_obj.left) < COLLISION_TOLERANCE:
                self.player.game_over(self.screen)
