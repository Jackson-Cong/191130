# -*- coding: UTF-8 -*-

from equipment import Equipment


class EQMove(Equipment):


    def show_me_unique(self):
        print('-----独有加成-----')
        print('                无')
        print('-----------------')
        return

if __name__ == '__main__':
    eq = EQMove()
    eq.show_me()
    eq.show_me_unique()
