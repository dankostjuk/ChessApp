from math import trunc, floor

import pygame
# from pygame.examples.video import backgrounds

import board
import button
import chess
import stockfishFce as stockf
pygame.init()
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 900
STANDART_BUTTON_WIDTH = 200
STANDART_BUTTON_HEIGHT = 40
BUTTON_OFFSET = 30
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def move_to_uci_format(cords):
    from_y,from_x,to_y,to_x = cords[0][0],cords[0][1],cords[1][0],cords[1][1]
    from_x = chr(ord(str (7 - int(from_x))) + 49)
    to_x = chr(ord(str(7 - int(to_x))) + 49)
    return '' + from_x + str(from_y + 1) + to_x + str(to_y + 1)


def make_move(chess_board,game_position):
    best_move_button = button.Button((SCREEN_WIDTH - STANDART_BUTTON_WIDTH) * 0.85 ,
                                SCREEN_HEIGHT  // 3 ,
                                STANDART_BUTTON_WIDTH + 30,
                                STANDART_BUTTON_HEIGHT,
                                'NEXT BEST MOVE','#7171ff',0,0)

    waiting = True
    move_figure = []
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        move = chess_board.draw(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        chess_board.draw_figures(screen, game_position)
        pygame.display.flip()

        if move != ():
            if len(move_figure) == 0 :
                move_figure.append(move)
            elif move_figure[0] != move:
                move_figure.append(move)
            else:
                continue
                # move_figure = []

            if len(move_figure) == 2:
                uci_move = move_to_uci_format(move_figure)
                move = chess.Move.from_uci(uci_move)

                if game_position.is_legal(move):
                    game_position.push(move)
                    return True
                else:
                    return False

        if best_move_button.draw(screen)[0]:
            move = chess.Move.from_uci(stockf.get_best_move(game_position.fen()))
            game_position.push(move)
            # return True


        # waiting = False
def main():
    play_button = button.Button((SCREEN_WIDTH - STANDART_BUTTON_WIDTH) // 2 ,
                                SCREEN_HEIGHT  // 3 ,
                                STANDART_BUTTON_WIDTH,
                                STANDART_BUTTON_HEIGHT,
                                'Play','#7171ff',0,0)
    analyze_button = button.Button((SCREEN_WIDTH - STANDART_BUTTON_WIDTH) // 2 ,
                                SCREEN_HEIGHT // 3 + BUTTON_OFFSET * 2 ,
                                STANDART_BUTTON_WIDTH,
                                STANDART_BUTTON_HEIGHT,
                                'Game Review','#7171ff',0,0)
    chess_board_running = False
    # chess_board_running = True
    #
    chess_board = board.Board(100,'#777777','#FFFFFF')
    # # game_position = [['wRook', 'wKnight', 'wBishop',  'wKing','wQueen', 'wBishop', 'wKnight', 'wRook'],
    # #                  ['wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn'],
    # #                  ['blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank'],
    # #                  ['blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank'],
    # #                  ['blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank'],
    # #                  ['blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank'],
    # #                  ['bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn'],
    # #                  ['bRook', 'bKnight', 'bBishop', 'bKing', 'bQueen', 'bBishop', 'bKnight', 'bRook']
    # #                  ]
    # #
    #
    fen = chess.STARTING_FEN
    game_board = chess.Board(fen)
    running = True
    screen_color = 'lightgreen'
    efect_duration = 100
    background_efect = False
    color_change_timer = 0
    while running:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if background_efect and pygame.time.get_ticks() - color_change_timer >= efect_duration:
            background_efect = False
            screen_color = 'lightgreen'

        screen.fill(screen_color)
        if chess_board_running:
            if not make_move(chess_board,game_board):
                color_change_timer = pygame.time.get_ticks()
                background_efect = True
                screen_color = 'red'
        if not chess_board_running:
            if play_button.draw(screen)[0]:
                chess_board_running = True
            analyze_button.draw(screen)

        pygame.display.flip()

        clock.tick(100)

    pygame.quit()

if __name__ == "__main__":
    main()
# print(int('#FFFFFF'[1:],16) - )