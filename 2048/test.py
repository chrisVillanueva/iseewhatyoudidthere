import pygame # type: ignore
import random

pygame.init()

pygame.display.set_caption("2048")
screen = pygame.display.set_mode((1010,700))
screen.fill((0,20,45))
font = pygame.font.Font(None, 36)
TickSpeed = 50
clock = pygame.time.Clock()
clock.tick(TickSpeed)
run = True
Spacing = 20
SquareSize = 150
GridSize = 4
GridColor = (220, 210, 120)
TileLoc = []


def CordLookUp(i):
    return i * (Spacing + SquareSize) - SquareSize

def Grid():
    size = GridSize + 1
    #draws the game play grid
    for x in range(size):
        for y in range(size):
            pygame.draw.rect(screen, (GridColor), [CordLookUp(x), CordLookUp(y), SquareSize, SquareSize], 0 ,10)
    #draws the sidebar
    pygame.draw.rect(screen, (180, 180, 150), [ CordLookUp(5), (Spacing/2), 300, 680], 0, 10)

def TileDraw (x, y, value):
    #sets up the color of the tile
    Color = {0: (204,192,179),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46)}
    TileLoc.append([x, y, value])
    try:
        pygame.draw.rect(screen, (Color[value]), [ CordLookUp(x) + 5, CordLookUp(y) + 5, SquareSize - 10, SquareSize - 10], 0 ,10)
    except:
        pygame.draw.rect(screen, ((0, 0, 0)), [ CordLookUp(x) + 5, CordLookUp(y) + 5, SquareSize - 10, SquareSize - 10], 0 ,10)
    
    text = font.render(str(value), True, (100, 0, 0))
    text_rect = text.get_rect(center=(CordLookUp(x) + SquareSize / 2, CordLookUp(y) + SquareSize / 2))
    screen.blit(text, text_rect)

def TileErase(x, y, value):
    x = int(x)
    y = int(y)
    value = int(value)
    TileLoc.remove([x, y, value])
    pygame.draw.rect(screen, (GridColor), [ CordLookUp(x) + 5, CordLookUp(y) + 5, SquareSize - 10, SquareSize - 10], 0, 10)

def TileSpawn():
    x = random.randint(1,4)
    y = random.randint(1,4)
    if any(coord[:2] == [x, y] for coord in TileLoc):
        TileSpawn()
    else:
        if random.randint(1,10) == 1:
            TileDraw(x, y, 4)
        else:
            TileDraw(x, y, 2)
            
