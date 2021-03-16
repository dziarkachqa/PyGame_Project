import pygame

WINDOW_SIZE = (1200, 800)

screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill((50, 100, 220))
owl = pygame.image.load("owl.jpg")
screen.blit(owl, (0,0))
# pygame.draw.rect(screen, (100,100,100), pygame.Rect(270, 150, 60, 60))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
