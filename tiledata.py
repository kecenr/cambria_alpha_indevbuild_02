from graphics_init import *

# triggers

class map_change_trigger(pygame.sprite.Sprite):

    def __init__(self, game, x, y):

        self.game = game
        self._layer = ground_layer
        self.groups = self.game.triggers
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TileSize
        self.y = y * TileSize
        self.width = TileSize
        self.height = TileSize

        self.image = self.game.grass.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

# tiles

class block(pygame.sprite.Sprite):

    def __init__(self, game, x, y):

        self.game = game
        self._layer = block_layer
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TileSize
        self.y = y * TileSize
        self.width = TileSize
        self.height = TileSize

        self.image = self.game.stonebricks.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class grass(pygame.sprite.Sprite):

    def __init__(self, game, x, y):

        self.game = game
        self._layer = ground_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TileSize
        self.y = y * TileSize
        self.width = TileSize
        self.height = TileSize

        self.image = self.game.grass.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
