import bj_module

def restart():
    rs = input('Would you like to play again?')
    if rs.lower() == 'y' or rs.lower() == 'n':
        return rs
    else:
        print(f'Invalid response. Please enter "Y" or "N".')
        return restart()

def checkHandTotal(player):
    if player.getHandValue() == 21:
        print(f'Blackjack! Congrats {player.name} you win!')
        rs = restart()
        if rs == 'y':
            return rs
        else:
            return "quit"
    elif player.getHandValue() > 21:
        print(f'Oooh sorry {player.name}. You bust.')
        rs = restart()
        if rs == 'y':
            return rs
        else:
            return "quit"

        

def StandorHit(deck,player):
    nextstep = input('Would you like to hit(take another card) or stand(stay with your hand)?')
    if nextstep.lower() == 'quit':
        return 'quit'
    elif nextstep.lower() == 'hit':
        player.draw(deck)
        print(f'Your Hand:')
        player.showHand()
        print(f'Hand Total = {player.getHandValue()}')
        if player.getHandValue() > 21:
            print(f'Oooh sorry {player.name}. You bust.')
            return 'game over'    
        return StandorHit(deck,player)
    elif nextstep.lower() == 'stand':
        return deck
    else:
        print(f'Invalid response. Please enter either stand or hit?')
        return StandorHit(deck,player)


def Blackjack():
    deck = bj_module.Deck_of_cards()
    deck.build()

    start = input('Welcome to BlackJack Deluxe! What is your name? ').title()
    start = bj_module.Player(start)
    dealer = bj_module.Dealer()
    deck.ShuffleDeck()
    print(f'Hello {start.name}! The dealer has shuffled the deck and we can now begin.'
    '(Enter "quit" at any time to exit the game)')
    while True:
        deal = input('Press enter to deal your hand')
        if deal.lower() == 'quit':
            return "quit"
        dealer.draw(deck)
        dealer.draw(deck)
        start.draw(deck)
        start.draw(deck)
        print(f'Your hand is:')
        start.showHand()
        print(f'Hand total = {start.getHandValue()}')
        print(f'Dealer shows:')
        dealer.showCard()
        chk = checkHandTotal(start)
        if chk == 'quit':
            return 'quit'
        elif chk == 'y':
            start.discardHand(deck)
            dealer.discardHand(deck)
            continue

        next = StandorHit(deck,start)
        if next == 'quit':
            return 'quit'
        elif next == 'game over':
            rs = restart()
            if rs == "y":
                start.discardHand(deck)
                dealer.discardHand(deck)
                continue
            else:
                break
        else:
            print(f'Your hand:')
            start.showHand()
            print(f'Hand Total = {start.getHandValue()}')
            print(f'Dealer Shows:')
            dealer.showHand()
            if dealer.getHandValue() == 21:
                print(f'Dealer Hand Total = {dealer.getHandValue()}')
                print(f'Dealer Blackjack. Sorry {start.name}, you lose!')
                rs = restart()
                if rs == "y":
                    start.discardHand(deck)
                    dealer.discardHand(deck)
                    continue
                else:
                    break


            while dealer.getHandValue()< 21:
                dealer.draw(deck)
                print(f'Dealer hits. Dealer hand is now:')
                dealer.showHand()
            if dealer.getHandValue() > 21:
                print(f'Dealer Hand Total = {dealer.getHandValue()}')
                print(f'Dealer Bust! Congrats {start.name}, you win!')
                 
            elif dealer.getHandValue() == 21:
                print(f'Dealer Hand Total = {dealer.getHandValue()}')
                print(f'Sorry {start.name}, you lose')
            
            elif dealer.getHandValue() == 21 and start.getHandValue() == 21:
                print(f'Dealer Hand Total = {dealer.getHandValue()}')
                print(f"It's a Tie!")
        
        rs = restart()
        if rs == "y":
            start.discardHand(deck)
            dealer.discardHand(deck)
            continue
        else:
            break
        
            


        
        
        

    

Blackjack()