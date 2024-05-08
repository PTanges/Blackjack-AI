from games import *
import blackjack_ai_players
import random

# Student(s): Patton Tang
# Course: CPSC-481
# Due Date: 2024-05

# use Stochastic Game
# May also need to implement a Monte_Carlo Player
# Random Player already exists but we can expand on that

'''
Query Player (Unchanged)
Implement Random Player as Monte Carlo Player in games.py
- return monte_carlo(state, game) #iteration_limit
Implement Stochastic(Game)
- chances(state)
- outcome(state, chance)
- probability(chance)
- play_game(*players)

Class Game
- actions(state)
- result(state, move)
- utility(state, player)
- terminal_test(state)
- to_move(state)
- display(state)
'''

'''
Game Rules:
House plays 2 Cards. Players each play 2 Cards.
- Player Actions (when total is < 21): Hit, Stand
- House Actions (when total is <17): Hit, Stand

Edge Case: Blackjack Hand > All Other Hands

AI:
- House MUST hit if under 17
- House goes AFTER the player, thus standing if their hand > player hand

Game Loop
- Player Turn
- AI Turn
- Evaluation

In case the above isn't complex enough... we can make a player who aims to win
- Bets are also not included
'''

class GameOfBlackjack(Game):
    suit_names = ["Spades", "Hearts", "Diamonds", "Clubs"] # "_ of suit_name"
    def __init__(self, deck_size = 1):
        '''
        Populate Deck
        - "Exceptions": {11: Jack, 12: Queen, 13: King, 14: Ace}
        '''
        moves = []
        # moves = ["Hit", "Stand"]

        deck = {}
        for i in range(2, 15):
            deck[i] = {}
            for suit in self.suit_names:
                deck[i][suit] = deck_size

        self.initial = GameState(to_move="Query", utility=0, board=deck, moves=moves)

        # Las Vegas Algorithm for Choosing a Card
        # May need to hold two arrays [] for valid card choices
        # card_values (a,b) of length n
        # available_suits (c, d) of length n
        # - after each valid pull, scan row in card_values to update, and adjust as necessary

        # House removes Hit if (hand < Player's_hand) & (21 <= hand value >= 17), this becomes OR with 2+ players
        # House removes Stand if (hand < 17)

        # house_initial_hand = (2 cards)
        # player_initial_hand = (2 cards)
        # - will need a better way, needs to scale with number of player(s)

        # self.initial = GameState(to_move="Max", utility=0, board=deck, moves=moves)
        # Refer to original class, usually board is reductive however here is incrementative
        # - we CAN make it reductive by starting at 21 and subtracting, ending at negative or = 0
        # Currently the game will run once per game start, thus meaning we populate deck with (-4) atm

        # Since the house seems to be incredibly simplistic (and pretty rigid rule wise), would be wise to implement a monte_carlo as player 2
        # - House AI is (nearly) entirely dictated by the rules
        # - may complexify by allowing it to decide how many player should lose, *maximizing* that

    def result(self, state, move):
        if move == None: return state
        if state.board == None: return state

        new_deck = state.board.copy()
        valid_moves = []
        new_utility = 0



    def actions(self, state):
        return state.moves

    def utility(self, state, player):
        return state.utility

    def terminal_test(self, state):
        return state.utility != 0 or len(state.moves) == 0

    def display(self, state):
        hand = state.hand
        print("Player Hand: ", hand)

    def to_move(self, state):
        return state.to_move

if __name__ == "__main__":
    game = GameOfBlackjack(deck_size=1)
    utility = game.play_game(query_player, blackjack_ai_players.monte_carlo_player, blackjack_ai_players.blackjack_house_player)

    print(utility)