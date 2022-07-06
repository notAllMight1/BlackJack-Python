import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    def __init__(self):
        self.deck = [] #deck = empty
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp = ''#structure of this deck
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'the deck has: '+deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand():
    def __init__(self):
        self.cards = [] #no cards
        self.value = 0 #start with 0 value
        self.ace = 0 #value checking for aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        #track aces
        if card.rank == 'Ace':
            self.ace+=1

        

    def ace_adjust(self):
        #if roral value > 21 and i have an ace
        #then Change my Ace to 1 instead of 11
        
        while self.value>21 and self.ace>0:
            self.value-=10
            self.ace-=1


class Chips():

    def __init__(self,total=100):
        self.total = total #provided by the user
        self.bet = 0
    def win(self):
        self.total+=self.bet
    def lose(self):
        self.total-=self.bet

#Functions needed for the game
def take_bet(Chips):
    while True:
        try:
            Chips.bet = int(input("HOW MANY CHIPS WOULD YOU LIKE TO BET? "))
        except:
            print("PLEASE INPUT AN INTEGER VALUE. ")
        else:
            if Chips.bet>Chips.total:
                print("Sorry, You dont have sufficient chips.")
            else:
                break

def hit(Deck,Hand):

    single_card = Deck.deal()
    Hand.add_card(single_card)
    Hand.ace_adjust()

def Hit_Or_Stand(Deck,Hand):
    global playing
    while playing == True:
        a = input("Hit or Stand (h / s)")
        x = a[0].lower()
        if x=='h':
            hit(Deck,Hand)
        elif x=='s':
            playing=False
        else:
            break

#card display
def show_some(player,dealer):
#show one of dealer card
    print("\nDealers Hand: ")
    print("First card hidden! ")
    print(dealer.cards[1])
#show all of player cards
    print("\nPlayers hand: ")
    for card in player.cards:
        print(card)



def show_all(player,dealer):
#show all dealer cards
    print("\nDealer hand: ")
    for card in dealer.cards:
        print(card)
#show the value of dealer
    print("\nValue of dealer is: {}".format(dealer.value))
#show players all cards
    print("\nPlayers hand: ")
    for card in player.cards:
        print(card)
    print("\nValue of player is: {}".format(player.value))


#GAME SENARIOS
def player_busts(player,dealer,Chips):
    print("Bust Player")
    Chips.lose()

def player_wins(player,dealer,Chips):
    print("Win Player")
    Chips.win()

def dealer_bust(player,dealer,Chips):
    print("Bust Dealer")
    Chips.win()

def dealer_win(player,dealer,Chips):
    print("Win Dealer")
    Chips.lose()

def push(player,dealer):
    print('Dealer and PLayer tie! PUSH')


#game logic
#
#
while True:
    #print opening statement
    print("WELCOME TO BLACKJACK")


    #shuffle deac and deal 2 cards per player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())


    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #setup players chips
    player_chips = Chips()

    
    #prompt for bet
    take_bet(player_chips)


    #show 2nd card of dealer and keep 1st one hidden
    show_some(player_hand,dealer_hand)

    while playing == True:


        #prompt hit or stand
        Hit_Or_Stand(deck,player_hand)
        print(player_hand)

        #show some cards
        show_some(player_hand,dealer_hand)

        #if player exceeds 21
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)

            break

    #if playe hasnt busted player dealer unter dealers value player
    if player_hand.value<=21:
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)

        #show all cards
        show_all(player_hand,dealer_hand)

        #winning senarios
        if dealer_hand.value>21:
            dealer_bust(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_win(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    
    #inform the chips
    print("\n total chips are {}".format(player_chips.total))

    #ask to play again
    new_game = input("Would yo like to play? (y/n)")

    if new_game[0].lower() == 'y':
        playing =True
        continue
    else:
        print("Thank you for playing!!")
        break
    