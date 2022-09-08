"""
this is a driver file. Handles user input and displaying the GameState object
"""

import pygame as p


import ChessEngine

WIDTH = HEIGHT = 512
DIMENTION=8
SQ_SIZE=HEIGHT//DIMENTION
MAX_FPS=15
IMAGES={}
'''
Initialize a global dictionary of images
'''
def loadImages():
    pieces=['wp','wR','wN','wB','wQ','wK','bp','bR','bN','bB','bQ','bK']
    for piece in pieces:
        IMAGES[piece]=p.transform.scale(p.image.load("images/"+piece+".png"),(SQ_SIZE,SQ_SIZE))

'''
main driver for user input and graphic update
'''

def main():
    p.init()
    screen=p.display.set_mode((WIDTH,HEIGHT))
    clock=p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    gs.__int__()
    loadImages()
    running=True
    while running:
        for e in p.event.get():
            if e.type==p.QUIT:
                running=False
        drawGameState(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()
'''
responcible for graphics
'''


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    colors=[p.Color("white"),p.Color("gray")]
    for i in range(DIMENTION):
        for j in range(DIMENTION):
            color=colors[((i+j)%2)]
            p.draw.rect(screen,color,p.Rect(j*SQ_SIZE,i*SQ_SIZE,SQ_SIZE,SQ_SIZE))




def drawPieces(screen,board):
    for i in range(DIMENTION):
        for j in range(DIMENTION):
            piece=board[i][j]
            if piece!="-": #not empty
                screen.blit(IMAGES[piece],p.Rect(j*SQ_SIZE,i*SQ_SIZE,SQ_SIZE,SQ_SIZE))

if __name__=="__main__":
    main()