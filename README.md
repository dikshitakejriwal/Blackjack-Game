# Blackjack Game

## Overview

- This Blackjack game is a simple yet comprehensive simulation of the popular casino game designed for the command line interface.
- It is built with Python and utilizes object-oriented programming principles.
- The game supports multiple players against a dealer, handling card shuffling, dealing, and basic game decisions such as hitting and standing.

## Components

The game is structured into four main Python files, each serving a specific purpose:

#### player.py - 

Defines the Player class, which includes methods for managing a player's hand, making decisions on whether to hit, and tracking the player's win/loss record.

#### dealer.py - 

Inherits from the Player class and adds functionalities specific to the dealer, such as shuffling the deck and dealing cards to players and themselves.

#### card_deck.py - 

Implements the CardDeck class, simulating a deck of cards with methods to shuffle and draw cards.

#### blackjack_game.py -

Contains the BlackjackGame class, which orchestrates the game by initializing players and the dealer, managing rounds of play, and determining the outcome of each game round.

## Testing

The game includes doctests for basic testing of functionality. To run these tests, execute the following command in the directory containing the game files:
```
python -m doctest -v blackjack_game.py
```
Replace blackjack_game.py with player.py, dealer.py, or card_deck.py to test other components.
