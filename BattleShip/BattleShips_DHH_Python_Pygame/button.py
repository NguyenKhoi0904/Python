import pygame


class Button:
    def __init__(self, image, size, pos, msg):
        self.name = msg
        self.image = image
        self.imageLarger = self.image
        self.imageLarger = pygame.transform.scale(self.imageLarger, (size[0] + 10, size[1] + 10))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.radarUsed = 0
        self.active = False

        self.msg = self.addText(msg)
        self.msgRect = self.msg.get_rect(center=self.rect.center)

    def addText(self, msg):
        font = pygame.font.SysFont('Stencil', 22)
        message = font.render(msg, 1, (255, 255, 255))
        return message

    def focusOnButton(self, window):
        if self.active:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(self.imageLarger, (self.rect[0] - 5, self.rect[1] - 5, self.rect[2], self.rect[3]))
            else:
                window.blit(self.image, self.rect)

    def action_on_press(self, game):
        if self.active:
            if self.name == 'Randomize':
                self.randomize_ship_positions(game, game.pFleet, game.pGameGrid, game.deployment)
                self.randomize_ship_positions(game, game.cFleet, game.cGameGrid, game.deployment)
            elif self.name == 'Reset':
                self.reset_ships(game.pFleet, game.deployment)
            elif self.name == 'Deploy':
                self.deployment_phase(game.deployment)
            elif self.name == 'Back':
                self.deployment_phase(game.deployment)
            elif self.name == 'Redeploy':
                game.tokens.clear()
                self.reset_ships(game.pFleet, game.deployment)
                self.randomize_ship_positions(game, game.cFleet, game.cGameGrid, game.deployment)
                game.update_pgame_logic(game.pGameGrid, game.pFleet)
                game.update_cgame_logic(game.cGameGrid, game.cFleet)
                #self.restart_the_game(game)

    def randomize_ship_positions(self, game, shiplist, gameGrid, deployment):
        if deployment:
            game.randomize_ship_positions(shiplist, gameGrid)

    def reset_ships(self, shiplist, deployment):
        """Resets the ships to their default positions"""
        if deployment:
            for ship in shiplist:
                ship.return_to_default_position()

    def deployment_phase(self, deployment):
        flag = True
        if deployment:
            flag = False
        return flag

    def restart_the_game(self, game):
        game.tokens.clear()
        self.reset_ships(game.pFleet, game.deployment)
        self.randomize_ship_positions(game, game.cFleet, game.cGameGrid, game.deployment)
        game.update_pgame_logic(game.pGameGrid, game.pFleet)
        game.update_cgame_logic(game.cGameGrid, game.cFleet)

    def updateButtons(self, gameStatus):
        if self.name == 'Deploy' and not gameStatus:
            self.name = 'Redeploy'
        elif self.name == 'Redeploy' and gameStatus:
            self.name = 'Deploy'
        if self.name == 'Reset' and not gameStatus:
            self.name = 'Radar Scan'
        elif self.name == 'Radar Scan' and gameStatus:
            self.name = 'Reset'
        if self.name == 'Randomize' and not gameStatus:
            self.name = 'Back'
        elif self.name == 'Back' and gameStatus:
            self.name = 'Randomize'
        self.msg = self.addText(self.name)
        self.msgRect = self.msg.get_rect(center=self.rect.center)

    def draw(self, window, deployment):
        self.updateButtons(deployment)
        self.focusOnButton(window)
        window.blit(self.image, self.rect)
        window.blit(self.msg, self.msgRect)
