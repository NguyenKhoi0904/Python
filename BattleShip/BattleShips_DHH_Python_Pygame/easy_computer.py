from service import SHOTSOUND, HITSOUND, MISSSOUND
import pygame
import random
from token import Tokens


class EasyComputer:
    def __init__(self):
        self.turn = False
        self.status = self.computerStatus('Thinking')
        self.name = 'Easy Computer'

    def computerStatus(self, msg):
        image = pygame.font.SysFont('Stencil', 22)
        message = image.render(msg, 1, (0, 0, 0))
        return message

    def makeAttack(self, gamelogic, game, turntimer):
        computerturntimer = pygame.time.get_ticks()
        rowX = -1
        colX = -1
        if computerturntimer - turntimer >= 1000:
            validChoice = False
            while not validChoice:
                rowX = random.randint(0, 9)
                colX = random.randint(0, 9)

                if gamelogic[rowX][colX] == ' ' or gamelogic[rowX][colX] == 'O':
                    validChoice = True

            if gamelogic[rowX][colX] == 'O':
                game.tokens.append(Tokens(game.redtoken, game.pGameGrid[rowX][colX], 'Hit', game.firetokenimagelist,
                                          game.explosionimagelist, None))
                gamelogic[rowX][colX] = 'T'
                SHOTSOUND.play()
                HITSOUND.play()
                self.turn = False
            else:
                gamelogic[rowX][colX] = 'X'
                game.tokens.append(Tokens(game.bluetoken, game.pGameGrid[rowX][colX], 'Miss', None, None, None))
                SHOTSOUND.play()
                MISSSOUND.play()
                self.turn = False
        return self.turn

    def draw(self, window, game):
        if self.turn:
            window.blit(self.status,
                        (game.cGameGrid[0][0][0] - game.cellSize, game.cGameGrid[-1][-1][1] + game.cellSize))
