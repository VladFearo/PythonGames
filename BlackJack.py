import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def add_card(self, card):
        self.all_cards.append(card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cards = []
        self.total = 0
        for i in range(1):
            self.cards.append(deck.deal_one())
            self.total += self.cards[-1].value

    def bet(self, amount):
        if amount > self.money:
            print(f'Low funds only {self.money} left betting it all')
            amount = self.money
            self.money = 0
        else:
            self.money = self.money - amount
        return amount

    def win(self, amount):
        self.money += amount * 2

    def hit(self):
        self.cards.append(deck.deal_one())
        if self.cards[-1].rank == "Ace":
            if self.total + 11 > 21:
                self.total += 1
        else:
            self.total += self.cards[-1].value

    def is_bust(self):
        return self.total > 21

    def replay(self):
        for _ in self.cards:
            deck.add_card(self.cards.pop())
        self.total = 0
        for i in range(2):
            self.cards.append(deck.deal_one())
            self.total += self.cards[-1].value

    def __str__(self):
        return f'Player cards: {" ; ".join(f"{card}" for card in self.cards)} total: {self.total} total money: {self.money}'


class Dealer:
    def __init__(self):
        self.cards = []
        self.total = 0
        for i in range(1):
            self.cards.append(deck.deal_one())
            self.total += self.cards[-1].value

    def hit(self):
        self.cards.append(deck.deal_one())
        if self.cards[-1].rank == "Ace":
            if self.total + 11 > 21:
                self.total += 1
        else:
            self.total += self.cards[-1].value

    def is_bust(self):
        return self.total > 21

    def replay(self):
        for _ in self.cards:
            deck.add_card(self.cards.pop())
        self.total = 0
        for i in range(2):
            self.cards.append(deck.deal_one())
            self.total += self.cards[-1].value

    def start_game(self):
        print(f'Dealer card: {self.cards[0]}')

    def __str__(self):
        return f'Dealer cards: {" ; ".join(f"{card}" for card in self.cards)} total: {self.total}'

def replay():
    player.replay()
    dealer.replay()
    deck.shuffle()
#game

game = True
deck = Deck()
deck.shuffle()
dealer = Dealer()
player = Player(name="Player", money=1500)

round = 0
while game:
    if player.money == 0:
        print("Sorry you dont have anymore money to bet, game over!")
        game = False
        break
    round+=1
    print("Round: ", round)
    dealer.start_game()
    print("Player money: ", player.money)
    replay()

    while True:
        try:
            bet = int(input("Choose a bet amount!\n"))
            if bet < 0:
                raise TypeError
            break
        except ValueError:
            print("Invalid input, not a number try again!")
        except TypeError:
            print("No negative numbers allowed")
    bet = player.bet(bet)
    choice = -1
    print(player)
    playing = True
    dealing = True
    while playing:
        if player.is_bust():
            print("BUST!")
            playing = False
            dealing = False
            break
        if player.total == 21:
            print("Player wins!")
            playing = False
            dealing = False
            player.win(bet)
            break

        try:
            choice = int(input("Choose what to do: \n1. Hit\n2. Stay\n"))
            if choice not in [1, 2]:
                raise TypeError
        except ValueError:
            print("Invalid input, not a number try again!")
        except TypeError:
            print("Invalid input, wrong number entered!")

        if choice == 1:
            player.hit()
            print(player)
        elif choice == 2:
            playing = False
            break

    while dealing:
        print(dealer)
        if dealer.is_bust():
            print("Dealer bust! Player wins!")
            player.win(bet)
            dealing = False
            break
        if dealer.total > player.total:
            print("Player looses")
            dealing = False

            break
        else:
            dealer.hit()


