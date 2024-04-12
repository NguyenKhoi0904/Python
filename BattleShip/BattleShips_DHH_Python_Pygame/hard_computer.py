from easy_computer import EasyComputer
import pygame
import random
from token import Tokens
from service import HITSOUND, SHOTSOUND, MISSSOUND


class HardComputer(EasyComputer):
    def __init__(self):
        super().__init__()
        self.moves = []

    def makeAttack(self, gamelogic, game, turntimer):
        rowX = -1
        rowY = -1
        if len(self.moves) == 0:
            computerturntimer = pygame.time.get_ticks()
            if computerturntimer - turntimer >= 1000:
                validChoice = False
                while not validChoice:
                    rowX = random.randint(0, 9)
                    rowY = random.randint(0, 9)

                    if gamelogic[rowX][rowY] == ' ' or gamelogic[rowX][rowY] == 'O':
                        validChoice = True

                if gamelogic[rowX][rowY] == 'O':
                    game.tokens.append(
                        Tokens(game.redtoken, game.pGameGrid[rowX][rowY], 'Hit', game.firetokenimagelist,
                               game.explosionimagelist, None))
                    gamelogic[rowX][rowY] = 'T'
                    SHOTSOUND.play()
                    HITSOUND.play()
                    self.generateMoves((rowX, rowY), gamelogic)
                    self.turn = False
                else:
                    gamelogic[rowX][rowY] = 'X'
                    game.tokens.append(Tokens(game.bluetoken, game.pGameGrid[rowX][rowY], 'Miss', None, None, None))
                    SHOTSOUND.play()
                    MISSSOUND.play()
                    self.turn = False

        elif len(self.moves) > 0:
            computerturntimer = pygame.time.get_ticks()
            if computerturntimer - turntimer >= 2000:
                rowX, rowY = self.moves[0]
                game.tokens.append(Tokens(game.redtoken, game.pGameGrid[rowX][rowY], 'Hit', game.firetokenimagelist,
                                          game.explosionimagelist, None))
                gamelogic[rowX][rowY] = 'T'
                SHOTSOUND.play()
                HITSOUND.play()
                self.moves.remove((rowX, rowY))
                self.turn = False
        return self.turn

    def generateMoves(self, coords, grid, lstDir=None):
        x, y = coords
        # nx, ny = 0, 0
        for direction in ['North', 'South', 'East', 'West']:
            if direction == 'North' and lstDir != 'North':
                nx = x - 1
                ny = y
                if not (nx > 9 or ny > 9 or nx < 0 or ny < 0):
                    if (nx, ny) not in self.moves and grid[nx][ny] == 'O':
                        self.moves.append((nx, ny))
                        self.generateMoves((nx, ny), grid, 'South')

            if direction == 'South' and lstDir != 'South':
                nx = x + 1
                ny = y
                if not (nx > 9 or ny > 9 or nx < 0 or ny < 0):
                    if (nx, ny) not in self.moves and grid[nx][ny] == 'O':
                        self.moves.append((nx, ny))
                        self.generateMoves((nx, ny), grid, 'North')

            if direction == 'East' and lstDir != 'East':
                nx = x
                ny = y + 1
                if not (nx > 9 or ny > 9 or nx < 0 or ny < 0):
                    if (nx, ny) not in self.moves and grid[nx][ny] == 'O':
                        self.moves.append((nx, ny))
                        self.generateMoves((nx, ny), grid, 'West')

            if direction == 'West' and lstDir != 'West':
                nx = x
                ny = y - 1
                if not (nx > 9 or ny > 9 or nx < 0 or ny < 0):
                    if (nx, ny) not in self.moves and grid[nx][ny] == 'O':
                        self.moves.append((nx, ny))
                        self.generateMoves((nx, ny), grid, 'East')

        return
