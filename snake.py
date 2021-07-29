import random
import pygame
from pygame.locals import *

#Initialize variables
metadata = {'render.modes': ['human'],
                'video.frames_per_second':20}
TITLE = "Snake"
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

VEL = 100
UNIT = 10
HEAD = 0
X = 0
Y = 1
SIZE_X_GRID = 600
SIZE_Y_GRID = 600
START_X_POS = 200
START_Y_POS = 200

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 128) 

def generateApple(maxX,maxY):
    return (random.randint(0,maxX/10)*10,random.randint(0,maxY/10)*10)

pygame.init()
clock = pygame.time.Clock()


screen = pygame.display.set_mode((SIZE_X_GRID,SIZE_Y_GRID))
screen.fill(BLACK)
pygame.display.set_caption(TITLE)

snake = [(START_X_POS,START_Y_POS), (START_X_POS+UNIT,START_Y_POS), (START_X_POS+(2*UNIT),START_Y_POS)]
snake_skin = pygame.Surface((UNIT,UNIT))
snake_skin.fill(WHITE)

apple_pos = generateApple(SIZE_X_GRID, SIZE_Y_GRID)
apple_skin = pygame.Surface((UNIT,UNIT))
apple_skin.fill(RED)

print("Apple position: ", apple_pos)

font = pygame.font.Font(pygame.font.get_default_font(), 36)

# now print the text
text_surface = font.render('Game Over!', True, GREEN)


my_direcction = LEFT
game_over = False
score = 0

while not game_over:

    pygame.display.set_caption(TITLE + " (Score: " + str(score) + ")")
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_direcction = LEFT
            if event.key == pygame.K_RIGHT:
                my_direcction = RIGHT
            if event.key == pygame.K_UP:
                my_direcction = UP
            if event.key == pygame.K_DOWN:
                my_direcction = DOWN    
    
    #Snake next move
    move = (0,0)
    if my_direcction == LEFT:
        move = (-UNIT,0)
    elif my_direcction == RIGHT:
        move = (UNIT,0)
    elif my_direcction == UP:
        move = (0,-UNIT)
    elif my_direcction == DOWN:
        move = (0,UNIT)

    #Clean screen
    screen.fill(BLACK)

    #Paint apple
    screen.blit(apple_skin, apple_pos)

    #Paint snake
    #pygame.time.delay(VEL)
    clock.tick(metadata["video.frames_per_second"])

    snake_copy = snake.copy()

    for index in range(len(snake)):
        screen.blit(snake_skin, snake[index])

        if index == HEAD:
            #Snake will eat the apple
            if snake[index] == apple_pos:
                score += 1
                snake.insert(0, apple_pos)
                apple_pos = generateApple(SIZE_X_GRID, SIZE_Y_GRID)
            
            #Move the head
            snake[index] = (snake[index][X] + move[X], snake[index][Y] + move[Y])
        else:
            #Move all the entire body
            snake[index] = snake_copy[index-1]
    
    #Validate the game rules
    if snake[HEAD][X] < 0 or snake[HEAD][X] >= SIZE_X_GRID:
        game_over = True
    if snake[HEAD][Y] < 0 or snake[HEAD][Y] >= SIZE_Y_GRID:
        game_over = True

    pygame.display.update()

if game_over:
    screen.blit(text_surface, dest=(SIZE_X_GRID//2-100,SIZE_Y_GRID//2))
    pygame.display.update()
    pygame.time.delay(2000)