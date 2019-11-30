# -*- coding: UTF-8 -*-

from equipment import Equipment


class EQMana(Equipment):

    add_mana_attack = 0.0

    def show_me_unique(self):
        print('-----独有加成-----')
        print('       +法术攻击:%0.2d' % (self.add_mana_attack))
        print('-----------------')
        return

if __name__ == '__main__':
    eq = EQMana()
    eq.show_me()
    eq.show_me_unique()
