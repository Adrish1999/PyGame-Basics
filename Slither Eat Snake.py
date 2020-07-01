import pygame
import sys
import time
import random

pygame.init()

white = (255,255,255)
black = (100,0,0)
red = (255,0,0)
window_width = 800
window_height = 600

gameDisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Slither")
font = pygame.font.SysFont(None,25,bold=True)

def myquit():
    pygame.quit()
    sys.exit(0)

#Part 2
clock = pygame.time.Clock()
FPS = 5
blockSize = 20
noPixel = 0
points = 0

#Part 3
def snake(blockSize , snakelist):
    for size in snakelist:
        pygame.draw.rect(gameDisplay,black,[size[0]+5,size[1],blockSize,blockSize],2)

def message_to_screen(msg , color , points):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text , [window_width/4 , window_height/4])
    msg_1 = "Your points is "+str(points)
    screen_text_2 = font.render(msg_1,True,color)
    gameDisplay.blit(screen_text_2,[(window_width/4),(window_height/4)+100])

#Part 4
def gameLoop():
    global points
    gameExit = False
    gameOver = False

    lead_x = window_width/2
    lead_y = window_height/2

    change_pixels_of_x = 0
    change_pixels_of_y = 0

    snakelist = []
    snakeLength = 1

    randomAppleX = round(random.randrange(0,window_width-blockSize))
    randomAppleY = round(random.randrange(0,window_height-blockSize))

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over , press c to play again , q to quit",red,points)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
#Logic 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myquit()
                leftArrow = event.key == pygame.K_LEFT
                rightArrow = event.key == pygame.K_RIGHT
                upArrow = event.key == pygame.K_UP
                downArrow = event.key == pygame.K_DOWN

                if leftArrow:
                    change_pixels_of_x = -blockSize
                    change_pixels_of_y = noPixel
                elif rightArrow:
                    change_pixels_of_x = blockSize
                    change_pixels_of_y = noPixel
                elif upArrow:
                    change_pixels_of_x = noPixel
                    change_pixels_of_y = -blockSize
                elif downArrow:
                    change_pixels_of_x = noPixel
                    change_pixels_of_y = blockSize

#Logic 2
            if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
                gameOver = True

        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y

        gameDisplay.fill(white)

        AppleThickness = 20

#Logic 3
        print([int(randomAppleX),int(randomAppleY),AppleThickness,AppleThickness])
        pygame.draw.rect(gameDisplay,red,[randomAppleX,randomAppleY,AppleThickness,AppleThickness])

        allspriteslist = []

        allspriteslist.append(lead_x)

        allspriteslist.append(lead_y)

        snakelist.append(allspriteslist)

        if len(snakelist) > snakeLength:
            del snakelist[0]

        for eachSegment in snakelist[:-1]:

            if eachSegment == allspriteslist:
                gameOver = True

#Logic 4
        snake(blockSize, snakelist)

        pygame.display.update()
#Logic 5
        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:

            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:
                randomAppleX = round(random.randrange(0, window_width - blockSize) / 10.0) * 10.0

                randomAppleY = round(random.randrange(0, window_height - blockSize) / 10.0) * 10.0

                snakeLength += 1
                points +=1

        clock.tick(FPS)

    pygame.quit()

    quit()


gameLoop()



