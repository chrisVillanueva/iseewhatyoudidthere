import pygame # type: ignore
import random

pygame.init()

pygame.display.set_caption("")
screen = pygame.display.set_mode((1020,780))
screen.fill((0,0,0))
font = pygame.font.Font(None, 36)
TickSpeed = 50
clock = pygame.time.Clock()
clock.tick(TickSpeed)
run = True

pygame.draw.rect(screen, (100, 100, 100), [10, 10, 100, 100])

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                
pygame.quit()