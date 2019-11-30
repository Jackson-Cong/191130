# -*- coding: UTF-8 -*-
import random

from equipment import Equipment
import global_VAR as GLV


class EQDefense(Equipment):

    restore_life_force = 0.0

    def __init__(self):
        '''按规则随机生成防御类道具'''
        self.name = self.__set_name()

        for i in range(GLV.MAX_FORGE_TIMES):
            n = random.randint(0, 10)
            self.__forge_eq(n)

        return


    def show_me_unique(self):
        print('-----独有加成-----')
        print('       +回血:%0.2f' % (self.restore_life_force))
        print('-----------------')
        return

    def __forge_eq(self, skill_num):

        if skill_num == 0:
            self.add_physical_attack += 0.05 *GLV.MAX_ATTACK
        elif skill_num == 1:
            pass
        elif skill_num == 2:
            self.add_mana_defense += 0.05 *GLV.MAX_DEFENSE
        elif skill_num == 3:
            pass
        elif skill_num == 4:
            self.add_move_speed += 0.05 *GLV.MAX_MOVE_SPEED
        elif skill_num == 5:
            self.add_life_force += 0.05 *GLV.MAX_LIFE_FORCE
        elif skill_num == 6:
            self.add_mana_power += 0.05 *GLV.MAX_MANA_POWER
        elif skill_num == 7:
            self.critical_strike = random.uniform(0.1, 0.5)
            if self.critical_strike >= 0.5:
                self.critical_strike = 0.5
        elif skill_num == 8:
            self.physical_suck = random.uniform(0.01, 0.1)
            if self.physical_suck >= 0.1:
                self.physical_suck = 0.1
        elif skill_num == 9:
            pass
        elif skill_num == 10:
            pass
        else:
            pass
        return


    def __set_name(self):

        all_eq_name = (
            '红玛瑙',
            '布甲',
            '抗魔披风',
            '提神水晶',
            '力量腰带',
            '熔炼之心',
            '神隐斗篷',
            '雪山圆盾',
            '守护者之铠',
            '反伤刺甲',
            '血魔之怒',
            '红莲斗篷',
            '霸者重装',
            '不祥征兆',
            '不死鸟之眼',
            '魔女斗篷',
            '极寒风暴',
            '冰痕之握',
            '护贤者的庇护',
            '暴烈之甲'
        )
        return random.choice(all_eq_name)

if __name__ == '__main__':
    eq = EQDefense()
    eq.show_me()
    eq.show_me_unique()
