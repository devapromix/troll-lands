from common.colors import *

def out(t, x, y, font, screen):
    text_surface, rect = font.render(str(t), DEFAULT_COLOR)
    screen.blit(text_surface, (x, y))
    #font.render_to(screen, (x, y), t, def_color)
    
