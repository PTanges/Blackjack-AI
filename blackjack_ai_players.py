from games import *
import random

# Monte Carlo & "House" (does not follow standard algorithm)

def monte_carlo_player(game, state):
    return monte_carlo_decision(game, state)

def monte_carlo_decision(game, state):
    # To Do:
    # Maximize closest to 21, but straddle with % of busting.
    # - Make decision IRRESPECTIVE of other player's hands
    return 0

def blackjack_house_player(game, state):
    return house_player_decision(game, state)

def house_player_decision(game, state):
    # To Do:
    # House is not required to beat other players
    # - House typically will stop when hand => 17
    # - Hit if (both players have not bust) and (player hand values are >= 17) and (house hand value < both player hands)
    return 0