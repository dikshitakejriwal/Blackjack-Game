from player import Player
from dealer import Dealer


class BlackjackGame:
    def __init__(self, player_names):
        self.dealer=Dealer()
        self.player_list=[]
        for playername in player_names: 
            self.player=Player(playername,self.dealer)
            self.player_list.append(self.player)

    def play_rounds(self, num_rounds=1):
        """
        >>> import random; random.seed(1)
        >>> game = BlackjackGame(["Lawrence","Melissa"])
        >>> print(game.play_rounds(2))
        Round 1
        Dealer: [10, 9] 0/0/0
        Lawrence: [10, 6, 3] 0/1/0
        Melissa: [8, 8] 0/0/1
        Round 2
        Dealer: [10, 10] 0/0/0
        Lawrence: [10, 3] 0/1/1
        Melissa: [9, 10] 0/0/2

        """

        natural_list=[]
        list1=[]
        for i in range(num_rounds):
            self.dealer.shuffle_deck()#dealer shuffles the deck

            for j in range(2):#each player and dealer receives the card
                for player in self.player_list:
                    self.dealer.signal_hit(player)

                self.dealer.signal_hit(self.dealer)
                


            for player in self.player_list:#everyone plays round
                if player.card_sum==21 and self.dealer.card_sum!=21:#natural blackjack for player
                    player.record_win()
                    natural_list.append(player)

        
                elif self.dealer.card_sum==21:#both player and dealer has a natural blackjack
                    if player.card_sum==21:
                        player.record_tie()
                    else:
                        player.record_loss()
                    natural_list.append(player) 


            for player in self.player_list:#everyone plays round
                if player not in natural_list:
                    player.play_round()
            self.dealer.play_round()

            for player in self.player_list:

                if player not in natural_list:

                    if self.dealer.card_sum>21:#dealer gone bust
                        if player.card_sum>21:#player gone bust
                            player.record_loss()
                            
                        elif player.card_sum<=21:#player not gone bust 
                            player.record_win()
                            
                    if self.dealer.card_sum<=21:
                        if player.card_sum>21:
                            player.record_loss()
                            
                        elif player.card_sum<=21 and self.dealer.card_sum<player.card_sum:
                            player.record_win()
                            
                        elif player.card_sum<=21 and self.dealer.card_sum==player.card_sum:
                            player.record_tie()
                            
                        elif player.card_sum<=21 and self.dealer.card_sum>player.card_sum:
                            player.record_loss()
                          

            list1.append('{}{}'.format('Round ',i+1))
            list1.append(str(self.dealer))
            for player in self.player_list:   
                list1.append(str(player))
                player.discard_hand()
            self.dealer.discard_hand()
            natural_list=[]
            result='\n'.join(list1)

        return result

    def reset_game(self):
        """
        >>> game = BlackjackGame(["Lawrence", "Melissa"])
        >>> _ = game.play_rounds()
        >>> game.reset_game()
        >>> game.player_list[0]
        Lawrence: [] 0/0/0
        >>> game.player_list[1]
        Melissa: [] 0/0/0
        """
        for self.player in self.player_list:
            self.player.discard_hand()
            self.player.reset_stats()
        


if __name__ == "__main__":
    import doctest
    doctest.testmod()
