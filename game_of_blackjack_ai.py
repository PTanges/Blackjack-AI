import game_of_blackjack as game
import random

class Blackjack_Player:
    hand = []
    hand_value = 0
    moves = []
    action = ""
    def __init__(self):
        pass

    def choose_action(self):
        raise NotImplementedError

class Query_Player(Blackjack_Player):
    name = "Query"
    def __init__(self):
        # super.__init__(variable) only when passing to parent constructor
        pass

    def choose_action(self):
        pass
    # Prompt Player for Action


class Monte_Carlo_Player(Blackjack_Player):
    name = "Monte Carlo"
    def __init__(self):
        self.iterations = 100
        self.moves = ["Hit", "Stand"]

    def choose_action(self, deck, suit_names):
        if self.hand_value >= 21:
            self.moves.clear()
            return

        bustrate = 0
        for i in range(0, self.iterations):
            _picked_card = self.peek_random_card(deck, suit_names)
            _card_value = _picked_card.keys()
            _hand_value = self.peek_adjusted_hand_value(_card_value)

            if _hand_value > 21: bustrate += 1

        if bustrate < 50: self.action = "Hit"
        else:
            self.action = "Stand"
            self.remove_actions()

    def peek_random_card(self, deck, suit_names):
        picked_card = {}

        # Brute Force Method
        while True:
            _card_number = random.randint(2, 14)
            _suit_index = random.randint(0, 3)
            _suit = suit_names[_suit_index]
            if deck[_card_number][suit_names[_suit_index]] > 0:
                picked_card[_card_number] = _suit  # Key:Value, Card_Number:Suit_Name
                return picked_card

    def peek_adjusted_hand_value(self, card_value):
        _ICV = list(card_value)
        internal_card_value = _ICV[0]
        new_hand_value = 0
        _aces = 0
        if (internal_card_value > 10) and (internal_card_value < 14):
            new_hand_value += 10
        elif internal_card_value == 14:
            _aces += 1
        else:
            new_hand_value += internal_card_value

        for card in self.hand:
            _ICV = list(card.keys())
            _card_value = _ICV[0]
            if (_card_value > 10) and (_card_value < 14): # Face Cards
                new_hand_value += 10
            elif (_card_value == 14):
                _aces += 1
            else:
                new_hand_value += _card_value

        for i in range(0, _aces):
            if (new_hand_value+11) > 21:
                new_hand_value += 1
            else:
                new_hand_value += 11

        return new_hand_value

    def remove_actions(self):
        self.moves.clear()

class House_Player(Blackjack_Player):
    name = "House"
    minimum_hand_value = 17
    def __init__(self):
        pass

    def choose_action(self):
        pass