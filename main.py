import sys, os, pygame, json
from common.colors import *
from common.constants import *
from common.engine import *

pygame.init()

screen = pygame.display.set_mode((1200, 600))
font = pygame.freetype.Font("assets/fonts/font.ttf", 32)

pygame.display.set_caption(GAME_TITLE)
pygame.display.set_icon(pygame.image.load("assets/icons/game.ico"))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    out(GAME_TITLE, 10, 10, font, screen)
    
    f = open("assets/data/lands.json")
    lands = json.load(f)
    out(lands["title"], 10, 50, font, screen)
    out(lands["descr"], 10, 80, font, screen)
    
    pygame.display.flip()













