#tank game
#color chart https://www.w3schools.com/colors/colors_picker.asp
#music MASTER BOOT RECORD https://www.youtube.com/watch?v=s1522TU8qeE
#sprites https://www.pygame.org/docs/tut/SpriteIntro.html
#similar https://codereview.stackexchange.com/questions/117875/space-shooter-made-using-pygame

import pygame, sys, random, time

#colors
colors = {'red' : pygame.Color(255, 0, 0),
        'green' : pygame.Color(0, 255, 0),
        'blue' : pygame.Color(0, 0, 255),
        'black' : pygame.Color(0, 0, 0),
        'white' : pygame.Color(255, 255, 255),
        'brown' : pygame.Color(165, 42, 42),
        'tan' : pygame.Color(255, 204, 102)}


#vehic class
class vehic(object):
    #attributes name, hp, fuel, armor, ammo, 
    #acceleration

    def __init__(self, name, hp, fuel, armor, ammo, posx, posy, max_speed, direction):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.ammo = ammo
        self.posx = posx
        self.posy = posy
        self.max_speed = max_speed
        self.barrel = direction


#base class for attacks
class shot(object):
    #attributes x, y, distance, direction, acceleration

    def __init__(self, posx, posy, direction, distance, speed):
        self.posx = posx
        self.posy = posy
        self.direction = direction
        self.distance = distance
        self.speed = speed

#inherits from shot
class fan(shot):
    #fan in deg
    def __init__(self, posx, posy, direction, distance, speed, fan):
        self.posx = posx
        self.posy = posy
        self.direction = direction
        self.distance = distance
        self.speed = speed
        self.fan = fan

class package(object):
    #attributes support type, amount

    def __init__(self, sup_type, amount, posx, posy):
        self.sup_type = sup_type
        self.amount = amount
        self.posx = posx
        self.posy = posy

# Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game Over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 20)
    playSurface.blit(GOsurf,GOrect) 
    pygame.display.flip()
    time.sleep(4)
    pygame.quit() #pygame exit
    sys.exit() #console exit

       

#import variables


#direction = 'RIGHT'
#changeto = direction

   #main game logic
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
    playSurface = pygame.display.set_mode((800,800))
    pygame.display.set_caption('Tanks')
    foodPos = [random.randrange(1,72)*10 ,random.randrange(1,46)*10]
    foodSpawn = True
     
    #frame controller
    fpsController = pygame.time.Clock()


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
