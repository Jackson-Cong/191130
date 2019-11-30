# -*- coding: UTF-8 -*-

from pkg_KOG.equipment import Equipment
from pkg_KOG.class_attack import EQAttack
from pkg_KOG.class_defense import EQDefense
from pkg_KOG.class_mana import EQMana
from pkg_KOG.class_move import EQMove

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
