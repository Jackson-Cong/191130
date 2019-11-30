# -*- coding: UTF-8 -*-

from pkg_KOG.class_hero import Hero

cjsh = Hero('A', 'B', 'C')
# cjsh.show_me()
print(cjsh.name)
print(cjsh.position)
print(cjsh.ab_difficulty)


cjsh.ab_difficulty = 999
print(cjsh.ab_difficulty)
