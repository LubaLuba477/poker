import itertools
from treys import Card, Evaluator, Deck

def get_card_id(card_str):
    return Card.new(card_str)

def calculate_equity(hero, villain, board):
    # convert card strings to card IDs to treys handling
    hero_hand_ids = [get_card_id(card) for card in hero]
    villain_hand_ids = [get_card_id(card) for card in villain]
    board_ids = [get_card_id(card) for card in board]
    
    # initialize evaluator and deck
    evaluator = Evaluator()
    deck = Deck()
    
    # remove known cards from the deck
    all_known_cards = hero_hand_ids + villain_hand_ids + board_ids
    for card in all_known_cards:
        deck.cards.remove(card)
    
    # keep track of wins and looses
    win_count = {1: 0, 2: 0}
    tie_count = 0
    total_count = 0
    
    # simulate the outcomse for all possible remaining cards using Monte Carlo simulation
    remaining_cards = deck.cards
    for remaining in itertools.combinations(remaining_cards, 5 - len(board)):
        full_board = board_ids + list(remaining)
        p1_score = evaluator.evaluate(full_board, hero_hand_ids)
        p2_score = evaluator.evaluate(full_board, villain_hand_ids)
        
        if p1_score < p2_score:
            win_count[1] += 1
        elif p2_score < p1_score:
            win_count[2] += 1
        else:
            tie_count += 1
        
        total_count += 1
        if(total_count > 50000):
            break
    
    # calculate equity percentages
    p1_equity = (win_count[1] + tie_count / 2) / total_count
    p2_equity = (win_count[2] + tie_count / 2) / total_count
    
    return p1_equity, p2_equity

