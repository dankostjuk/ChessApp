from chess.svg import board
from pygame.examples.stars import move_stars
from stockfish import Stockfish
import chess
#
# # Initialize Stockfish
# stockfish = Stockfish(path="/usr/games/stockfish")
#
# # Example of setting up a position using a list of moves
# moves = ["e2e4", "e7e5", "g1f3", "b8c6"]
# stockfish.set_position(moves)
#
# # Example of setting up a position using a FEN string
# fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
# stockfish.set_fen_position(fen)
#
# # Get the best move from the current position
# best_move = stockfish.get_best_move()
# print(f"Best move: {best_move}")
#
# # Get the full board evaluation
# evaluation = stockfish.get_evaluation()
# print(f"Evaluation: {evaluation}")

def get_best_move(fen):
    stockfish = Stockfish(path="/usr/games/stockfish")
    stockfish.set_fen_position(fen)
    return stockfish.get_best_move()


def generate_new_fen(fen, move):
    new_board = chess.Board(fen)
    chess_move = chess.Move.from_uci(move)
    new_board.push(chess_move)
    new_fen = new_board.fen()
    return new_fen

def legal_move_check(fen, move) -> bool:
    stockfish = Stockfish(path="/usr/games/stockfish")
    stockfish.set_fen_position(fen)
    return stockfish.is_move_correct(move)
