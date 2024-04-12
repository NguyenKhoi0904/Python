import pygame, sys
from player import Player
from easy_computer import EasyComputer
from hard_computer import HardComputer
from button import Button

from battle_ship_type_one import BattleShips_TypeOne
from service import SCREENWIDTH, SCREENHEIGHT, load_image, load_animation_images, load_sprite_sheet_images, GAMESCREEN, get_font, BUTTONSOUND, updateGameScreen

pygame.init()

# game = BattleShips_TypeOne()
# game.create_grid()
# game.create_fleet()
# game.create_logic()
# game.create_button()
# game.randomize_ship_positions(game.cFleet, game.cGameGrid)
# player1 = Player()
# computer = EasyComputer()
# RUNGAME = True
def menu_main(window):
    print("Menu screen")
    while True:
        bgmain = pygame.image.load(r'assets\images\background\backroundplay.jpg')
        bgmain = pygame.transform.scale(bgmain, (SCREENWIDTH, SCREENHEIGHT))
        window.blit(bgmain, (0, 0))

        textmain = get_font(100).render(" MENU ", True, "Black")
        testrect = textmain.get_rect(center=((SCREENWIDTH)//2, (SCREENHEIGHT)//6))
        window.blit(textmain, testrect)

        BUTTONIMAGE = load_image(r'assets\images\buttons\button.png', (300, 100))
        button = [
            Button(BUTTONIMAGE, (300, 100), ((SCREENWIDTH - 300)//2, (SCREENHEIGHT - 100)//2 - 150), 'Play'),
            Button(BUTTONIMAGE, (300, 100), ((SCREENWIDTH - 300)//2, (SCREENHEIGHT - 100)//2), 'Option'),
            Button(BUTTONIMAGE, (300, 100), ((SCREENWIDTH - 300)//2, (SCREENHEIGHT - 100)//2 + 150), 'Quit')
        ]

        for buttons in button:
            if buttons.name in ['Play', 'Option', 'Quit']:
                buttons.active = True
                buttons.draw(window, False)
            else:
                buttons.active = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for buttonx in button:
                        if buttonx.rect.collidepoint(pygame.mouse.get_pos()):
                            if buttonx.name == 'Play' and buttonx.active:
                                BUTTONSOUND.play()
                                play(window)
                            elif buttonx.name == 'Option' and buttonx.active:
                                BUTTONSOUND.play()
                                option(GAMESCREEN)
                            elif buttonx.name == 'Quit' and buttonx.active:
                                BUTTONSOUND.play()
                                pygame.quit()
                                sys.exit()

        pygame.display.update()


def play(window):
    print("Play screen")
    while True:
        bgplay = pygame.image.load(r'assets\images\background\Carrier.jpg')
        bgplay = pygame.transform.scale(bgplay, (SCREENWIDTH, SCREENHEIGHT))
        window.blit(bgplay, (0, 0))

        textplay = get_font(100).render(" PLAY ", True, "Black")
        testrect = textplay.get_rect(center=((SCREENWIDTH) // 2, (SCREENHEIGHT) // 6))
        window.blit(textplay, testrect)

        BUTTONIMAGE = load_image(r'assets\images\buttons\button.png', (300, 100))
        button = [
            Button(BUTTONIMAGE, (300, 100), ((SCREENWIDTH - 300)//2, (SCREENHEIGHT - 100)//2 - 150), 'Computer'),
            Button(BUTTONIMAGE, (300, 100), ((SCREENWIDTH - 300)//2, (SCREENHEIGHT - 100)//2), 'Multiplayer'),
            Button(BUTTONIMAGE, (300, 100), ((SCREENWIDTH - 300)//2, (SCREENHEIGHT - 100)//2 + 150), 'Quit')
        ]

        for buttons in button:
            if buttons.name in ['Computer', 'Multiplayer', 'Quit']:
                buttons.active = True
                buttons.draw(window, False)
            else:
                buttons.active = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for buttonx in button:
                        if buttonx.rect.collidepoint(pygame.mouse.get_pos()):
                            if buttonx.name == 'Computer' and buttonx.active:
                                BUTTONSOUND.play()
                                computer(window)
                            elif buttonx.name == 'Multiplayer' and buttonx.active:
                                BUTTONSOUND.play()
                                multiplayer()
                            elif buttonx.name == 'Quit' and buttonx.active:
                                BUTTONSOUND.play()
                                menu_main(GAMESCREEN)
        pygame.display.update()

def option(window):
    print("Option screen")

def computer(window):
    print("Play with computer")
    while True:
        bgcomputer = pygame.image.load(r'assets\images\background\Destroyer.jpg')
        bgcomputer = pygame.transform.scale(bgcomputer, (SCREENWIDTH, SCREENHEIGHT))
        window.blit(bgcomputer, (0, 0))

        textcomputer = get_font(100).render(" COMPUTER PLAY ", True, "Black")
        testrect = textcomputer.get_rect(center=((SCREENWIDTH) // 2, (SCREENHEIGHT) // 6))
        window.blit(textcomputer, testrect)

        BUTTONIMAGE = load_image(r'assets\images\buttons\button.png', (300, 100))
        button = [
            Button(BUTTONIMAGE, (300, 100), ((SCREENWIDTH - 300) // 2, (SCREENHEIGHT - 100) // 2 - 150), 'Game Type One - Easy'),
            Button(BUTTONIMAGE, (300, 100), ((SCREENWIDTH - 300) // 2, (SCREENHEIGHT - 100) // 2), 'Game Type One - Hard'),
            Button(BUTTONIMAGE, (300, 100), ((SCREENWIDTH - 300) // 2, (SCREENHEIGHT - 100) // 2 + 150), 'Quit')
        ]

        for buttons in button:
            if buttons.name in ['Game Type One - Easy', 'Game Type One - Hard', 'Quit']:
                buttons.active = True
                buttons.draw(window, False)
            else:
                buttons.active = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for buttonx in button:
                        if buttonx.rect.collidepoint(pygame.mouse.get_pos()):
                            if buttonx.name == 'Game Type One - Easy' and buttonx.active:
                                BUTTONSOUND.play()
                                start_game_typeone_easy(window)
                            elif buttonx.name == 'Game Type One - Hard' and buttonx.active:
                                BUTTONSOUND.play()
                                start_game_typeone_hard(window)
                            elif buttonx.name == 'Quit' and buttonx.active:
                                BUTTONSOUND.play()
                                play(window)
                                sys.exit()
        pygame.display.update()

def start_game_typeone_easy(window):
    print("Play game type one easy")
    game = BattleShips_TypeOne()

    game.start_game(window, 1)
    if game.playerchoice == 1:
        start_game_typeone_easy(window)
    elif game.playerchoice == 0:
        computer(window)

def start_game_typeone_hard(window):
    print("Play game type one hard")
    game = BattleShips_TypeOne()

    game.start_game(window, 2)
    if game.playerchoice == 1:
        start_game_typeone_hard(window)
    elif game.playerchoice == 0:
        computer(window)

def multiplayer():
    print("Play multiplayer")
menu_main(GAMESCREEN)

pygame.quit()