from graphics_init import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = p_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        pygame.mixer.pre_init(44100, 16, 2, 32) #frequency, size, channels, buffersize

        self.x = x * TileSize
        self.y = y * TileSize
        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'
        self.an_loop = 0
        self.footstep_timer = 0

        self.width = TileSize
        self.height = TileSize

        self.image = self.game.playerspritesheet.get_sprite(0, 0, 32, 32)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.hp = 100

        # loading player sounds

        self.footsteps = [pygame.mixer.Sound('Assets/footstep2.ogg'),
                                   pygame.mixer.Sound('Assets/footstep3.ogg'),
                                   pygame.mixer.Sound('Assets/footstep4.ogg')]

    def update(self):
        self.movement()
        self.animation()
        self.rect.x += self.x_change
        self.collision('x')
        self.rect.y += self.y_change
        self.collision('y')
        self.enemy_collision()
        self.mct_collision()

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()

        if self.footstep_timer > 0:
            self.footstep_timer -= 1

        if self.footstep_timer == 0:
            self.footstep_timer = 20

        if keys[pygame.K_w]:

            self.y_change -= PlayerVel
            self.facing = 'up'

            if self.footstep_timer == 20:
                random.choice(self.footsteps).play()

        if keys[pygame.K_a]:

            self.x_change -= PlayerVel
            self.facing = 'left'

            if self.footstep_timer == 20:
                random.choice(self.footsteps).play()

        if keys[pygame.K_s]:

            self.y_change += PlayerVel
            self.facing = 'down'

            if self.footstep_timer == 20:
                random.choice(self.footsteps).play()

        if keys[pygame.K_d]:

            self.x_change += PlayerVel
            self.facing = 'right'

            if self.footstep_timer == 20:
                random.choice(self.footsteps).play()

    #collisions

    def collision(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def enemy_collision(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
            
        if hits:
            self.hp -= 20
            if self.hp < 0:
                self.kill()
                self.game.playing = False

    def mct_collision(self):
        hits = pygame.sprite.spritecollide(self, self.game.triggers, False)
        if hits:
            key = (int(hits[0].rect.left/TileSize), int(hits[0].rect.top/TileSize))
            if key in self.game.tilemap.links:
                self.game.setTilemap(self.game.tilemap.links[key])
            else:
                print('crash prevention')

    def animation(self):

        right_walk = [self.game.playerspritesheet.get_sprite(64, 0, self.width, self.height), # left foot
                             self.game.playerspritesheet.get_sprite(32, 0, self.width, self.height)] # right foot

        left_walk = [self.game.playerspritesheet.get_sprite(128, 0, self.width, self.height), # left foot
                           self.game.playerspritesheet.get_sprite(160, 0, self.width, self.height)] # right foot

        down_walk = [self.game.playerspritesheet.get_sprite(224, 0, self.width, self.height), # left foot
                             self.game.playerspritesheet.get_sprite(256, 0, self.width, self.height)] # right foot

        up_walk = [self.game.playerspritesheet.get_sprite(320, 0, self.width, self.height), # left foot
                         self.game.playerspritesheet.get_sprite(352, 0, self.width, self.height)] # right foot

        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.playerspritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = right_walk[math.floor(self.an_loop)]
                self.an_loop += 0.1 # determines animation speed
                if self.an_loop >= 2: # resets the animation
                    self.an_loop = 0

        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.playerspritesheet.get_sprite(96, 0, self.width, self.height)
            else:
                self.image = left_walk[math.floor(self.an_loop)]
                self.an_loop += 0.1 # determines animation speed
                if self.an_loop >= 2: # resets the animation
                    self.an_loop = 0

        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.game.playerspritesheet.get_sprite(192, 0, self.width, self.height)
            else:
                self.image = down_walk[math.floor(self.an_loop)]
                self.an_loop += 0.1 # determines animation speed
                if self.an_loop >= 2: # resets the animation
                    self.an_loop = 0

        if self.facing == 'up':
            if self.y_change == 0:
                self.image = self.game.playerspritesheet.get_sprite(288, 0, self.width, self.height)
            else:
                self.image = up_walk[math.floor(self.an_loop)]
                self.an_loop += 0.1 # determines animation speed
                if self.an_loop >= 2: # resets the animation
                    self.an_loop = 0
