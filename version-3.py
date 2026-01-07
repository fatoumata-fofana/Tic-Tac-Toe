player_symbol = "X"
cpu_symbol = "O"

def create_board():
    return [[1,2,3],[4,5,6],[7,8,9]]
    
def display_board(board):
  for row in board: 
    print(row)

def get_player_choice(player_symbol):
  choice = input("Player " + player_symbol + ", enter a number (1-9): ")
  return int(choice)

board = create_board()
display_board(board)
choice = get_player_choice(player_symbol)
