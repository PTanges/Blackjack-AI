from games import *

# Student(s): Patton Tang
# Course: CPSC-481
# Due Date: 2024-04-19

'''
constructor: int array
valid moves/actions: int tuples
	{ index arrayval
	index arrayval-1 until == 1 }
funct result(state, move): {
	return new_state}
funct actions(state): {
	return actions array}
funct terminal test(state): {
	return True if state = end
	ie all of array = 0}
funct utility(state, player): {
	returns +1 for MAX win
	returns -1 for MIN win
	- loser det by who picked LAST / "Next turn" player wins
funct to_move(state): {
	returns player who's turn it is to move
	- default impl in abstr: Game is enough

Note:
Consider overriding Game.play_game() to print the current state & player

Requirements:
- Extend class(Game)
- Represent state by int array
- Action removes obj from ONE pile (of range [1, n])
'''

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""

    def __init__(self, board=[]):
        self.board = [int(x) for x in board]
        self.initial = [int(x) for x in board]

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        # pair (a, b) where a is the row and b iters from val-1 as ...[1, val]
        moves = []
        for row_index, row_value in enumerate(state):
            if row_value == 0: continue
            for iterator in range(0, row_value):
                moves.append((row_index, iterator+1))
            # end for
        #end for
        return moves

    def result(self, state, move):
        # Given a state and what action to take... return the resulting state!
        # state = [(a,b), (c,d)...], and move = (a, b)
        row_index, sticks_removed = move
        new_state = state.copy()
        new_state[row_index] = state[row_index] - sticks_removed
        return new_state

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        if self.terminal_test(state):
            # Todo: Will need to implement properly
            # Assume with counter: even = loss, odd = win
            if player == 0:
                return -1
            else:
                return 1
        return 0

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return self.isBoardEmpty(state)

    def display(self, state):
        board = state
        print("board: ", board)

    def to_move(self, state):
        # Todo: Implement a way to detect Player
        # May return string, etc, but must match in Utility afterwards
        return 0

    def isBoardEmpty(self, state):
        _val = True
        for x in state:
            if x <= 0:
                return False
        return _val

if __name__ == '__main__':
    nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    # nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    # print(nim.initial)  # must be [0, 5, 3, 1]
    # print(nim.actions(nim.initial))  # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    # print(nim.result(nim.initial, (1, 3)))

    utility = nim.play_game(alpha_beta_player, query_player)  # computer moves first
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")

'''
Issue: AB_Player returns the board state with EVERY
'''