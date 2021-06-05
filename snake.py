import pygame
import random
import time

pygame.init()

width = 800
height = 600

#create the screen
dis= pygame.display.set_mode((width,height))
pygame.display.update()
pygame.display.set_caption('Welcome to Snake')
fontStyle = pygame.font.SysFont('comicsans', 35)


#color variables
snakeColor= (0,0,255) # blue snake
foodColor= (255, 0, 0) # red food
backgroundColor = (150,150,150) # grey background
messageColor = (0,0,0) #black


clock = pygame.time.Clock()

# Functions for keeping score, creating the snake, and displaying messages
def yourScore(score):
    value = fontStyle.render('Score: ' + str(score), True, messageColor)
    dis.blit(value,[0,0])
def ourSnake(snake_block,snakeList):
    for x in snakeList:
        pygame.draw.rect(dis, snakeColor,[x[0],x[1], snake_block,snake_block])
def message(msg,color):
    mesg = fontStyle.render(msg,True, color)
    dis.blit(mesg,[width/6, height/3])

# main game logic function
def Game():
    #Snake position and movement variables
    x1 = width/2
    y1 = height/2
    x1_change = 0
    y1_change = 0
    snake_block = 10
    snake_speed = 10


    # Food variables
    #Start in random position
    foodx = round(random.randrange(0, width-snake_block)/10)*10
    foody = round(random.randrange(0, height-snake_block)/10)*10


    #used to keep track of the snake as it gets longer
    snakeList = []
    snakeLength = 1

    gameOver = False
    gameClose = False
    while not gameClose:
        while gameOver:
            message('You Lost! Press F to start a new game! Press X to exit', messageColor)
            yourScore(snakeLength - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        gameClose = True
                        gameOver = False
                    if event.key == pygame.K_f:
                        Game()


        #Handle keyboard input for quitting game and moving snake
        #snake can be moved with arrow buttons or WASD keys
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameClose = True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = snake_block

        #Check Lose conditions
        # if snake goes off the edge of display
        if x1 < 0 or x1 > width or y1 < 0 or y1 > height:
            gameOver = True

        x1 +=x1_change
        y1 += y1_change

        dis.fill(backgroundColor)
        pygame.draw.rect(dis, foodColor, [foodx,foody, snake_block, snake_block])
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)

        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        #check if snake has bit itself
        # check all x except for the last one which
        # is the head
        for x in snakeList[:-1]:
            if x == snakeHead:
                gameOver = True

        ourSnake(snake_block, snakeList)
        yourScore(snakeLength - 1)


        pygame.display.update()

        # Place new food and update length of the snake when food is eaten
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width-snake_block)/10)*10
            foody = round(random.randrange(0, height-snake_block)/10)*10
            snakeLength += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()

Game()
