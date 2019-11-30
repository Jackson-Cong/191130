# -*- coding: UTF-8 -*-

from pkg_KOG.equipment import Equipment
from class_attack import EQAttack
from class_defense import EQDefense
from class_mana import EQMana
from class_move import EQMove

eq1 = Equipment()
eq1.show_me()

eq2 = EQAttack()
eq2.show_me()
eq2.show_me_unique()

eq3 = EQDefense()
eq3.show_me()
eq3.show_me_unique()

eq4 = EQMana()
eq4.show_me()
eq4.show_me_unique()

eq5 = EQMove()
eq5.show_me()
eq5.show_me_unique()
