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
	- loser det by who picked LAST
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

    def __init__(self, board=[3,1]):
        raise NotImplementedError

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves

    def result(self, state, move):
        raise NotImplementedError

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        raise NotImplementedError

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        raise NotImplementedError

    def display(self, state):
        board = state.board
        print("board: ", board)

if __name__ == '__main__':
    nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    # nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board)  # must be [0, 5, 3, 1]
    print(nim.initial.moves)  # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2,
    1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1, 3)))
    utility = nim.play_game(alpha_beta_player, query_player)  # computer moves first
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")