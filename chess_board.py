#!/usr/bin/env python3
"""Simple chessboard printer with initial piece setup.

Run: `python chess_board.py`
"""

WHITE = {'K':'♔','Q':'♕','R':'♖','B':'♗','N':'♘','P':'♙'}
BLACK = {'k':'♚','q':'♛','r':'♜','b':'♝','n':'♞','p':'♟'}
INITIAL_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"


def fen_to_board(fen):
    ranks = fen.split('/')
    board = []
    for rank in ranks:
        row = []
        for ch in rank:
            if ch.isdigit():
                row.extend(['.'] * int(ch))
            else:
                if ch.isupper():
                    row.append(WHITE.get(ch, ch))
                else:
                    row.append(BLACK.get(ch, ch))
        board.append(row)
    return board


def print_board(board):
    files = '  a b c d e f g h'
    print(files)
    for i, row in enumerate(board):
        rank = 8 - i
        print(f"{rank} " + ' '.join(row) + f" {rank}")
    print(files)


def main():
    board = fen_to_board(INITIAL_FEN)
    print_board(board)


if __name__ == '__main__':
    main()
