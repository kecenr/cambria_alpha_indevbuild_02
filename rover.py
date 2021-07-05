from graphics_init import *

class rover(pygame.sprite.Sprite):

    def __init__(self, game, x, y):

        self.game = game
        self._layer = foe_layer
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TileSize
        self.y = y * TileSize
        self.width = TileSize
        self.height = TileSize

        self.x_change = 0
        self.y_change = 0
        self.idle = 0

        self.facing = random.choice(['left', 'right', 'swdash', 'nwdash', 'nedash', 'sedash', 'idle'])
        self.move_loop = 0
        self.max_travel = random.randint(32, 128)
        self.max_dash = random.randint(32, 64)

        self.image = self.game.roverspritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):

        self.movement()
        self.animation()
        self.collision()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):

        if self.facing == 'left':
            self.x_change -= RoverVel
            self.move_loop -= 1
            if self.move_loop <= -self.max_travel:
                self.facing = random.choice(['right', 'swdash', 'nwdash', 'nedash', 'sedash', 'idle'])

        elif self.facing  == 'right':
            self.x_change += RoverVel
            self.move_loop += 1
            if self.move_loop >= self.max_travel:
                self.facing = random.choice(['left', 'swdash', 'nwdash', 'nedash', 'sedash', 'idle'])

        elif self.facing  == 'swdash':
            self.x_change -= RoverDashVel
            self.y_change += RoverDashVel
            self.move_loop += 1
            if self.move_loop >= self.max_dash:
                self.facing = random.choice(['left', 'right', 'nwdash', 'nedash', 'sedash', 'idle'])

        elif self.facing  == 'sedash':
            self.x_change += RoverDashVel
            self.y_change += RoverDashVel
            self.move_loop += 1
            if self.move_loop >= self.max_dash:
                self.facing = random.choice(['left', 'right', 'nwdash', 'nedash', 'swdash', 'idle'])

        elif self.facing  == 'nwdash':
            self.x_change -= RoverDashVel
            self.y_change -= RoverDashVel
            self.move_loop += 1
            if self.move_loop >= self.max_dash:
                self.facing = random.choice(['left', 'right', 'sedash', 'nedash', 'swdash', 'idle'])

        elif self.facing  == 'nedash':
            self.x_change += RoverDashVel
            self.y_change -= RoverDashVel
            self.move_loop += 1
            if self.move_loop >= self.max_dash:
                self.facing = random.choice(['left', 'right', 'sedash', 'nwdash', 'swdash', 'idle'])

        elif self.facing == 'idle':
            self.idle += 1
            self.x_change = 0
            self.y_change = 0
            self.move_loop = 0
            if (self.idle > 100):
                self.facing = random.choice(['left', 'right', 'swdash', 'nwdash', 'nedash', 'sedash'])

    def animation(self):

        if self.facing == 'right' or self.facing == 'nedash' or self.facing == 'sedash':
            self.image = self.game.roverspritesheet.get_sprite(32, 0, self.width, self.height)

        elif self.facing == 'left' or self.facing == 'swdash' or self.facing == 'nwdash':
            self.image = self.game.roverspritesheet.get_sprite(64, 0, self.width, self.height)

        elif self.facing == 'idle':
            self.image = self.game.roverspritesheet.get_sprite(0, 0, self.width, self.height)

    def collision(self):

#credit to belambic for coding most of this

        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if hits:
            self.move_loop = 0
            if self.x_change < 0:
                if self.y_change < 0:
                    self.facing = random.choice(['right', 'sedash'])
                elif self.y_change == 0:
                    self.facing = random.choice(['right', 'nedash', 'sedash'])
                elif self.y_change > 0:
                    self.facing = random.choice(['right', 'nedash'])
            elif self.x_change > 0:
                if self.y_change < 0:
                    self.facing = random.choice(['left', 'swdash'])
                elif self.y_change == 0:
                    self.facing = random.choice(['left', 'nwdash', 'swdash'])
                elif self.y_change > 0:
                    self.facing = random.choice(['left', 'nwdash'])
            self.x_change = -self.x_change
            self.y_change = -self.y_change

    def entity_collision(self):

# I had to copy the block collision code because for some reason  you can only put one sprite group in the
# hits variable or else it sets the last argument to True which makes the blocks disappear.

        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.move_loop = 0
            if self.x_change < 0:
                if self.y_change < 0:
                    self.facing = random.choice(['right', 'sedash'])
                elif self.y_change == 0:
                    self.facing = random.choice(['right', 'nedash', 'sedash'])
                elif self.y_change > 0:
                    self.facing = random.choice(['right', 'nedash'])
            elif self.x_change > 0:
                if self.y_change < 0:
                    self.facing = random.choice(['left', 'swdash'])
                elif self.y_change == 0:
                    self.facing = random.choice(['left', 'nwdash', 'swdash'])
                elif self.y_change > 0:
                    self.facing = random.choice(['left', 'nwdash'])
            self.x_change = -self.x_change
            self.y_change = -self.y_change
