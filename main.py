import os
import random
import pygame


# Initialising Pygame

pygame.init()


# The Screen Setup

WIDTH, HEIGHT = 1366, 768
FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KickBall 26")
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont("arial", 35)

# Colours

WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


# Classes Setup

class Button:
     def __init__(self, text, x_pos, y_pos, height, width, font, enabled, bg_colour=WHITE, bd_colour=BLACK):
         self.text = text
         self.x_pos = x_pos
         self.y_pos = y_pos
         self.enabled = enabled 
         self.height = height
         self.width = width
         self.bg_colour = bg_colour
         self.bd_colour = bd_colour

     def draw(self):
         button_text = font.render(self.text, True, (0, 0, 0))
         button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.height, self.width))
         pygame.draw.rect(screen, self.bg_colour, button_rect, 0, 5)
         pygame.draw.rect(screen, self.bd_colour, button_rect, 2, 5)
         screen.blit(button_text, (self.x_pos + 3, self.y_pos + 3))
    



# Launch Screen Background Image Loading

launch_bg = pygame.image.load("images/kb_launchscreen.jpg")
launch_bg = pygame.transform.scale(launch_bg, (WIDTH, HEIGHT))


# Launch Screen Buttons 

newgame_button = Button("New Game",155, 450, 200, 40, font, True, (50, 50, 255))
continuegame_button = Button("Continue", 155, 505, 200, 40, font, True, (181, 33, 129))


# Drawing Launch Screen
def draw_launchscreen():
    screen.blit(launch_bg, (0,0))
    newgame_button.draw()
    continuegame_button.draw()
    pygame.display.update()


# Main Game Loop

while running:

    draw_launchscreen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()

