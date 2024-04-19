from games import *
import random

# Student(s): Patton Tang
# Course: CPSC-481
# Due Date: 2024-04-19

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""
    def __init__(self, board=[7, 5, 3, 1]):
        # self.initial = GameState(to_move='X', utility=0, board={}, moves=moves)

        moves = []
        for row_index, row_value in enumerate(board):
            if row_value == 0: continue
            for iterator in range(0, row_value):
                moves.append((row_index, iterator+1))

        self.initial = GameState(to_move="Max", utility=0, board=board, moves=moves)

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves

    def result(self, state, move):
        # Return Gamestate + pre-calculate utility value based on action taken
        if move == None: return state
        if state.board == None: return state

        row_index, sticks_removed = move
        new_board = state.board.copy()

        valid_moves = []
        new_utility = 0
        if row_index > (len(state.board)-1):
            # Players may "cheat" by skipping their turn (invalid action)
            pass
        elif sticks_removed > state.board[row_index]:
            # Players entering a value MORE than the actual sticks will set = max of that row
            # (invalid action) -modified-> valid action
            new_board[row_index] = 0
        else:
            # Remove sticks
            new_board[row_index] = state.board[row_index] - sticks_removed

        # Calculate valid actions
        for row_index, row_value in enumerate(new_board):
            if row_value == 0: continue
            for iterator in range(0, row_value):
                valid_moves.append((row_index, iterator + 1))

        # Swap Players now that action has been taken
        if state.to_move == "Min":
            next_player = "Max"
        else:
            next_player = "Min"

        # Calculate Utility
        quantity_of_actions = len(valid_moves)
        if quantity_of_actions == 0 and next_player == "Max":
            new_utility = -1
        elif quantity_of_actions == 0 and next_player == "Min":
            new_utility = 1
        else:
            new_utility = 0

        return GameState(to_move=next_player, utility=new_utility, board=new_board, moves=valid_moves)


    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return state.utility

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return state.utility != 0 or len(state.moves) == 0

    def display(self, state):
        board = state.board
        print("board: ", board)

    def to_move(self, state):
        return state.to_move

if __name__ == '__main__':
    nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    # nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial)  # must be [0, 5, 3, 1]
    print(nim.actions(nim.initial))  # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1, 3)))
    print("\n")

    utility = nim.play_game(query_player, alpha_beta_player)  # computer moves first
    if (utility > 0):
        print("MIN won the game")
    else:
        print("MAX won the game")