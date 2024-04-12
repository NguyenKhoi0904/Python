from token import Tokens
from service import SHOTSOUND, HITSOUND, MISSSOUND
import pygame


class Player:
    def __init__(self):
        self.turn = True

    def makeAttack(self, grid, logicgrid, game):
        posX, posY = pygame.mouse.get_pos()
        if grid[0][0][0] < posX < grid[0][-1][0] + game.cellSize and grid[0][0][1] < posY < grid[-1][0][1] + game.cellSize:
            for i, rowX in enumerate(grid):
                for j, colX in enumerate(rowX):
                    if colX[0] < posX < colX[0] + game.cellSize and colX[1] < posY < colX[1] + game.cellSize:
                        if logicgrid[i][j] != ' ':
                            if logicgrid[i][j] == 'O':
                                game.tokens.append(Tokens(game.redtoken, grid[i][j], 'Hit', None, None, None))
                                logicgrid[i][j] = 'T'
                                SHOTSOUND.play()
                                HITSOUND.play()
                                self.turn = False
                        else:
                            logicgrid[i][j] = 'X'
                            SHOTSOUND.play()
                            MISSSOUND.play()
                            game.tokens.append(Tokens(game.greentoken, grid[i][j], 'Miss', None, None, None))
                            self.turn = False
