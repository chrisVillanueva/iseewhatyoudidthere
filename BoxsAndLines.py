import pygame # type: ignore
import random

pygame.init()

pygame.display.set_caption("Boxes and Lines")
screen = pygame.display.set_mode((1020,780))
screen.fill((50, 80, 50))
font = pygame.font.Font(None, 100)
TickSpeed = 50
clock = pygame.time.Clock()
clock.tick(TickSpeed)
run = True
GameState = "menu"

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    
    if GameState == "menu":
        pygame.draw.rect(screen, (130, 130, 130), [340, 250, 340, 100], 0, 10)
        pygame.draw.rect(screen, (130, 130, 130), [340, 400, 340, 100], 0, 10)
        pygame.draw.rect(screen, (130, 130, 130), [340, 550, 340, 100], 0, 10)
        screen.blit(font.render("Play", True, (0, 0, 0)), [340, 550], )

    elif GameState == "Testing":
        pass
    
    
    pygame.display.update()
                
pygame.quit()
