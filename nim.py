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
    def __init__(self):
        pass

    def new_funct(self):
        pass


if __name__ == '__main__':
    nim = GameOfNim()