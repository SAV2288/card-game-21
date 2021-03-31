from random import shuffle
from time import sleep


def print_separator():
    print('--------------------')


def player_game(deck_of_cards):
    """Ход игрока"""

    shuffle(deck_of_cards)  # Тасование колоды
    player_hand = []
    player_result = 0
    while True:
        print_separator()
        answer = input('Для того, чтобы вытянуть карту нажмите "Enter". Для передачи хода компьютеру "1".')
        if answer == '1':           # Передача хода компьютеру
            player_number_of_cards = len(player_hand)
            comp_result = comp_game(deck_of_cards, player_number_of_cards)
            result_game = {'player': player_result, 'comp': comp_result}
            break

        card = deck_of_cards.pop() 
        player_hand.append(card[0])
        player_result += card[1]
        print_separator()
        print(f'Ваша рука: {", ".join(player_hand)}. Всего {player_result} очков.')

        if player_result > 21:  # Обработка перебора у игрока
            result_game = {'player': player_result}
            break
    return result_game


def get_number_of_good_cards_and_total_cards(player_number_of_cards, required_balance, points):
    
    number_of_good_cards = 0
    total_cards = 0

    for key, value in points.items():
        total_cards += value
        if key <= required_balance:
            number_of_good_cards += value
    
    total_cards -= player_number_of_cards
    
    return [number_of_good_cards, total_cards]


def comp_pull_out_the_card(comp_hand, comp_result, player_number_of_cards, points):
    """Обработка возможности следующего хода компьютера на основе теории вероятности"""

    required_balance = 21 - comp_result
    data = [player_number_of_cards, required_balance, points]
    number_of_good_cards, total_cards = get_number_of_good_cards_and_total_cards(*data)

    probability_of_drawing_a_good_card = number_of_good_cards / total_cards
    return probability_of_drawing_a_good_card > 0.3


def comp_game(deck_of_cards, player_number_of_cards):
    """Ход компьютера"""

    points = {
        2:4,
        3:4,
        4:4,
        5:4,
        6:4,
        7:4,
        8:4,
        9:4,
        10:16,
        11:4
    }
    
    comp_hand = {}
    comp_result = 0
    while comp_result<=19 and comp_pull_out_the_card(comp_hand, comp_result, player_number_of_cards, points):
        card = deck_of_cards.pop()
        comp_hand[card[0]] = card[1]
        comp_result += card[1]
        points[card[1]] = points[card[1]] - 1
        sleep(1.5)
        print_separator()
        print(f'Рука компьютера: {", ".join(comp_hand.keys())}. Всего {comp_result} очков.')
    return comp_result


def get_result_game(game_score):

    result = {
        1: 'Поздравляем вы победили!',
        2: 'Победил компьютер!',
        3: 'Ничья',
        4: 'У вас перебор. Победил компьютер!',
        5: 'У компьютера перебор. Поздравляем вы победили!'
    }

    if game_score['player'] > 21:
        result_game = result[4]
    elif game_score['comp'] > 21:
        result_game = result[5]
    elif game_score['player'] > game_score['comp']:
        result_game = result[1]
    elif game_score['comp'] > game_score['player']:
        result_game = result[2]
    else:
        result_game = result[3]
    
    return result_game


def print_result(game_score, result_game):
    """Обработка и вывод результата игры"""

    print('')
    if result_game == 'У вас перебор. Победил компьютер!':
        print(f"++++++++++ Вы набрали {game_score['player']} очков. {result_game} ++++++++++")
    else:
        print(f"++++++++++ Счет {game_score['player']}: {game_score['comp']}. {result_game} ++++++++++")
    print('')


def game():
    """Карточная игра в 21"""

    deck_of_cards = [
        ('двойка червей',2), ('двойка крестей',2), ('двойка бубей',2), ('двойка виней',2),
        ('тройка червей',3), ('тройка крестей',3), ('тройка бубей',3), ('тройка виней',3),
        ('четверка червей',4), ('четверка крестей',4), ('четверка бубей',4), ('четверка виней',4),
        ('пятерка червей',5), ('пятерка крестей',5), ('пятерка бубей',5), ('пятерка виней',5),
        ('шестерка червей',6), ('шестерка крестей',6), ('шестерка бубей',6), ('шестерка виней',6),
        ('семерка червей',7), ('семерка крестей',7), ('семерка бубей',7), ('семерка виней',7),
        ('восьмерка червей',8), ('восьмерка крестей',8), ('восьмерка бубей',8), ('восьмерка виней',8),
        ('девятка червей',9), ('девятка крестей',9), ('девятка бубей',9), ('девятка виней',9),
        ('десятка червей',10), ('десятка крестей',10), ('десятка бубей',10), ('десятка виней',10),
        ('валет червей',10), ('валет крестей',10), ('валет бубей',10), ('валет виней',10),
        ('дама червей',10), ('дама крестей',10), ('дама бубей',10), ('дама виней',10),
        ('король червей',10), ('король крестей',10), ('король бубей',10), ('король виней',10),
        ('туз червей',11), ('туз крестей',11), ('туз бубей',11), ('туз виней',11),
    ]

    game_score = player_game(deck_of_cards)
    result_game = get_result_game(game_score)
    print_result(game_score, result_game)


game()