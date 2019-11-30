# -*- coding: UTF-8 -*-
from pkg_KOG.equipment import Equipment

class EQAttack(Equipment):

    critical_strike = 0.0
    physical_suck = 0.0


    def show_me_unique(self):
        print('-----独有加成-----')
        print('       +暴击率:%0.2f' % (self.critical_strike))
        print('     +物理吸血:%0.2f' % (self.physical_suck))
        print('-----------------')
        return
