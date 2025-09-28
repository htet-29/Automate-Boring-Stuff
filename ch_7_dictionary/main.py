import sys, copy, collections

STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
'a1': 'wR', 'b1': 'wN', 'c1': 'ww', 'd1': 'wQ', 'e1': 'wK', 'f1': 'ww',
'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}

BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""

WHITE_SQUARE = '||'
BLACK_SQUARE = '  '

def print_chessboard(board):
    squares = []
    is_white_square = True
    for y in '87654321':
        for x in 'abcdefgh':
            if x + y in board.keys():
                squares.append(board[x + y])
            else: 
                if is_white_square:
                    squares.append(WHITE_SQUARE)
                else:
                    squares.append(BLACK_SQUARE)
            is_white_square = not is_white_square
        is_white_square = not is_white_square
    
    print(BOARD_TEMPLATE.format(*squares))
    """
    Start syntax '*' pass the values in the list as individual argumens.
    """


def isValidChessBoard(board: dict) -> bool:
    valid_columns = 'abcdefgh'
    valid_rows = '12345678'

    for square in board.keys():
        if len(square) != 2:
            print(f"Validation Failed. Invalid square format (length must be 2) found: '{square}'")
            return False
        
        col = square[0]
        row = square[1]

        if col not in valid_columns or row not in valid_rows:
            print(f"Validation Failed. Invalid square key found. '{square}'. (e.g., 'a1').")
            return False

    print("Square Validation Successful: All keys are valid chess squares.")

    valid_player = ['w', 'b']
    for piece in board.values():
        if len(piece) != 2:
            print(f"Validation Failed. Invalid square format (length must be 2) found: '{piece}'")
            return False

        player = piece[0]

        if player not in valid_player:
            print(f"Validation Failed. Invalid player piece found {player}. Must be 'w' or 'b'.")
            return False

    print("Pieces Validation Successful. All pieces are valid.")


    # Get all piece value from dictionary
    pieces = board.values()

    pieces_count = collections.Counter(pieces)

    white_king_count = pieces_count["wK"]
    black_king_count = pieces_count["bK"]
    white_pawn_count = pieces_count["wP"]
    black_pawn_count = pieces_count["bP"]

    if white_king_count == 1 and black_king_count == 1 and white_pawn_count == 8 and black_pawn_count == 8:
        print("Pieces Count Validation Successful. All players have necessary pieces")
        return True
    else:
        print("Validation Failed. Some player lacks certain pieces.")
        return False


isValidChessBoard(STARTING_PIECES)


# print('Interactive Chessboard')
# print('by AI Sweigart al@inventwithpython.com')
# print()
# print('Pieces:')
# print('  w - White, b - Black')
# print('  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King')
# print('Commands:')
# print('  move e2 e4 - Moves the piece at e2 to e4.')
# print('  remove e2 - Removes the piece at e2.')
# print('  set e2 wP - Sets square e2 to a white pawn.')
# print('  reset - Reset pieces back to their starting squares.')
# print('  clear - Clear the entire board.')
# print('  fill wP - Fill entire board with white pawns.')
# print('  help - Show this help information.')
# print('  quit - Quits the program.')
#
# main_board = copy.copy(STARTING_PIECES)
# while True:
#     print_chessboard(main_board)
#     response = input('> ').split()
#     if response[0] == 'move':
#         main_board[response[2]] = main_board[response[1]]
#         del main_board[response[1]]
#     elif response[0] == 'remove':
#         del main_board[response[1]]
#     elif response[0] == 'set':
#         main_board[response[1]] = response[2]
#     elif response[0] == 'reset':
#         main_board = copy.copy(STARTING_PIECES)
#     elif response[0] == 'clear':
#         main_board = {}
#     elif response[0] == 'fill':
#         for y in '87654321':
#             for x in 'abcdefgh':
#                 main_board[x + y] = response[1]
#     elif response[0] == 'quit':
#         sys.exit()

