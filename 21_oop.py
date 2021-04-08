import importlib
from random import shuffle


class Croupier:
    """Модель Крупье"""

    cards = importlib.import_module('cards').cards
    dict_cards_points = importlib.import_module('cards').points

    def shuffle_the_deck(self):
        """Перетасовать колоду"""

        shuffle(self.cards)

    def give_card(self):
        """Выдать карту"""

        return self.cards.pop()


сroupier = Croupier()


class Gamer:
    """Модель игрока"""

    cards_in_the_game = len(сroupier.cards)

    def __init__(self, name):
        self.point = 0                  # Количество очков в руке
        self.hand = []                  # Список карт в руке
        self.turn_completed = False     # Ход завершен
        self.name = name                # Имя игрока

    def check(self):
        """Проверка руки на перебор"""
        
        return self.point < 22

    def get_card(self):
        """Взять следующую карту"""

        if self.check():
            card, point = сroupier.give_card()
            self.hand.append(card)
            self.point += point
            Gamer.cards_in_the_game -= 1

            return (f'{self.name} вытащил карту: {card}', point)

        else:
            self.pass_the_move()
    
    def pass_the_move(self):
        """Присвоить метке завершения хода игрока значение 'True'"""

        self.turn_completed = True


class Computer(Gamer):
    """Модель игрока компьютер"""

    # Минимальная вероятность получить хорошую карту, при котором компьютер сделает ход
    minimum_probability_of_a_good_card = 0.3

    def the_likelihood_of_a_good_card(self):
        """Подсчет вероятности вытащить карту и при этом не перебрать"""

        # Получаем количество очков, позволяющих не перебрать
        max_point = 21 - self.point
        # Подсчет количества карт, номиналом не более max_point
        count_number_of_good_cards = 0

        for nominal_value in сroupier.dict_cards_points:
            if nominal_value <= max_point:
                count_number_of_good_cards += сroupier.dict_cards_points[nominal_value]
        return count_number_of_good_cards/Computer.cards_in_the_game \
             >= Computer.minimum_probability_of_a_good_card
        

    def possibility_of_action(check_funck):
        """Определение возможности сделать действие. 
        Принимает проверяющую функцию"""

        def decorator(func):
            def wrapper(self):
                if check_funck(self):
                    func(self)

                else:
                    self.end = True
            return wrapper
        return decorator

    @possibility_of_action(the_likelihood_of_a_good_card)
    def get_card(self):
        card, point = Gamer.get_card(self)
        сroupier.dict_cards_points[int(point)] -= 1


gamer = Gamer(input('Введите имя: '))
comp = Computer('Гена')

def print_game_result():
    """Печать результата игры"""

    if not gamer.check():
        name = gamer.name
        game_result = 3
    elif not comp.check():
        name = comp.name
        game_result = 3
    elif gamer.point == comp.point:
        game_result = 2
    elif gamer.point - comp.point >0:
        name = gamer.name
        game_result = 1
    elif gamer.point - comp.point <0:
        name = comp.name
        game_result = 1

    result = {
        1: f'Победил {name}!',
        2: 'Ничья!',
        3: f'{name} Перебрал!',
    }

    print(f'Счет {comp.point}: {gamer.point}. {result[game_result]}')


def game():
    """Игра в 21 с компьютером"""
    сroupier.shuffle_the_deck()

    while True:
        if gamer.check() and comp.check():
            if not gamer.turn_completed:
                answer = input(
                    'Взять карту?( Нет(нажми "3"), Да(нажми любую другую кнопку) )'
                    )
                if answer == '3':
                    gamer.pass_the_move()
                else:
                    print(gamer.get_card()[0])
            elif not comp.turn_completed:
                comp.get_card()
            else:
                break
        else:
            break

    print_game_result()


if __name__ == '__main__':
    game()