def slide(direction):
    #need to shrink to one smaller function so you dont reuse code

    if direction == "up":
        Col1 = 0
        column1 = []
        Col2 = 0
        column2 = []
        Col3 = 0
        column3 = []
        Col4 = 0
        column4 = []
        for tile in TileLoc:
            if tile[0] == 1:
                column1.append(tile)
            elif tile[0] == 2:
                column2.append(tile)
            elif tile[0] == 3:
                column3.append(tile)
            elif tile[0] == 4:
                column4.append(tile)
            else:
                print("tile out of tile range")

        column1.sort(key=lambda x: x[1])
        for tiles in column1:
            TileErase(tiles[0], tiles[1], tiles[2])
            Col1 += 1
            TileDraw(1, Col1, tiles[2])

        column2.sort(key=lambda x: x[1])
        for tiles in column2:
            TileErase(tiles[0], tiles[1], tiles[2])
            Col2 += 1
            TileDraw(2, Col2, tiles[2])

        column3.sort(key=lambda x: x[1])
        for tiles in column3:
            TileErase(tiles[0], tiles[1], tiles[2])
            Col3 += 1
            TileDraw(3, Col3, tiles[2])
        
        column4.sort(key=lambda x: x[1])
        for tiles in column4:
            TileErase(tiles[0], tiles[1], tiles[2])
            Col4 += 1
            TileDraw(4, Col4, tiles[2])

    if direction == "down":
        Col1 = 5
        column1 = []
        Col2 = 5
        column2 = []
        Col3 = 5
        column3 = []
        Col4 = 5
        column4 = []
        for tile in TileLoc:
            if tile[0] == 1:
                column1.append(tile)
            elif tile[0] == 2:
                column2.append(tile)
            elif tile[0] == 3:
                column3.append(tile)
            elif tile[0] == 4:
                column4.append(tile)
            else:
                print("tile out of tile range")

        column1.sort(key=lambda x: x[1])
        column1.reverse()
        for tiles in column1:
            TileErase(tiles[0], tiles[1], tiles[2])
            Col1 -= 1
            TileDraw(1, Col1, tiles[2])

        column2.sort(key=lambda x: x[1])
        column2.reverse()
        for tiles in column2:
            TileErase(tiles[0], tiles[1], tiles[2])
            Col2 -= 1
            TileDraw(2, Col2, tiles[2])

        column3.sort(key=lambda x: x[1])
        column3.reverse()
        for tiles in column3:
            TileErase(tiles[0], tiles[1], tiles[2])
            Col3 -= 1
            TileDraw(3, Col3, tiles[2])
        
        column4.sort(key=lambda x: x[1])
        column4.reverse()
        for tiles in column4:
            TileErase(tiles[0], tiles[1], tiles[2])
            Col4 -= 1
            TileDraw(4, Col4, tiles[2])
    
    if direction == "left":
        Row1 = 0
        row1 = []
        Row2 = 0
        row2 = []
        Row3 = 0
        row3 = []
        Row4 = 0
        row4 = []
        for tile in TileLoc:
            if tile[1] == 1:
                row1.append(tile)
            elif tile[1] == 2:
                row2.append(tile)
            elif tile[1] == 3:
                row3.append(tile)
            elif tile[1] == 4:
                row4.append(tile)
            else:
                print("tile out of tile range")

        row1.sort(key=lambda x: x[0])
        for tiles in row1:
            TileErase(tiles[0], tiles[1], tiles[2])
            Row1 += 1
            TileDraw(Row1, 1, tiles[2])

        row2.sort(key=lambda x: x[0])
        for tiles in row2:
            TileErase(tiles[0], tiles[1], tiles[2])
            Row2 += 1
            TileDraw(Row2, 2, tiles[2])

        row3.sort(key=lambda x: x[0])
        for tiles in row3:
            TileErase(tiles[0], tiles[1], tiles[2])
            Row3 += 1
            TileDraw(Row3, 3, tiles[2])
        
        row4.sort(key=lambda x: x[0])
        for tiles in row4:
            TileErase(tiles[0], tiles[1], tiles[2])
            Row4 += 1
            TileDraw(Row4, 4, tiles[2])
        
    if direction == "right":
        Row1 = 5
        row1 = []
        Row2 = 5
        row2 = []
        Row3 = 5
        row3 = []
        Row4 = 5
        row4 = []
        for tile in TileLoc:
            if tile[1] == 1:
                row1.append(tile)
            elif tile[1] == 2:
                row2.append(tile)
            elif tile[1] == 3:
                row3.append(tile)
            elif tile[1] == 4:
                row4.append(tile)
            else:
                print("tile out of tile range")

        row1.sort(key=lambda x: x[0])
        row1.reverse()
        for tiles in row1:
            TileErase(tiles[0], tiles[1], tiles[2])
            Row1 -= 1
            TileDraw(Row1, 1, tiles[2])

        row2.sort(key=lambda x: x[0])
        row2.reverse()
        for tiles in row2:
            TileErase(tiles[0], tiles[1], tiles[2])
            Row2 -= 1
            TileDraw(Row2, 2, tiles[2])

        row3.sort(key=lambda x: x[0])
        row3.reverse()
        for tiles in row3:
            TileErase(tiles[0], tiles[1], tiles[2])
            Row3 -= 1
            TileDraw(Row3, 3, tiles[2])
        
        row4.sort(key=lambda x: x[0])
        row4.reverse()
        for tiles in row4:
            TileErase(tiles[0], tiles[1], tiles[2])
            Row4 -= 1
            TileDraw(Row4, 4, tiles[2])
#game Setup
Grid()
for i in range(2):
    TileSpawn()
        
while run:
    #GameEndDetection
    if len(TileLoc) == (GridSize*GridSize):
        run = False
    #controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                TileSpawn()
            if event.key == pygame.K_UP:
                slide("up")
            if event.key == pygame.K_DOWN:
                slide("down")
            if event.key == pygame.K_LEFT:
                slide("left")
            if event.key == pygame.K_RIGHT:
                slide("right")

    pygame.display.update()
    pygame.time.wait(TickSpeed)
#after game end
pygame.quit()