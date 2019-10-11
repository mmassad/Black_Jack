from game import Game
from player import Player
from deck import Card
from deck import Deck
from console import Console
from dealer import Dealer
# This module checks some features for the split cases

def multiple_decks():
    # Testing multiple decks of 52 cards
    game_test = Game()
    game_test.start_game()
    print(len(game_test.deck.cards))
def split_with_aces():
    # Testing split function
    console = Console()
    deck = Deck()
    player_test = Player("Player 0", 10, [[Card("A", "Spades", False), Card("A", "Clubs", False)]])
    player_test.place_bet()
    player_test.points = [player_test.hand[0][0].check_value() + player_test.hand[0][1].check_value()]

    console.print_hand(player_test)

    player_test.turn(deck, 0)
    console.print_hand(player_test)
def winner_with_split_hand():
    # Testing winner function when player has multiple hands
    console = Console()
    dealer = Dealer("Table", [Card("A", "Spades", False), Card("3", "Spades", False), Card("4", "Spades", False)])
    dealer.points = 18

    player_test = Player("Player 0", 2, [[Card("J", "Spades", False), Card("7", "Spades", False)],
                                         [Card("10", "Spades", False), Card("4", "Spades", False), Card("9", "Spades", False)],
                                         [Card("A", "Spades", False), Card("Q", "Spades", False)],
                                         [Card("2", "Spades", False), Card("8", "Spades", False), Card("8", "Spades", False)]])
    player_test.bet = [2, 2, 2, 2]
    player_test.points = [17, 23, 21, 18]

    print(" Chips: \t" + str(player_test.chips) + "\t")
    dealer.check_winner(player_test)
    print(" Chips: \t" + str(player_test.chips) + "\t")
def four_splits():
    game = Game()
    game.console = Console()
    game.deck = Deck()
    game.deck.cards[2:14] = [Card("9", "Spades", False), Card("9", "Clubs", False), Card("9", "Hearts", False), Card("9", "Diamonds", False),
                             Card("9", "Spades", False), Card("2", "Clubs", False), Card("3", "Hearts", False), Card("4", "Diamonds", False),
                             Card("5", "Spades", False), Card("6", "Clubs", False), Card("7", "Hearts", False), Card("8", "Diamonds", False)]

    game.dealer = Dealer("Table", [])
    game.dealer.hit(game.deck)
    game.dealer.hit(game.deck)

    game.player = Player("Player 0", 10, [[]])
    game.player.hit(game.deck, 0)
    game.player.hit(game.deck, 0)

    game.console.print_table(game.dealer, game.player)
    game.player_turn(game.player, 0)
def split_bust():
    game = Game()
    game.console = Console()
    game.deck = Deck()
    game.deck.cards[2:14] = [Card("8", "Spades", False), Card("8", "Clubs", False),
                             Card("9", "Spades", False), Card("5", "Diamonds", False)]

    game.dealer = Dealer("Table", [])
    game.dealer.hit(game.deck)
    game.dealer.hit(game.deck)

    game.player = Player("Player 0", 10, [[]])
    game.player.hit(game.deck, 0)
    game.player.hit(game.deck, 0)

    game.console.print_table(game.dealer, game.player)
    game.player_turn(game.player, 0)

split_bust()
