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
font_title = pygame.font.Font("assets/flickdemo.ttf", 30)

# Colours

WHITE = (255, 255, 255)
GREY = (127, 130, 128)
BLUE = (50, 50, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (68, 152, 242)
PURPLE = (181, 33, 129)


# Classes Setup

class Button:
     def __init__(self, text, x_pos, y_pos, height, width, font_title, enabled, bg_colour=WHITE, bd_colour=BLACK, hover_colour=WHITE):
         self.text = text
         self.x_pos = x_pos
         self.y_pos = y_pos
         self.enabled = enabled 
         self.height = height
         self.width = width
         self.bg_colour = bg_colour
         self.bd_colour = bd_colour
         self.hover_colour = hover_colour

     def draw(self):
         button_text = font_title.render(self.text, True, (0, 0, 0))
         button_rect = pygame.Rect((self.x_pos, self.y_pos), (self.width, self.height))

         if self.is_clicked() or self.is_hovered():
            pygame.draw.rect(screen, self.hover_colour, button_rect, border_radius=14)

         else:
            pygame.draw.rect(screen, self.bg_colour, button_rect, border_radius=14)
        
         pygame.draw.rect(screen, self.bd_colour, button_rect, 2, border_radius=14)
         text_rect = button_text.get_rect(center=button_rect.center)
         screen.blit(button_text, text_rect)

     def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

        return left_click and button_rect.collidepoint(mouse_pos) and self.enabled


     def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        return pygame.Rect(self.x_pos, self.y_pos, self.width, self.height).collidepoint(mouse_pos)
    



# Launch Screen Background Image Loading

launch_bg = pygame.image.load("images/kb_launchscreen.jpg")
launch_bg = pygame.transform.scale(launch_bg, (WIDTH, HEIGHT))


# Launch Screen Buttons 

newgame_button = Button("New Game",155, 450, 40, 200, font_title, True, (50, 50, 255))
continuegame_button = Button("Continue", 155, 505, 40, 200, font_title, True, (181, 33, 129))


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

