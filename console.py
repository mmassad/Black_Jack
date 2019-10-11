from deck import Card
# This module is responsible for printing the cards of the game in a standardized way.
# The player functions account for multiple hands on the same player (split cases).

class Console:
    def __init__(self):
        self.output = [None] * 7

    def str_hidden_card(self):

        hidden_string = '| ' + (Card.size_of_card - 2) * '#' + '|'

        self.output[0] += ' ' + ((Card.size_of_card - 1) * '_').center(Card.size_of_card - 1) + ' '
        self.output[1] += hidden_string
        self.output[2] += hidden_string
        self.output[3] += hidden_string
        self.output[4] += hidden_string
        self.output[5] += hidden_string
        self.output[6] += ' ' + ((Card.size_of_card - 1) * '_').center(Card.size_of_card - 1) + ' '


    def str_open_card(self, card):

        self.output[0] += ' '  + ((Card.size_of_card - 1) * '_').center(Card.size_of_card - 1) + ' '
        self.output[1] += '| ' + card.number.ljust((Card.size_of_card - 2)) + '|'
        self.output[2] += '| ' + (Card.size_of_card - 2) * ' ' + '|'
        self.output[3] += '| ' + (Card.suits_to_symbol[card.suit]).center(Card.size_of_card - 2) + '|'
        self.output[4] += '| ' + (Card.size_of_card - 2) * ' ' + '|'
        self.output[5] += '| ' + card.number.rjust(Card.size_of_card - 2) + '|'
        self.output[6] += ' '  + ((Card.size_of_card - 1) * '_').center(Card.size_of_card - 1) + ' '


    def concatenate_cards(self, cards):

        for i in range(len(cards)):
            if cards[i].hidden:
                self.str_hidden_card()

            else:
                self.str_open_card(cards[i])


        print("\n".join(self.output))


    def print_hand(self, player):
        for k in range(len(player.hand)):
            empty_string = Card.size_of_card * ' '
            if len(player.hand) > 1:
                self.output = [empty_string, empty_string, empty_string, player.name.center(Card.size_of_card),
                               ("Hand " + str(k+1)).center(len(empty_string)), empty_string, empty_string]
            else:
                self.output = [empty_string, empty_string, empty_string, player.name.center(Card.size_of_card), empty_string, empty_string, empty_string]
            self.concatenate_cards(player.hand[k])
            self.print_player_info(player, k)

    def print_dealer(self, dealer):
        empty_string = Card.size_of_card * ' '
        self.output = [empty_string, empty_string, empty_string, dealer.name.center(Card.size_of_card), empty_string, empty_string, empty_string]
        self.concatenate_cards(dealer.hand)


    def print_player_info(self, player, index):
        print(player.name + "\t"+" Chips: \t" + str(player.chips) + "\t" + "Bet: \t" + str(player.bet[index]) + "\t" + "Points: \t" + str(player.points[index]))

    def print_table_info (self, dealer):
        print(dealer.name + "\t" + "Points: \t" + str(dealer.points))

    def clear_screen(self):
        print(30*"\n")

    def print_table(self, dealer, player):
        self.clear_screen()
        self.print_dealer(dealer)
        self.print_hand(player)


