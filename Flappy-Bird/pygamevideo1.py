import pygame

pygame.init()

surface = pygame.display.set_mode((800,400))

pygame.display.set_caption('Helicopter')

clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()















    
