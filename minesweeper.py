import pygame # type: ignore
import random

pygame.init()

GridSize = [10, 10]
BlockSize = 30
BlockSpacing = 10
NumOfBombs = 17
Blocks = []
Bombs = []
MarkedBombs = []

pygame.display.set_caption("MineSweeper")
screen = pygame.display.set_mode((1010,700))
screen.fill((0,20,45))
font = pygame.font.Font(None, BlockSize)
TickSpeed = 50
clock = pygame.time.Clock()
clock.tick(TickSpeed)
run  = True

def CordLookUp(x):
    return (x * (BlockSize + BlockSpacing) + 20)

def CordLookDown(ScreenCord):
    return (ScreenCord - 20) // (BlockSize + BlockSpacing)

def TextAdd(x, y, text):
    text = str(text)
    text_surface = font.render(text, True, (225, 225, 225))  # Change text color to black
    text_rect = text_surface.get_rect(center=(CordLookUp(x) + BlockSize / 2, CordLookUp(y) + BlockSize / 2))
    screen.blit(text_surface, text_rect)

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        self.image = pygame.Surface([BlockSize, BlockSize])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        x = CordLookUp(x)
        y = CordLookUp(y)
        if type == "Bomb":
            pygame.draw.rect(screen, (225, 100, 100), [x, y, BlockSize, BlockSize])
        elif type == "unknown":
            pygame.draw.rect(screen, (100, 100, 100), [x, y, BlockSize, BlockSize])
        elif type == "MarkedBomb":
            pygame.draw.rect(screen, (150, 70, 70), [x, y, BlockSize, BlockSize])
        else:
            pygame.draw.rect(screen, (133, 133, 133), [x, y, BlockSize, BlockSize])
            if type > 0:
                TextAdd(CordLookDown(x), CordLookDown(y), str(type))
            

GameBoad = pygame.draw.rect(screen, ((173, 173, 173)), [10, 10, 680, 680])

while NumOfBombs != len(Bombs):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    if [x, y] not in Bombs:
        Bombs.append([x, y])
        Block(x, y, "Bomb")
Bombs.sort()

for x in range(1, GridSize[0]+1):
    for y in range(1, GridSize[1]+1):
        if [x, y] not in Bombs:
            NearBombs = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if [x + i, y + j] in Bombs and [x, y] != [0, 0]:
                        NearBombs += 1
            Blocks.append([x, y, NearBombs])
        Block(x, y, "unknown")

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if event.button == 1: 
                for block in Blocks:
                    if (mouse_pos[0] >= CordLookUp(block[0]) and mouse_pos[0] <= CordLookUp(block[0]) + BlockSize and mouse_pos[1] >= CordLookUp(block[1]) and mouse_pos[1] <= CordLookUp(block[1]) + BlockSize):
                        print(f"Clicked on block at ({block[0]}, {block[1]})")
                        Block(block[0], block[1], block[2])
                for bomb in Bombs:
                    if (mouse_pos[0] >= CordLookUp(bomb[0]) and mouse_pos[0] <= CordLookUp(bomb[0]) + BlockSize and mouse_pos[1] >= CordLookUp(bomb[1]) and mouse_pos[1] <= CordLookUp(bomb[1]) + BlockSize):
                        print("You clicked on a bomb!")
                        run = False
            if event.button == 3:
                for block in Blocks:
                    if (mouse_pos[0] >= CordLookUp(block[0]) and mouse_pos[0] <= CordLookUp(block[0]) + BlockSize and mouse_pos[1] >= CordLookUp(block[1]) and mouse_pos[1] <= CordLookUp(block[1]) + BlockSize and block not in MarkedBombs):
                        if [block[0], block[1]] in MarkedBombs:
                            Block(block[0], block[1], "unknown")
                            MarkedBombs.remove([block[0], block[1]])
                        else:
                            Block(block[0], block[1], "MarkedBomb")
                            MarkedBombs.append([block[0], block[1]])
                for bomb in Bombs:
                    if (mouse_pos[0] >= CordLookUp(bomb[0]) and mouse_pos[0] <= CordLookUp(bomb[0]) + BlockSize and mouse_pos[1] >= CordLookUp(bomb[1]) and mouse_pos[1] <= CordLookUp(bomb[1]) + BlockSize) and bomb not in MarkedBombs:
                        Block(bomb[0], bomb[1], "MarkedBomb")
                        MarkedBombs.append([block[0], block[1]])
                
    
    pygame.display.update()

pygame.quit()
