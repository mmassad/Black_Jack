from deck import Deck
from player import Player
from dealer import Dealer
from console import Console
from time import sleep

# This module implement all elements of the BlackJack game. It initializes the deck, dealer and players and
# keep the turns running. The class also accounts for a replay with the same players, making sure everyone has enough
# chips to start again.
class Game:
    def __init__(self):
         self.restart = 0
         self.deck = []
         self.player = []
         self.dealer = []
         self.console = Console()

    def start_game(self):
        self.deck = Deck()
        self.deck.cards += Deck().cards
        self.deck.shuffle()

        self.dealer = Dealer("Table", [])
        self.dealer.hit(self.deck)
        self.dealer.hit(self.deck)
        self.dealer.hand[1].hidden = True

        print('Welcome to Black Jack. \nHouse rules: \n\
        Each player begins with 10 chips\n\
        House pays 2:1 and 3:1 to BlackJacks. \n')

        self.create_list_players()

    def create_list_players(self):
        try:
            n = int(input('Number of players, up to 5: '))

            if n not in range(1, 6, 1):
                print('Please enter a valid number of players \n')
                self.create_list_players()

            for i in range(n):
                self.player.append(Player("Player " + str(i + 1), 10, [[]]))
                self.player[i].hit(self.deck, 0)
                self.player[i].hit(self.deck, 0)

        except ValueError or TypeError:
            print('Please enter a valid number of players \n')
            self.create_list_players()

    def player_turn(self, player, index):
        bust = False
        [plot_cards, play_again] = player.turn(self.deck, index)

        if plot_cards:
            self.console.print_table(self.dealer, player)
            bust = player.check_bust(index)

        if play_again and not(bust):
            self.player_turn(player, index)

        if not play_again and len(player.hand) > 1 and index < len(player.hand)-1 \
           or play_again and bust:
            self.player_turn(player, index+1)


    def dealer_turn(self):
        self.console.clear_screen()
        self.console.print_dealer(self.dealer)
        sleep(1)
        if self.dealer.points > 21:
            print("Dealer went over 21, remaining players win their bets.")
        elif self.dealer.turn(self.deck):
            self.dealer_turn()
        else:
            self.console.print_table_info(self.dealer)



    def end_game(self):
        print("\nEnd game:")
        for i in range(len(self.player)):
            print(self.player[i].name + "\t"+" Chips: \t" + str(self.player[i].chips) + "\t")
            self.player[i].hand = [[]]
            self.player[i].points = [0]
            self.player[i].bet = [0]
            self.player[i].ace = [0]
        self.dealer.hand = []
        self.dealer.points = 0

    def do_over(self):
        try:
            flag = str(input("Would you like to play again? Y/N \n"))

            if flag.upper() == "Y":
                self.dealer.hit(self.deck)
                self.dealer.hit(self.deck)
                self.dealer.hand[1].hidden = True

                for i in range(len(self.player)):
                    self.player[i].hit(self.deck, 0)
                    self.player[i].hit(self.deck, 0)

                self.game_loop(1)

            elif flag.upper() == "N":
                print("Thank you for playing")

            else:
                print("Write Y or N")
                self.do_over()

        except TypeError:
            self.do_over()

    def remove_player(self):
        pop_index = []
        for i in range(len(self.player)):
            if not self.player[i].place_bet():
                pop_index.append(i)

        if pop_index != []:
            pop_index.reverse()

            for k in range(len(pop_index)):
                self.player.pop(pop_index[k])

    def game_loop(self, flag):
        if flag == 0:
            self.start_game()

        self.remove_player()

        for i in range(len(self.player)):
            self.console.print_table(self.dealer, self.player[i])
            self.player_turn(self.player[i], 0)

        self.dealer.hand[1].hidden = False
        self.dealer_turn()


        for i in range(len(self.player)):
            self.dealer.check_winner(self.player[i])

        self.end_game()

        if len(self.deck.cards) > 25:
            self.do_over()
        else:
            print("Thank you for playing")