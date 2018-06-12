import pygame,sys,random
from pygame.locals import *


BLUE=(0,0,255,1)
GREEN=(0,255,0,1)
RED=(255,0,0,1)
ORANGE=(255,126,0,1)
PURPLE=(126,0,126,1)
CIRCLE='circle'
OVAL='oval'
SQUARE='square'
LINES='lines'
DIAMOND='diamond'

COLORS=(GREEN,RED,ORANGE,PURPLE)
SHAPES=(CIRCLE,OVAL,SQUARE,LINES,DIAMOND)

def getRandomizedBoard():
    icons=[]
    for color in COLORS:
        for shape in SHAPES:
            icons.append((shape,color))
    random.shuffle(icons)
    iconsreq=int((10*5)/2)
    icons=icons[:iconsreq]*2
    random.shuffle(icons)

    board=[]
    for x in range(9):
        column=[]
        for y in range(4):
            column.append(icons[y])
            del icons[y]
        board.append(column)
    return board

def main():
    pygame.init()
    DisplaySurf = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("memorygame")
    DisplaySurf.fill(BLUE)
    mainboard=getRandomizedBoard()
    print(mainboard)
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__=='__main__':
    main()