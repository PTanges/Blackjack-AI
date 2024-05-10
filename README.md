<div align="center">

# Blackjack
Also known as 21.
</div>

## Overview:
A card game where each player aims to beat the dealer by getting as close to 21 as possible.


## Program Execution Instructions
Python needs to be installed. Run game_of_blackjack.py in console or through an IDE. The game will be executed and game data will be displayed through the console. Enter "Hit" to be dealt another card, or "Stand" to keep your current hand.

Additional players may be added by instantiating a player object and passing that object into the game.playgame function as a parameter. House should be the last player in the list. Query is a human player.

## File Breakdown
game_of_blackjack.py contains the main game loop and the game logic for distributing cards and evaluating hand value. Major functionality is broken down into each function with a central Blackjack class to store all the data such as the deck and how to create the deck.

game_of_blackjack_ai.py contains the AI for the additional players as well as the Query (Human) Player logic for i/o processes. These AI are not general purpose and must be tied to the game_of_blackjack.py file. House AI is extremely simplistic, being almost entirely determined by the game ruleset. All players (including Query) are derived from the Blackjack Player class which holds unimplemented methods for required function calls from the Blackjack class.

## Meta:
Course: **CPSC 481**. Project with Professor Kilambi

Language Chosen: **Python**
### Team Members:
```sh
Patton Tang (Computer Science Junior)
```

### Submission Specifications
Due: 05/19/2024 submitted via Canvas with all required files.

Groups of up to 3 students.
_The assignment must be coded in a high level language such as C++, Python, or Java._
