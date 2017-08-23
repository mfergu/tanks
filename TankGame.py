#tank game
#color chart https://www.w3schools.com/colors/colors_picker.asp
#music MASTER BOOT RECORD https://www.youtube.com/watch?v=s1522TU8qeE
# pygame music https://www.pygame.org/docs/ref/music.html#comment_pygame_mixer_music_load
#sprites http://programarcadegames.com/index.php?chapter=introduction_to_sprites
#sprite libraries https://opengameart.org/content/starter-kits
#similar https://codereview.stackexchange.com/questions/117875/space-shooter-made-using-pygame

import pygame, sys, random, time
from os import path

######################################################
##asset dirs
img_dir = path.join(path.dirname(__file__),'sprites/PNG')
sound_dir = path.join(path.dirname(__file__),'music')

######################################################
WIDTH = 800
HEIGHT = 800
FPS = 60
POWERUP_TIME = 5000

#colors
colors = {'red' : pygame.Color(255, 0, 0),
        'green' : pygame.Color(0, 255, 0),
        'blue' : pygame.Color(0, 0, 255),
        'black' : pygame.Color(0, 0, 0),
        'white' : pygame.Color(255, 255, 255),
        'brown' : pygame.Color(165, 42, 42),
        'tan' : pygame.Color(255, 204, 102)}
######################################################

######################################################
##initialize pygame and create window

check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors,\
    exiting...".format(check_errors[1]))
    sys.exit("-1")
else:
    print("(+) PyGame successfully initialized!")
# setup music
pygame.mixer.init()
#play surface
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tanks')
#frame controller
#for syncing the fps
fpsController = pygame.time.Clock() 
#game font
font_name = pygame.font.match_font('arial')
######################################################
     

def main_menu():
    global screen
    menu_song = pygame.mixer.music.load(path.join(sound_dir, "MBR-DOOM.ogg"))
    pygame.mixer.music.play(-1)

    title = pygame.image.load(path.join(img_dir, "main.jpg")).convert()
    title = pygame.transform.scale(title, (WIDTH, HEIGHT), screen)
    screen.blit(title, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_q or ev.type == pygame.QUIT:
                pygame.quit()
                quit()
        else:
            draw_text(screen, "Press [ENTER] To Begin", 30, WIDTH/2, HEIGHT/2)
            draw_text(screen, "or [Q] to Quit", 30, WIDTH/2, (HEIGHT/2)+40)
            pygame.display.update()

    ready = pygame.mixer.Sound(path.join(sound_dir,'segue.ogg'))
    ready.play()
    screen.fill(colors['black'])
    draw_text(screen, "GET READY!", 40, WIDTH/2, HEIGHT/2)
    pygame.display.update()
    pygame.time.wait(2)
    pygame.mixer.music.stop()


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, colors['white'])
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    pygame.draw.rect(surf, colors['green'], fill_rect)
    pygame.draw.rect(surf, colors['white'], outline_rect, 2)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect= img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)



#vehic class
class vehic(pygame.sprite.Sprite):
    #attributes name, hp, fuel, armor, ammo, 
    #acceleration

    def __init__(self, name, hp, fuel, armor, ammo, posx, posy, max_speed, direction):
        super.init()
        self.name = name
        self.hp = hp
        self.armor = armor
        self.ammo = ammo
        self.posx = posx
        self.posy = posy
        self.max_speed = max_speed
        self.barrel = direction


#base class for attacks
class shot(pygame.sprite.Sprite):
    #attributes x, y, distance, direction, acceleration

    def __init__(self, posx, posy, direction, distance, speed):
        super.init()
        self.posx = posx
        self.posy = posy
        self.direction = direction
        self.distance = distance
        self.speed = speed

#inherits from shot
class fan(pygame.sprite.Sprite):
    #fan in deg
    def __init__(self, posx, posy, direction, distance, speed, fan):
        super.init()
        self.posx = posx
        self.posy = posy
        self.direction = direction
        self.distance = distance
        self.speed = speed
        self.fan = fan

class care_package(pygame.sprite.Sprite):
    #attributes support type, amount

    def __init__(self, sup_type, amount, posx, posy):
        super.init()
        self.sup_type = sup_type
        self.amount = amount
        self.posx = posx
        self.posy = posy

# Game over function
def game_over():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game Over!', True, colors['red'])
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 20)
    screen.blit(GOsurf,GOrect) 
    pygame.display.flip()
    time.sleep(4)
    pygame.quit() #pygame exit
    sys.exit() #console exit

       
main_menu()
game_over()

#import variables


#direction = 'RIGHT'
#changeto = direction
"""

foodPos = [random.randrange(1,80)*10 ,random.randrange(1,80)*10]
foodSpawn = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    changeto = 'RIGHT'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    changeto = 'LEFT'
                if event.key == pygame.K_UP or event.key == ord('w'):
                    changeto = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    changeto = 'DOWN'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

                    
        #direction validation
        if changeto == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'
        if changeto == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if changeto == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if changeto == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'

        if direction == 'RIGHT':
            snakePos[0] += 10
        if direction == 'LEFT':
            snakePos[0] -= 10
        if direction == 'UP':
            snakePos[1] -= 10
        if direction == 'DOWN':
            snakePos[1] += 10

        #snake body mechanics
        snakeBody.insert(0,list(snakePos))
        if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
            foodSpawn = False
        else:
            snakeBody.pop()

        if foodSpawn == False:
            foodPos = [random.randrange(1,72)*10 ,random.randrange(1,46)*10]
        foodSpawn = True

        playSurface.fill(colors['tan'])
        for pos in snakeBody:
            pygame.draw.rect(playSurface, colors['green'], pygame.Rect(pos[0],pos[1],10,10))
                    
        pygame.draw.rect(playSurface, colors['brown'], pygame.Rect(foodPos[0],foodPos[1],10,10))

        if snakePos[0] > 710 or snakePos[0] < 0:
            gameOver()
        if snakePos[1] > 450 or snakePos[1] < 0:
            gameOver()

        for block in snakeBody[1:]:
            if snakePos[0] == block[0] and snakePos[1] == block[1]:
                gameOver()
        pygame.display.flip()
        fpsController.tick(15)
        """
