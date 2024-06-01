import pygame # type: ignore
import random

pygame.init()

GridSize = [10, 10]
BlockSize = 25
BlockSpacing = 10
NumOfBombs = 17
Blocks = []
Bombs = []

pygame.display.set_caption("MineSweeper")
screen = pygame.display.set_mode((1010,700))
screen.fill((0,20,45))
font = pygame.font.Font(None, 36)
TickSpeed = 50
clock = pygame.time.Clock()
clock.tick(TickSpeed)
run  = True

def RandColor():
    return(random.randint(1,225), random.randint(1,225), random.randint(1,225))

def CordLookUp(x):
    return (x * (BlockSize + BlockSpacing) + 20)

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, type):
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        if type == "Bomb":
            pygame.draw.rect(screen, (225, 100, 100), [x, y, width, height])
        else:
            pygame.draw.rect(screen, (133, 133, 133), [x, y, width, height])
            text = font.render(str(type), True, (225, 225, 225))
            text_rect = text.get_rect(center=(CordLookUp(x) + BlockSize / 2, CordLookUp(y) + BlockSize / 2))
            screen.blit(text, text_rect)




GameBoad = pygame.draw.rect(screen, ((173, 173, 173)), [10, 10, 680, 680,])

while NumOfBombs != len(Bombs):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    if [x, y] not in Bombs:
        Bombs.append([x, y])
        Block(CordLookUp(x), CordLookUp(y), BlockSize, BlockSize, "Bomb")
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
            Block(CordLookUp(x), CordLookUp(y), BlockSize, BlockSize, NearBombs)

print(Bombs)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    
    
    pygame.display.update()
    pygame.sprite.Sprite.update(Block)

pygame.quit()
