import sys, pygame, json

pygame.init()

screen = pygame.display.set_mode((1200, 600))
font = pygame.freetype.Font("assets/fonts/font.ttf", 24)
def_color = (200, 200, 200)

pygame.display.set_caption("Troll Lands")
pygame.display.set_icon(pygame.image.load("assets/icons/game.ico"))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    
    pygame.display.flip()













