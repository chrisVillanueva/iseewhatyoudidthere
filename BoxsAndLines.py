import pygame # type: ignore
import random

pygame.init()

pygame.display.set_caption("Boxes and Lines")
screen = pygame.display.set_mode((1020,780))
screen.fill((50, 80, 50))
font = pygame.font.Font(None, 36)
TickSpeed = 50
clock = pygame.time.Clock()
clock.tick(TickSpeed)
run = True
GameStage = "menu"


pygame.display.update()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    
    if GameStage == "menu":
        
        pygame.draw.rect(screen, (70, 70, 70), [340, 250, 340, 100], 0, 10)
        pygame.draw.rect(screen, (70, 70, 70), [340, 400, 340, 100], 0, 10)
        pygame.draw.rect(screen, (70, 70, 70), [340, 550, 340, 100], 0, 10)


    pygame.display.update()
                
pygame.quit()