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
font = pygame.font.Font("assets/gilroy.ttf", 20)

# Colours

WHITE = (255, 255, 255)
GREY = (127, 130, 128)
BLUE = (50, 50, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (68, 152, 242)
PURPLE = (181, 33, 129)


# Load Popup Image Background 
popup_bg = pygame.image.load("images/kb_popup.jpg")
popup_bg = pygame.transform.scale(popup_bg, (400, 400))
opup_bg = pygame.image.load("images/kb_popup.jpg").convert_alpha()


# Launch Screen Background Image Loading

launch_bg = pygame.image.load("images/kb_launchscreen.jpg")
launch_bg = pygame.transform.scale(launch_bg, (WIDTH, HEIGHT))



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

class Popup:
    def __init__(self, x_pos, y_pos, message, bg_image, true_callback, false_callback=None, label_one="Yes", label_two="No", width=400, height=400, font_size=20, visible=True):
        self.message = message
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.bg_image = pygame.transform.scale(popup_bg, (width, height))
        self.true_callback = true_callback
        self.false_callback = false_callback
        self.label_one = label_one
        self.label_two = label_two
        self.width = width
        self.height = height
        self.font_size = font_size
        self.font = font
        self.visible = visible


        button_width = 120
        button_height = 50
        padding = 30

        self.button_one = Button(self.label_one, self.x_pos + (self.width // 2) - button_width - (padding // 2), self.y_pos + self.height - button_height - 20, button_height, button_width, font, True)
        self.button_two = Button(self.label_two, self.x_pos + (self.width // 2) + (padding // 2), self.y_pos + self.height - button_height - 20, button_height, button_width, font, True)

    def draw(self, surface):
        if self.visible == False:
            return
            
        popup_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        surface.blit(self.bg_image, popup_rect)

        pygame.draw.rect(surface, (0,0,0), popup_rect, 2, border_radius=14)

        message_text = self.font.render(self.message, True, (0,0,0))
        message_rect = message_text.get_rect(center=(self.x_pos + self.width // 2, self.y_pos + self.height // 2 - 30))
        surface.blit(message_text, message_rect)

        self.button_one.draw()
        self.button_two.draw()   


    def event_handler(self, event):
        if self.visible == False:
            return
            
        if self.button_one.is_clicked():
            self.true_callback()
            self.visible = False
            
        elif self.button_two.is_clicked():
            self.false_callback()
            self.visible = False



# Launch Screen Buttons 

newgame_button = Button("New Game",155, 450, 40, 200, font_title, True, (50, 50, 255))
continuegame_button = Button("Continue", 155, 505, 40, 200, font_title, True, (181, 33, 129))


# Drawing Launch Screen
def draw_launchscreen():
    screen.blit(launch_bg, (0,0))
    newgame_button.draw()
    continuegame_button.draw()
    pygame.display.update()


# New Game Function

def newgame():
    print("New Game")


def cancel_newgame():
    print("Cancelled")



# Popup For The Menu Screen

newgame_popup = Popup(x_pos=400, y_pos=184, width=400, height=400, label_one="Continue", label_two="Cancel", true_callback=newgame, false_callback=cancel_newgame, bg_image=popup_bg, message="All your past progress will be lost if you start a new game, are you sure you want to continue?")


# Main Game Loop

while running:

    # Launch Screen

    draw_launchscreen()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if newgame_popup.visible:
            newgame_popup.event_handler(event)

    if newgame_popup.visible:
        newgame_popup.draw(screen)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()

