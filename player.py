from time import sleep

# This module creates players for the BlackJack game.
# The class contains a name, available chips for betting and a hand with cards. Since the game allows card splitting,
# the player's hand may contain multiple lists of cards (up to 4, according to BlackJack rules).
# Other attributes are the bet amount, hand points and the presence of aces, all three independent attributes for each player hand.
# The player must place a bet (as long as there are enough chips) and can pick the top card from the deck, double down
# on the initial hand or split initial cards with the same number.
# This class also check the player's hand for blackjacks (ace + 10, J, Q or K), sum the hand's points (aces become 1 if the
# player's hand is over 21) and check for busts (over 21 points).
class Player:
    def __init__(self, name, chips, hand):
        self.name = name
        self.chips = chips
        self.bet = [0]
        if type(hand) == list:
            self.hand = hand
        else:
            raise TypeError('Hand must be an array of cards')
        self.points = [0]
        self.ace = [0]
        #self.human = True

    def sum_points(self, index):
        self.points[index] += self.hand[index][-1].check_value()

        if self.points[index] > 21 and self.ace[index] == 1:
            self.points[index] -= 10
            self.ace[index] +=1

    def hit(self, deck, index):
        new_card = deck.pick_top()
        new_card.hidden = False

        if new_card.number == "A":
            self.ace[index] += 1
        self.hand[index].append(new_card)
        self.sum_points(index)


    def condition_to_split(self, index):
        last_card = self.hand[index][-1]
        for i in range(len(self.hand[index])-1):
            return last_card.number == self.hand[index][i].number and self.chips >= self.bet[index] and len(self.hand) < 4


    def split(self, deck, index):
        self.chips -= self.bet[index]
        self.bet.append(self.bet[index])
        self.points.append(self.hand[index][-1].check_value())
        self.points[index] -= self.hand[index][-1].check_value()

        self.hand.append([self.hand[index][-1]])
        self.hand[index].pop(-1)

        if self.hand[index][0].number == "A":
            self.hit(deck, index)
            self.hit(deck, index+1)
            return False

        else:
            return True

    def condition_to_double_down(self, index):
        return self.chips >= self.bet[index] and len(self.hand[index]) < 3

    def double_down(self, index):
        self.chips -= self.bet[index]
        self.bet[index] += self.bet[index]

    def check_bust(self, index):
        if self.points[index] > 21:
            print(self.name + " went over 21 and lost " + str(self.bet[index]) + " chip(s)")
            sleep(3)
            return True
        else:
            sleep(3)
            return False

    def check_blackjack(self):
        if len(self.hand) > 1:
            return False
        else:
            return (self.hand[0][0].number in ["10", "J", "Q", "K"] and self.hand[0][1].number == 'A') or \
                   (self.hand[0][1].number in ["10", "J", "Q", "K"] and self.hand[0][0].number == 'A')

    def place_bet(self):
        try:
            if self.chips < 1:
                print(self.name + ' does not have enough chips to play \n')
                return False
            else:
                bet = int(input(self.name + ', how much would you like to bet?'))

                if bet > self.chips:
                    print('Insufficient chips, change the bet value \n')
                    self.place_bet()

                elif bet < 1:
                    print('Please enter a valid amount \n')
                    self.place_bet()

                else:
                    self.chips -= bet
                    self.bet[0] = bet
                    return True


        except ValueError:
            print('Please enter a valid amount \n')
            self.place_bet()

    def player_actions(self, index):
        try:
            possible_actions = [1, 2]
            str1 = self.name + ", choose a number for an action"
            if len(self.hand) > 1:
                str1 += " on hand number " + str(index+1)
            str1a = ": 1 - Stand"
            str2 = "  2 - Hit"

            if len(self.hand[index]) < 3:
                if self.condition_to_double_down(index):
                    str3 = "  3 - Double down"
                    possible_actions.append(3)
                else:
                    str3 = ""

                if self.condition_to_split(index):
                    str4 = "  4 - Split"
                    possible_actions.append(4)
                else:
                    str4 = ""
            else:
                str3 = ""; str4= ""

            action = int(input(
                "\n".join([str1 + str1a, " " * len(str1) + str2, " " * len(str1) + str3, " " * len(str1) + str4 + "\n"])))

            if action not in possible_actions:
                self.player_actions(index)

            else:
                return action

        except ValueError:
            self.player_actions(index)

    def turn(self, deck, index):
        action = self.player_actions(index)

        plot_hand = False
        replay = False

        if action == 2:
            self.hit(deck, index)
            plot_hand = True
            replay = True

        if action == 3:
            self.double_down(index)
            self.hit(deck, index)
            plot_hand = True
            replay = False

        if action == 4:
            plot_hand = True
            replay = self.split(deck, index)

        return plot_hand, replay