import pygame # type: ignore
import random
pygame.init()

pygame.display.set_caption("Platformer")
screen = pygame.display.set_mode((1020,780))
screen.fill((50, 80, 50))
font = pygame.font.Font(None, 50)
TickSpeed = 60
clock = pygame.time.Clock()
clock.tick(TickSpeed)
run = True

#defining Key inputs
KeyInp = [False, False, False,False]


#load images and sounds
UsbImg = pygame.image.load("Images/UsbPlayer.png")
PlayerImg = pygame.transform.scale(UsbImg, [UsbImg.get_width() * 0.1, UsbImg.get_height() * 0.1])

PlayerSpeed = 0.5



class Players(pygame.sprite.Sprite):
    def __init__(self, posX, PoxY):
        super().__init__()
        self.image = pygame.Surface([100, 100])
        self.rect = self.image.get_rect()
        self.rect.center = [posX, PoxY]
    
    

        
PlayerScreenCord = [100, 200]
Player = Players(100, 100)
Players_Group = pygame.sprite.Group()
Players_Group.add(Player)

while run:
    #draw items on the screen
    screen.fill((50, 80, 50))
    Players_Group.draw(screen)
    screen.blit(PlayerImg, PlayerScreenCord)

    #calc movement
    PlayerScreenCord[1] += (KeyInp[1] - KeyInp[0]) * PlayerSpeed
    PlayerScreenCord[0] += (KeyInp[3] - KeyInp[2]) * PlayerSpeed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_w:
                KeyInp[0] = True
            if event.key == pygame.K_s:
                KeyInp[1] = True
            if event.key == pygame.K_a:
                KeyInp[2] = True
            if event.key == pygame.K_d:
                KeyInp[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                KeyInp[0] = False
            if event.key == pygame.K_s:
                KeyInp[1] = False
            if event.key == pygame.K_a:
                KeyInp[2] = False
            if event.key == pygame.K_d:
                KeyInp[3] = False
    
    Players_Group.update()
    pygame.display.update()
                
pygame.quit()
