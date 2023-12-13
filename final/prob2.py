class Card :
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit) :
        self.rank = rank
        self.suit = suit

    def __str__(self) :
        reply = self.rank + self.suit
        return reply

class Hand :

    def __init__(self) :
        self.cards = []

    def __str__(self) :
        if self.cards :
            reply = ""
            for card in self.cards:
                reply += str(card) + " "
        else :
            reply = "<empty>"
        return reply
    
    def clear(self) :
        self.cards = []

    def add(self, card) :
        self.cards.append(card)

    def give(self, card, other_hand) :
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand) :
    def populate(self) :
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))

    def shuffle(self) :
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1) :
        for rounds in range(per_hand) :
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card,hand)
                else :
                    print("Out of cards!")

class Positionable_Card(Card) :
	def __str__(self) :
		if self.is_face_up :
			reply = super().__str__()
		else :
			reply = "XX"
		return rep

		def flip(self):
			self.is_face_up = not self.is_face_up	

if __name__ == "__main__" :
	deck1 = Deck()
	deck1.populate()
	deck1.shuffle()

	my_hand = Hand()
	your_hand = Hand()

	hands = [my_hand, your_hand]
	deck1.deal(hands, per_hand = 2)
	print("Welcome to the world simplest game!")
	num_of_player = int(input("How many players? (2-5): "))

	
