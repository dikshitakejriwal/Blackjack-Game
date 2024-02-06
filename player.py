import random
import importlib

class Player:

    def __init__(self, name, dealer):
        self.hand=[]
        self.win=0
        self.loss=0
        self.tie=0
        self.name=name
        self.dealer=dealer#request cards from

    def decide_hit(self):
        # DO NOT MODIFY
        return random.choice([True, True, False])

    def deal_to(self, card_value):
        """
        >>> player = Player(None, None)
        >>> player.deal_to(11)
        >>> player.hand
        [11]
        >>> player.deal_to(10)
        >>> player.hand
        [11, 10]
        """
        self.hand.append(card_value)
        
        
    @property
    def card_sum(self):
        """
        >>> player = Player(None, None)
        >>> player.deal_to(2)
        >>> player.card_sum
        2
        >>> player.deal_to(10)
        >>> player.card_sum
        12
        """
        total=0# is this inefficient?
        for i in self.hand:

            total+=i
        return total  

    def play_round(self):
        """
        >>> from dealer import Dealer
        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> player = Player(None, dealer)

        We see that after the first call the play_round, we have only hit once as dictated by decide_hit
        >>> player.play_round()
        >>> player.hand
        [10]

        After calling play_round again, decide_hit has decided to stand
        >>> player.play_round()
        >>> player.hand
        [10]

        After a third call to play_round, we've decided to hit, but busted!
        >>> player.play_round()
        >>> player.hand
        [10, 8, 10]

        After a final call to play_round, our hand shouldn't change since we've already busted
        >>> player.play_round()
        >>> player.hand
        [10, 8, 10]
        """
        x=self.decide_hit()
        while x==True and self.card_sum<21:
            self.dealer.signal_hit(self)
            x=self.decide_hit()

        return None

    def discard_hand(self):
        """
        >>> player = Player(None, None)
        >>> player.deal_to(11)
        >>> player.deal_to(5)
        >>> player.discard_hand()
        >>> player.hand
        []
        """
        self.hand=[]
        

    @property
    def wins(self):
        return self.win
        

    @property
    def ties(self):
        return self.tie

    @property
    def losses(self):
        return self.loss

    def record_win(self):
        """
        >>> player = Player(None, None)
        >>> player.record_win()
        >>> player.wins
        1
        """
        self.win+=1
        

    def record_loss(self):
        """
        >>> player = Player(None, None)
        >>> player.record_loss()
        >>> player.losses
        1
        """
        self.loss+=1
        

    def record_tie(self):
        """
        >>> player = Player(None, None)
        >>> player.record_tie()
        >>> player.ties
        1
        """
        self.tie+=1
        

    def reset_stats(self):
        """
        >>> player = Player(None, None)
        >>> player.record_tie()
        >>> player.record_loss()
        >>> player.record_win()
        >>> player.reset_stats()
        >>> player.ties
        0
        >>> player.wins
        0
        >>> player.losses
        0
        """
        (self.tie,self.win,self.loss)=(0,0,0)
        

    def __repr__(self):
        """
        Output should include the player name, their current hand, and their wins/ties/losses in that order
        >>> player = Player("Eric", None)
        >>> player.record_loss()
        >>> player.record_win()
        >>> player.record_win()
        >>> player
        Eric: [] 2/0/1
        """

        return "{}: {} {}/{}/{}".format(self.name,self.hand,self.win,self.tie,self.loss)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
