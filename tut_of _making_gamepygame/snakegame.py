import pygame
import random
pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

#display variables
DIS_HEIGHT=500
DIS_WIDTH=800
game_window=pygame.display.set_mode((DIS_WIDTH,DIS_HEIGHT))
pygame.display.set_caption("SNAKES")


#game variables
game_over=False
game_exit=False
fps=30
scrore=0

#score
font = pygame.font.SysFont(None, 55)
def text_score(text, color, x ,y):
    screen_text = font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

# snake
snakegetX=DIS_WIDTH/2
snakegetY=DIS_HEIGHT/2
headsize=20
velocityx=0
velocityy=0
snakelist=[]
snakelength=1
def plotsnake(game_window, black, snakelist, headsize):
    for x,y in snakelist:
        pygame.draw.rect(game_window, black, [x, y, headsize, headsize])

# food
foodx=random.randint(DIS_WIDTH/5,4*DIS_WIDTH/5)
foody=random.randint(DIS_HEIGHT/5,4*DIS_HEIGHT/5)
foodsize=20


clock=pygame.time.Clock()

#game loop
while not game_exit:
    for event in pygame.event.get():
            # print(event)

            if event.type==pygame.QUIT:
                game_exit=True

            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_UP:
                    velocityy=4
                    velocityx=0
                elif  event.key== pygame.K_RIGHT:
                    velocityy=0
                    velocityx=4
                elif event.key == pygame.K_LEFT:
                    velocityy = 0
                    velocityx = -4
                elif event.key == pygame.K_DOWN:
                    velocityy = -4
                    velocityx = 0
                elif event.key == pygame.K_x:
                    game_exit=True

    if abs(snakegetY-foody)<(foodsize+headsize)/2 and abs(snakegetX-foodx)<(foodsize+headsize)/2:
        scrore+=1
        snakelength+=5
        foodx = random.randint(DIS_WIDTH / 5, 4 * DIS_WIDTH / 5)
        foody = random.randint(DIS_HEIGHT / 5, 4 * DIS_HEIGHT / 5)
        # print("score",scrore)

    snakegetX+=velocityx
    snakegetY-=velocityy
    game_window.fill(white)

    head=[]
    head.append(snakegetX)
    head.append(snakegetY)
    snakelist.append(head)

    text_score("Score: " + str(scrore * 10), black, 50, 50)
    # pygame.draw.rect(game_window, black, [snakegetX,snakegetY,headsize,headsize])
    plotsnake(game_window, black, snakelist, headsize)

    pygame.draw.rect(game_window, red, [foodx, foody, foodsize,foodsize])

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()