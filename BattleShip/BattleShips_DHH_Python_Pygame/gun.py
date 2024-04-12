from service import load_image
import pygame


class Guns:
    def __init__(self, imgPath, pos, size, offset):
        self.orig_image = load_image(imgPath, size, True)
        self.image = self.orig_image
        self.offset = offset
        self.rect = self.image.get_rect(center=pos)

    def update(self, ship):
        """Cập nhật vị trí Gun trên Ship"""
        self.rotate_guns(ship)
        if not ship.rotation:
            self.rect.center = (ship.rect.centerx, ship.rect.centery + (ship.image.get_height() // 2 * self.offset))
        else:
            self.rect.center = (ship.rect.centerx + (ship.image.get_width() // 2 * -self.offset), ship.rect.centery)

    def _update_image(self, angle):
        """"Cập nhật hình ảnh lại khi mà hình ảnh Gun xoay theo chuột"""
        self.image = pygame.transform.rotate(self.orig_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def rotate_guns(self, ship):
        """Thay đổi vị trí Gun chỉa theo chuột"""
        direction = pygame.math.Vector2(pygame.mouse.get_pos()) - pygame.math.Vector2(self.rect.center)
        radius, angle = direction.as_polar()
        if not ship.rotation:
            if self.rect.centery <= ship.vImageRect.centery and angle <= 0:
                self._update_image(angle)
            if self.rect.centery >= ship.vImageRect.centery and angle > 0:
                self._update_image(angle)
        else:
            if self.rect.centerx <= ship.hImageRect.centerx and (angle <= -90 or angle >= 90):
                self._update_image(angle)
            if self.rect.centerx >= ship.hImageRect.centerx and (-90 <= angle <= 90):
                self._update_image(angle)

    def draw(self, window, ship):
        self.update(ship)
        window.blit(self.image, self.rect)
