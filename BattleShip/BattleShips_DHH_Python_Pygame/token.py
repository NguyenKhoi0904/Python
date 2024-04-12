import pygame


class Tokens:
    def __init__(self, image, pos, action, imageList=None, explosionList=None, soundFile=None):
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.topleft = self.pos
        self.imageList = imageList
        self.explosionList = explosionList
        self.action = action
        self.soundFile = soundFile
        self.timer = pygame.time.get_ticks()
        self.imageIndex = 0
        self.explosionIndex = 0
        self.explosion = False

    def animate_explosion(self):
        self.explosionIndex += 1
        if self.explosionIndex < len(self.explosionList):
            return self.explosionList[self.explosionIndex]
        else:
            return self.animate_fire()

    def animate_fire(self):
        if pygame.time.get_ticks() - self.timer >= 100:
            self.timer = pygame.time.get_ticks()
            self.imageIndex += 1
        if self.imageIndex < len(self.imageList):
            return self.imageList[self.imageIndex]
        else:
            self.imageIndex = 0
            return self.imageList[self.imageIndex]

    def draw(self, window):
        if not self.imageList:
            window.blit(self.image, self.rect)
        else:
            self.image = self.animate_explosion()
            self.rect = self.image.get_rect(topleft=self.pos)
            self.rect[1] = self.pos[1] - 10
            window.blit(self.image, self.rect)
