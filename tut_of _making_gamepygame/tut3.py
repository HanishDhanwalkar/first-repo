import pygame
x=pygame.init()
# print(x)
game_window= pygame.display.set_mode((500,500))
pygame.display.set_caption("MyFristGame")

exit_game=False
game_over=False

# game looop
while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            exit_game=True



pygame.quit()
quit()