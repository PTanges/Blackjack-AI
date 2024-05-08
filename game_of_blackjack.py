import game_of_blackjack_ai as AI
import random

class Blackjack:
    suit_names = ["Spades", "Hearts", "Diamonds", "Clubs"]  # "_ of suit_name"
    def __init__(self, deck_size=1):
        self.deck = {}
        for i in range(2, 15):
            self.deck[i] = {}
            for suit in self.suit_names:
                self.deck[i][suit] = deck_size

    def play_game(self, *players):
        # Include a way to move the House player (if added) to the last index
        game_players = []
        for player in players:
            game_players.append(player)

        self.deal_starting_hands(game_players)
        for player in game_players:
            self.actions(player)
            while len(player.moves) > 0:
                player.choose_action(self.deck, self.suit_names)
                self.result(player)
                self.evaluate_hand_value(player)
                if player.hand_value >= 21:
                    break

        self.display(players)

    def change_player_turn(self):
        pass

    def actions(self, player):
        self.evaluate_hand_value(player)
        if player.hand_value >= 21:
            player.remove_actions()

    def result(self, player):
        if player.action == "Stand":
            player.remove_actions()
        elif player.action == "Hit":
            player.hand.append(self.draw_card())
        elif len(player.moves) == 0:
            return

    def display(self, players):
        for player in players:
            player_hand = []

            _internal_card_map = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
            for card in player.hand:
                cards = ""
                _ICN = list(card.keys())
                _internal_card_number = _ICN[0]
                _suit = card[_internal_card_number]

                if _internal_card_number > 10:
                    cards += _internal_card_map[_internal_card_number]
                else:
                    cards += str(_internal_card_number)
                cards = cards + " of " + _suit
                player_hand.append(cards)

            print(f'Player Name: {player.name}\n'
                  f'Hand: {player_hand}\n'
                  f'Hand Value: {player.hand_value}\n')

    def convert_internal_card_number_to_face_name(self, internal_card_number):
        _internal_card_map = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
        if internal_card_number > 10:
            return _internal_card_map[internal_card_number]
        return internal_card_number

    def deal_starting_hands(self, players):
        for player in players:
            player.hand.append(self.draw_card())
            player.hand.append(self.draw_card())

    def draw_card(self):
        # Deck[2-14][suits], with rand [0,3] for Suit and rand [0, len-1] for Card
        picked_card = {}

        # Brute Force Method
        while True:
            _card_number = random.randint(2, 14)
            _suit_index = random.randint(0, 3)
            _suit = self.suit_names[_suit_index]
            if self.deck[_card_number][self.suit_names[_suit_index]] > 0:
                self.deck[_card_number][self.suit_names[_suit_index]] -= 1

                picked_card[_card_number] = _suit  # Key:Value, Card_Number:Suit_Name
                return picked_card



        '''
        Las Vegas Method:
        Cards are stored in a nested dict of {internal_card_number(2-14) : {suit_name: deck_quantity}}
        
        keys() on Cards to obtain ICNs. Randomint(len(ICNs))
        Cards[ICN.key].keys() to obtain Suit_Names. Randomint(len(Suit_Names))
        - If Quantity == 1, remove entry instead of decrementing/set to None
        '''

    def evaluate_hand_value(self, player):
        new_hand_value = 0
        _aces = 0
        for card in player.hand:
            _card_value = list(card.keys())
            if (_card_value[0] > 10) and (_card_value[0] < 14): # Face Cards
                new_hand_value += 10
            elif (_card_value[0] == 14):
                _aces += 1
            else:
                new_hand_value += _card_value[0]

        for i in range(0, _aces):
            if (new_hand_value+11) > 21:
                new_hand_value += 1
            else:
                new_hand_value += 11

        player.hand_value = new_hand_value

if __name__ == "__main__":
    game = Blackjack(deck_size=1)
    Q_Player = AI.Query_Player()
    MC_Player1 = AI.Monte_Carlo_Player()
    MC_Player2 = AI.Monte_Carlo_Player()
    game.play_game(Q_Player, MC_Player1, MC_Player2)
    # game.play_game(AI.Query_Player, AI.Monte_Carlo_Player, AI.House_Player)