import pygame
import time

pygame.init()

surface_width = 1280
surface_height = 720

SURFACE = pygame.display.set_mode((surface_width, surface_height))
pygame.display.set_caption('hiihhi')
FPSCLOCK = pygame.time.Clock()

#Howtoplay를 위한 이미지들!
back_button = ("image/surface/Back_button.png")
back_button_act = ("image/surface/Back_button_act.png")

#play를 위한 이미지들!
#background_image = ("") #만들기

#main_menu,play 캐릭터들
sprite_img = pygame.image.load("image/characters/sprite.PNG")
ham_zzizzi = pygame.image.load("image/characters/hamster_zzizzi_success.png")
start_button = pygame.image.load("image/surface/start_button.png")
start_button_act = pygame.image.load("image/surface/start_button_clicked.png")
howtoplay_button = pygame.image.load("image/surface/howtoplay_button.png")
howtoplay_button_act = pygame.image.load("image/surface/howtoplay_button_act.png") 
penguin_smile = pygame.image.load("image/characters/penguin_smile.png")
#robby = pygame.image.load("E:/gongmo/image/surface/Robby.png") //만들어야함!

class Button():
    def __init__(self, img, x, y, width, height, img_act, x_act, y_act, act=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            SURFACE.blit(img_act, (x_act, y_act))
            
            if click[0] and act != None:
                act()
        else:
            SURFACE.blit(img, (x, y))
            
def main_menu():
    
    font = pygame.font.Font("font/DungGeunMo.ttf", 100)
    game_title = font.render("ㅋ", True, (0,0,0))
    
    while True:
        for event in pygame.event.get():
            SURFACE.fill('#5CACEE') 
            SURFACE.blit(game_title, (430, 150))
                
            Button(howtoplay_button, 512, 420, 256, 144, howtoplay_button_act, 512,420, Explain_game)
                
            if event.type == pygame.QUIT:
                pygame.quit()
                     
        pygame.display.update()
        FPSCLOCK.tick(30)

def Explain_game():
    #font = pygame.font.Font("ㅋ")
    while True:
        for event in pygame.event.get():
            SURFACE.fill('#FFAEB9')
            
            Button(start_button, 1000, 560, 256, 144, start_button_act, 1000, 560, main_game)
            
            if event.type == pygame.QUIT:
                pygame.quit()
                
        pygame.display.update()
        FPSCLOCK.tick(30)
 
def main_game():
    x_move = 0
    y_move = 0
    x_pos = 0
    y_pos = 0

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_pos = -5
                elif event.key == pygame.K_d:
                    x_pos = 5
                elif event.key == pygame.K_w:
                    y_pos = -5
                elif event.key == pygame.K_s:
                    y_pos = 5
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    y_pos = 0
                elif event.key == pygame.K_s:
                    y_pos = 0
                elif event.key == pygame.K_a:
                    x_pos = 0
                elif event.key == pygame.K_d:
                    x_pos = 0

        x_move += x_pos
        y_move += y_pos

        SURFACE.fill('#00B9FF')
        SURFACE.blit(sprite_img, (x_move, y_move))

        pygame.display.update()
        FPSCLOCK.tick(30)

main_menu()