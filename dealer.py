# This module is the dealer for the BlackJack game. The class has a name, a single hand and its points.
# The dealer must hit the deck until its points are equal or over 17. The ace's value is always 11.
# The class compares the dealer's and player's points to determine who's the winner or if there's a tie and distribute
# the bet accordingly. A blackjack hand is considered a win in case of a draw.

class Dealer:

    def __init__(self, name, hand):
        self.name = name
        if type(hand) == list:
            self.hand = hand
        else:
            raise TypeError('Hand must be an array of cards')
        self.points = 0

    house_rate = 2
    blackjack_rate = 3

    def sum_points(self):
        self.points += self.hand[-1].check_value()

    def hit(self, deck):
        new_card = deck.pick_top()
        new_card.hidden = False
        self.hand.append(new_card)
        self.sum_points()

    def turn(self, deck):
        if self.points < 17:
            self.hit(deck)
            return True
        else:
            return False

    def check_winner(self, player):
        for index in range(len(player.hand)):
            if self.player_loses(player, index):
                print(player.name + " lost " + str(player.bet[index]) + " chip(s)")

            elif self.player_wins(player, index):
                if player.check_blackjack():
                    multiplier = Dealer.blackjack_rate
                    str1 = "BLACKJACK! "
                else:
                    multiplier = Dealer.house_rate
                    str1 = ""
                player.chips += multiplier * player.bet[index]
                print(str1 + player.name + " won " + str(multiplier * player.bet[index]) + " chips")

            else:
                player.chips += player.bet[index]
                print(player.name + " tied with the table, get back " + str(player.bet[index]) + " chip(s)")

    def player_loses(self, player, index):
        bool =  (player.points[index] > 21) or \
                (21 >= self.points > player.points[index]) or \
                (self.points == player.points[index] and self.check_blackjack() and not player.check_blackjack())

        return bool

    def player_wins(self, player, index):
        bool =  (self.points > 21 and player.points[index] <= 21) or \
                (21 >= player.points[index] > self.points) or \
                (self.points == player.points[index] and not self.check_blackjack() and player.check_blackjack())

        return bool

    def check_blackjack(self):
        return (self.hand[0].number in ["10", "J", "Q", "K"] and self.hand[1].number == 'A') or \
               (self.hand[1].number in ["10", "J", "Q", "K"] and self.hand[0].number == 'A')

