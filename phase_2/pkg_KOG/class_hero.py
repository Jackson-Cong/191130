# -*- coding: UTF-8 -*-
import random

class Hero():
    '''
    skin = '英雄原始皮肤'
    name = '英雄姓名'
    position = '英雄定位'

    ab_viability = 0
    ab_damage = 0
    ab_effect = 0
    ab_difficulty = 0
    '''

    def __init__(self, s, n, p):
        '初始化英雄类'
        self.skin = s
        self.__name = n       # 不可更改
        self.__position = p   # 不可更改

        self.ab_viability = random.randint(1, 100)
        self.ab_damage = random.randint(1, 100)
        self.ab_effect = random.randint(1, 100)
        self.ab_difficulty = random.randint(1, 100)
        return

    @property
    def name(self):
        return self.__name
    @property
    def position(self):
        return self.__position

    def show_story(self):
        return

    def show_history(self):
        return
