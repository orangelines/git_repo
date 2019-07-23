import random
import sys

class Keg:
    def rand_keg(self):
        lst = [x for x in range(1, self.amount + 1)]
        random.shuffle(lst)
        for i, y in enumerate(lst):
            print('{:*^30}'.format('-'))
            print('Новый бочонок: {} (осталось {})'.format(y, self.amount - (i+1)))
            yield y

    def __init__(self, amount):
        self.amount = amount
        self.gen = self.rand_keg()


class Cards:
    def set_card(self):
        num = set()
        while len(num) < self.strs * 5:
            num.add(random.randint(1, 91))
        cards = list(num)
        random.shuffle(cards)
        
        while len(cards) % self.strs != 0: 
            cards.append('None')
        self.strs = int(len(cards) / self.strs)
        cards = [cards[i: i + self.strs] for i in range(0,len(cards),self.strs)]

        for i in range(len(cards)):
            cards[i].sort()
        self.card_user = cards[:3]
        self.card_comp = cards[3:]

    def __init__(self, amount_card):
        str1 = 3
        self.strs = str1 * amount_card
        self.set_card()

    def get_card(self, card_player):
        print('{:-^25}'.format(self.name))
        print('{0[0]:>2} {0[1]:<10} {0[2]:<5} {0[3]} {0[4]} '.format(card_player[0]))
        print('{0[0]:>4} {0[1]:<6} {0[2]:<4} {0[3]:<4} {0[4]} '.format(card_player[1]))
        print('{0[0]} {0[1]:<5} {0[2]:<5} {0[3]:<5} {0[4]} '.format(card_player[2]))
        print('{:-^25}'.format( '-'))

    def search(self, card_player, num_keg):
        for i, n in enumerate(card_player):
            if num_keg in n:
                card_player[i][n.index(num_keg)] = '-'
                self.score += 1
                if self.score == 15:
                    print('{} Победила!'.format(self.name))
                    sys.exit(1)
                return True
        return False


class Player(Cards):

    def __init__(self, name):
        self.name = name
        self.score = 0

def main():

    game = Cards(2)
    keg = Keg(90)
    player = Player('Ваша карточка')
    computer = Player('Карточка компьютера')

    while True:
        num_keg = next(keg.gen)
        player.get_card(game.card_user)
        computer.get_card(game.card_comp)
        
        input_user = input('Зачеркнуть цифру? (y/n)')
        if input_user == 'y':
            if player.search(game.card_user, num_keg):
                continue
            else:
                print('Game Over!')
                sys.exit(1)
        if input_user == 'n':
            if player.search(game.card_user, num_keg):
                print('Game Over!')
                sys.exit(1)
            elif computer.search(game.card_comp, num_keg):
                continue
        if input_user != 'n' and input_user != 'y':
                print('Game Over! Нужно было ввести y или n!')
                sys.exit(1)

if __name__ == '__main__':
    main()