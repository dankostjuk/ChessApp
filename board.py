import pygame as pg
import button
from stockfish import Stockfish

clock = pg.time.Clock()
chess_pieces_images = {
    'r': 'BlackRook.png',
    'R': 'WhiteRook.png',
    'n': 'BlackKnight.png',
    'N': 'WhiteKnight.png',
    'b': 'BlackBishop.png',
    'B': 'WhiteBishop.png',
    'q': 'BlackQueen.png',
    'Q': 'WhiteQueen.png',
    'k': 'BlackKing.png',
    'K': 'WhiteKing.png',
    'p': 'BlackPawn.png',
    'P': 'WhitePawn.png',
    '.': None
}

class Board:
    def __init__(self, size, dark_tile_color, light_tile_color):
        self.tile_size = size
        self.dark_tile_color = dark_tile_color
        self.light_tile_color = light_tile_color
        self.tile_cords = []

    def draw(self, surface, surface_width, surface_height):
        couter = 1
        activated_tile = ()
        for i in range(8):
            couter += 1
            for j in range(8):
                x = surface_width // 2 - (j - 4) * self.tile_size - self.tile_size
                y = surface_height // 2 - (i - 4) * self.tile_size - self.tile_size
                self.tile_cords.append((x+self.tile_size//2,y+self.tile_size//2))
                if couter % 2 == 1:
                    tile = button.Button(x,y,self.tile_size,self.tile_size,'',self.dark_tile_color,i,j)
                    if tile.draw(surface)[0]:
                        activated_tile = (i,j)
                else:
                    tile = button.Button(x, y, self.tile_size, self.tile_size, '', self.light_tile_color,i,j)
                    if tile.draw(surface)[0]:
                        activated_tile = (i, j)

                couter += 1
        return activated_tile

    def draw_figures(self, surface ,board):
        index = -1
        position = str(board).split('\n')
        position = [tile.split()[::-1] for tile in position]
        position = position[::-1]
        for row in position:
            for tile in row:
                index += 1
                if chess_pieces_images[tile] is not None:
                    chess_figure = pg.image.load('figures/' + chess_pieces_images[tile])
                    figure_rect = chess_figure.get_rect()
                    figure_rect.topleft = (self.tile_cords[index][0]-figure_rect.width//2
                                          ,self.tile_cords[index][1]-figure_rect.height//2)
                    surface.blit(chess_figure,figure_rect)
                else:
                    continue

