import main
import pygame
import time

# Makes the game window.
pygame.init()
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("Luigi's Casino")
pygame.display.set_icon(pygame.image.load("assets/LuigiLogic.png"))


# Load fonts and images.
pokertable = pygame.image.load("assets/TableBackground.jpg").convert()
pokertable = pygame.transform.smoothscale_by(pokertable, 0.5)
superfont = pygame.font.Font("assets/SuperMario256.ttf", size = 42)
titletext = superfont.render("Welcome to Luigi's Casino!\nTesting!", True, (255, 255, 255))
text_rect = titletext.get_rect(center=(1500 // 2, 50))


# Button class, to make buttons.
class Button():
    def __init__(self, x, y, image, scale=1):
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = self.image.get_rect(center=(x, y))
        self.clicked = False
        


    def draw(self):
        # Drawing the button on screen
        screen.blit(self.image, self.rect)
    
    def click(self):
        action = False

        # Getting the mouse position, and checking if it's over the button
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            action = False

        return action


    
tbuttonimg = pygame.image.load("assets/Testbutton.png").convert_alpha()
tbutton = Button(750, 500, tbuttonimg, .5)

# Button to swap music tracks
music_toggle_image = pygame.image.load("assets/MusicSwitcher.png").convert()
music_toggle_button = Button(120, 880, music_toggle_image, .35)
music_tracks = ["assets/LuigiBalatro.mp3", "assets/Pi'illoCastle.mp3"]
selected_track = 0




# Infinite music loop. Rejoice!
pygame.mixer.music.load(music_tracks[selected_track])
pygame.mixer.music.set_volume(.75)
pygame.mixer.music.play(-1)

# Game loop!
running = True
while running:
    screen.blit(pokertable, (0, 0))
    screen.blit(titletext, text_rect)
    tbutton.draw()
    music_toggle_button.draw()
    
    if tbutton.click():
        print("Clicked!")

    if music_toggle_button.click():
        if selected_track == len(music_tracks)-1:\
            selected_track = 0
        else:
            selected_track += 1
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_tracks[selected_track])
        pygame.mixer.music.play(-1)



    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()