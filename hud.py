from graphics_init import *

class hud (pygame.sprite.Sprite):
    def __init__(self, game, hudx, hudy):

        self.game = game
        self._layer = 3
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.hudx = 0
        self.hudy = 0

        self.width = WinWidth
        self.height = 80
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(black)
        self.rect = self.image.get_rect()

        # Unimplemented (broken) code for a HP system

        #self.hpdisplay = Button(10, 100, 100, 50, white, black, 'HP: {n}', 32) #.format(n=game.player.hp), 32)
        #self.hpdisplay = game.font.render('HP: 100', True, white)
        #self.hpdisplay.rect = self.hpdisplay.get_rect(x=10, y=10)
        #game.screen.blit(self.hpdisplay, self.hpdisplay.rect)
