from common.colors import *

def out(text, x, y, font, screen):
    text_surface, rect = font.render(str(text), DEFAULT_COLOR)
    screen.blit(text_surface, (x, y))
    #font.render_to(screen, (x, y), t, def_color)
    
def out_list(list, x, y, font, screen):
    for i, line in enumerate(list):
        out(line, x, y + (i * 30), font, screen)