import main
import random
from main import deck
from main import balance
from main import draw_cards
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

superfont = pygame.font.Font("assets/SuperMario256.ttf", size = 46)

titletext = superfont.render("Welcome to three card poker!", True, (255, 255, 255))
titletext2 = pygame.font.Font("assets/SuperMario256.ttf", size = 35).render("Please input an ante value below.", True, (255, 255, 255))


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

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x - w // 2, y - h // 2, w, h)
        self.color = pygame.Color('lightskyblue3')
        self.text = text
        self.txt_surface = pygame.font.Font("assets/SuperMario256.ttf", size = 35).render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = pygame.Color('dodgerblue2') if self.active else pygame.Color('lightskyblue3')
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    global input_text
                    input_text = self.text
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = pygame.font.Font("assets/SuperMario256.ttf", size = 35).render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

def music_toggle():
    global music_tracks
    global selected_track
    if music_toggle_button.click():
            if selected_track == len(music_tracks)-1:
                selected_track = 0
            else:
                selected_track += 1
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_tracks[selected_track])
            pygame.mixer.music.play(-1)
    
def set_card_sprites(hand):
    global deck
    deck_sprites = ["assets/ASpades.png",
                "assets/cards/2Spades.png",
                "assets/cards/3Spades.png",
                "assets/cards/4Spades.png",
                "assets/cards/5Spades.png",
                "assets/cards/6Spades.png"
                "assets/cards/7Spades.png",
                "assets/cards/8Spades.png",
                "assets/cards/9Spades.png",
                "assets/cards/10Spades.png",
                "assets/cards/JSpades.png",
                "assets/cards/QSpades.png",
                "assets/cards/KSpades.png",
                
                "assets/cards/AClubs.png",
                "assets/cards/2Clubs.png",
                "assets/cards/3Clubs.png",
                "assets/cards/4Clubs.png",
                "assets/cards/5Clubs.png",
                "assets/cards/6Clubs.png"
                "assets/cards/7Clubs.png",
                "assets/cards/8Clubs.png",
                "assets/cards/9Clubs.png",
                "assets/cards/10Clubs.png",
                "assets/cards/JClubs.png",
                "assets/cards/QClubs.png",
                "assets/cards/KClubs.png",
                
                "assets/cards/ADiamonds.png",
                "assets/cards/2Diamonds.png",
                "assets/cards/3Diamonds.png",
                "assets/cards/4Diamonds.png",
                "assets/cards/5Diamonds.png",
                "assets/cards/6Diamonds.png"
                "assets/cards/7Diamonds.png",
                "assets/cards/8Diamonds.png",
                "assets/cards/9Diamonds.png",
                "assets/cards/10Diamonds.png",
                "assets/cards/JDiamonds.png",
                "assets/cards/QDiamonds.png",
                "assets/cards/KDiamonds.png",
                
                "assets/cards/AHearts.png",
                "assets/cards/2Hearts.png",
                "assets/cards/3Hearts.png",
                "assets/cards/4Hearts.png",
                "assets/cards/5Hearts.png",
                "assets/cards/6Hearts.png"
                "assets/cards/7Hearts.png",
                "assets/cards/8Hearts.png",
                "assets/cards/9Hearts.png",
                "assets/cards/10Hearts.png",
                "assets/cards/JHearts.png",
                "assets/cards/QHearts.png",
                "assets/cards/KHearts.png",]
    
    return [deck_sprites[deck.index(hand[0])], deck_sprites[deck.index(hand[1])], deck_sprites[deck.index(hand[2])]]

# Button to swap music tracks
music_toggle_image = pygame.image.load("assets/MusicSwitcher.png").convert()
music_toggle_button = Button(120, 880, music_toggle_image, .35)
music_tracks = ["assets/LuigiBalatro.mp3",
                "assets/Pi'illoCastle.mp3",
                "assets/CastleFunk.mp3",
                "assets/ToadTownBowser.mp3"]
selected_track = 0




# Infinite music loop. Rejoice!
pygame.mixer.music.load(music_tracks[selected_track])
pygame.mixer.music.set_volume(.75)
pygame.mixer.music.play(-1)

# Develops the main screen, then copies it for later use.
screen.blit(pokertable, (0, 0))
screen.blit(titletext, titletext.get_rect(center=(1500 // 2, 50)))
music_toggle_button.draw()
start_screen = screen.copy()


# Makes an input box using the defined class.
anteinput = InputBox(700, 500, 100, 40)


# Game loop!
running = True
input_text = ""
while running:
    # Loop 1: ante selector
    ante_unselected = True
    while ante_unselected:
        screen.blit(start_screen, (0, 0))
        balancetext = pygame.font.Font("assets/SuperMario256.ttf", size = 30).render(f"Balance: {balance} Chips", True, (255, 255, 255))
        screen.blit(balancetext, balancetext.get_rect(center=(1300, 950)))
        music_toggle()

        screen.blit(titletext2, titletext2.get_rect(center=(1500 // 2, 450)))
        anteinput.draw()
        anteinput.update()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            anteinput.handle_event(event)

        if input_text != "":
            try:
                if float(input_text) == int(input_text):
                    if (int(input_text) > 0) and (int(input_text) <= balance):
                        ante_unselected = False
                        ante = int(input_text)
                        input_text = ""
                    else:
                        titletext2 = pygame.font.Font("assets/SuperMario256.ttf", size = 35).render("Invalid ante. Please make sure your ante is within your balance.", True, (255, 255, 255))
                        input_text = ""
                else:
                    titletext2 = pygame.font.Font("assets/SuperMario256.ttf", size = 35).render("Invalid ante. Please input an integer.", True, (255, 255, 255))
                    input_text = ""
            except:
                titletext2 = pygame.font.Font("assets/SuperMario256.ttf", size = 35).render("Invalid ante. Please input an integer.", True, (255, 255, 255))
                input_text = ""

        pygame.display.flip()

    # Loop two: card phase
    card_draw_phase = True
    player_hand, cpu_hand =  draw_cards()
    player_hand_sprites = set_card_sprites(player_hand)
    cpu_hand_sprites = set_card_sprites(cpu_hand)

    cpu_card_1 = pygame.transform.scale_by(pygame.image.load("assets/cards/CardBack.png").convert_alpha(), 2.5)
    cpu_card_2 = pygame.transform.scale_by(pygame.image.load("assets/cards/CardBack.png").convert_alpha(), 2.5)
    cpu_card_3 = pygame.transform.scale_by(pygame.image.load("assets/cards/CardBack.png").convert_alpha(), 2.5)
    while card_draw_phase:
        screen.blit(start_screen, (0, 0))
        balancetext = pygame.font.Font("assets/SuperMario256.ttf", size = 30).render(f"Balance: {balance} Chips", True, (255, 255, 255))
        screen.blit(balancetext, balancetext.get_rect(center=(1300, 950)))
        music_toggle()

        screen.blit(cpu_card_1, cpu_card_1.get_rect(center = (100, 100)))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()









        pygame.display.flip()



pygame.quit()