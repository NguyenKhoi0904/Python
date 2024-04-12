import pygame

from button import Button

SCREENWIDTH = 1530
SCREENHEIGHT = 775
NUMROWS = 10
NUMCOLS = 10
cellSizeY = (SCREENHEIGHT // 2) // (NUMROWS)
cellSizeX = (SCREENWIDTH // 2) // (NUMCOLS)
CELLSIZE = cellSizeY
STAGE = ['Main Menu', 'Deployment', 'Game Over']
GAMESTATE = 'Main Menu'
GAMESCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Battle Ships')
icon = pygame.image.load(r'assets\images\background\icon.png')
pygame.display.set_icon(icon)

bg = None

GAMESTATE = 'Main Menu'
STAGE = ['Main Menu', 'Deployment', 'Game Over']
def load_image(path, size, rotate=False):
    """A function to import the images into memory"""
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, size)
    if rotate:
        img = pygame.transform.rotate(img, -90)
    return img

def load_animation_images(path, aniNum, size):
    """Load in stipulated number of images to memory"""
    imageList = []
    for num in range(aniNum):
        if num < 10:
            imageList.append(load_image(f'{path}00{num}.png', size))
        elif num < 100:
            imageList.append(load_image(f'{path}0{num}.png', size))
        else:
            imageList.append(load_image(f'{path}{num}.png', size))
    return imageList

def load_sprite_sheet_images(spriteSheet, rows, cols, newSize, size):
    image = pygame.Surface((128, 128))
    image.blit(spriteSheet, (0, 0), (rows * size[0], cols * size[1], size[0], size[1]))
    image = pygame.transform.scale(image, (newSize[0], newSize[1]))
    image.set_colorkey((0, 0, 0))
    return image

def increase_animation_image(imageList, ind):
    return imageList[ind]

def mainMenuScreen(window, game):
    GAMESCREEN.blit(bg, (0, 0))

    for button in game.button:
        if button.name in ['Easy Computer', 'Hard Computer']:
            button.active = True
            button.draw(window, game.deployment)
        else:
            button.active = False

def deploymentScreen(window, game):
    window.fill((0, 0, 0))

    window.blit(BACKGROUND, (0, 0))
    window.blit(game.pgamegriding, (game.cellSize1//2, game.cellSize1//2))
    window.blit(game.cgamegriding, (game.cGameGrid[0][0][0] - game.cellSize, game.cGameGrid[0][0][1] - game.cellSize))

    #  Draws the player and computer grids to the screen
    game.show_grid_onscreen(GAMESCREEN)
    game.show_ship_onscreen(GAMESCREEN, game.cFleet, game.cGameGrid)
    #  Draw ships to screen
    game.show_ship_onscreen(GAMESCREEN, game.pFleet, game.pGameGrid, True)

    game.show_ship_onscreen(GAMESCREEN, game.cFleet, game.cGameGrid, True)

    game.show_button_onscreen(GAMESCREEN, game.button)

    #computer.draw(window)

    game.show_radar_scanner_onscreen(window)
    game.show_radar_blip_onscreen(window)

    game.show_token_onscreen(GAMESCREEN, game.tokens)

    game.update_pgame_logic(game.pGameGrid, game.pFleet)
    game.update_cgame_logic(game.cGameGrid, game.cFleet)


def endScreen(window, game):
    window.fill((0, 0, 0))

    window.blit(ENDSCREENIMAGE, (0, 0))


    for button in game.button:
        if button.name in ['Easy Computer', 'Hard Computer', 'Quit']:
            button.active = True
            button.draw(window, game.deployment)
        else:
            button.active = False


def updateGameScreen(window, game, type):
    # game.show_grid_onscreen(GAMESCREEN)
    # game.show_ship_onscreen(GAMESCREEN, game.pFleet, game.pGameGrid, True)
    # game.show_ship_onscreen(GAMESCREEN, game.cFleet, game.cGameGrid, True)
    # game.show_button_onscreen(GAMESCREEN, game.button)
    # game.show_token_onscreen(GAMESCREEN, game.tokens)
    # game.update_pgame_logic(game.pGameGrid, game.pFleet)
    # game.update_cgame_logic(game.cGameGrid, game.cFleet)
    # game.show_radar_scanner_onscreen(window)
    # game.show_radar_blip_onscreen(window)

    if type == 1:
        mainMenuScreen(window, game)
    elif type == 2:
        deploymentScreen(window, game)
    elif type == 3:
        endScreen(window, game)

    pygame.display.update()

def get_font(size):
    return pygame.font.Font("assets/images/font/font.ttf", size)

MAINMENUIMAGE = load_image(r'assets/images/background/Battleship.jpg', (SCREENWIDTH // 3 * 2, SCREENHEIGHT))
ENDSCREENIMAGE = load_image(r'assets/images/background/Carrier.jpg', (SCREENWIDTH, SCREENHEIGHT))
BACKGROUND = load_image(r'assets/images/background/gamebg.png', (SCREENWIDTH, SCREENHEIGHT))
pygame.mixer.init()
HITSOUND = pygame.mixer.Sound(r'assets\sounds\sounds\explosion.wav')
HITSOUND.set_volume(0.05)
SHOTSOUND = pygame.mixer.Sound(r'assets\sounds\sounds\gunshot.wav')
SHOTSOUND.set_volume(0.05)
MISSSOUND = pygame.mixer.Sound(r'assets\sounds\sounds\splash.wav')
MISSSOUND.set_volume(0.05)
BUTTONSOUND = pygame.mixer.Sound(r'assets\sounds\sounds\buttonsound.mp3')
BUTTONSOUND.set_volume(10)