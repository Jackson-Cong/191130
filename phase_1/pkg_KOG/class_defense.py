# -*- coding: UTF-8 -*-

from equipment import Equipment


class EQDefense(Equipment):

    restore_life_force = 0.0

    def show_me_unique(self):
        print('-----独有加成-----')
        print('       +回血:%0.2f' % (self.restore_life_force))
        print('-----------------')
        return

if __name__ == '__main__':
    eq = EQDefense()
    eq.show_me()
    eq.show_me_unique()
