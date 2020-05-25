# -*- coding: utf-8 -*-
# @Time    : 2020-05-23
# @Author  : 爱吃苹果的鱼

import random


class StringUtils:

    @staticmethod
    def name_get():
        fst = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'  # 姓
        name = '永祥荣玉明树近伯晓正福佩中泽润智礼振岐跃良啸志英林江山春秋夏冬国凤龙呈' \
               '风雷发强刚贵才亮阳宝唐杰海磊蕾风岩炎申珏超宇岳枫锋田光克文永祥荣玉明树近' \
               '伯晓正福佩中泽润智礼振岐跃良啸志英'  #名字
        if random.randint(0, 1) == 0:  # 随机生成2个字在名字/单个字在名字
            return random.choice(fst) + random.choice(name)
        else:
            return random.choice(fst) + random.choice(name) + random.choice(name)  # 拼接返回

    @staticmethod
    def phone_get():
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]  # 第二位数字
        third = {
            3: random.randint(0, 9),
            4: [5, 7, 9][random.randint(0, 2)],
            5: [i for i in range(10) if i != 4][random.randint(0, 8)],
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9),
        }[second]  # 第三位数字
        suffix = random.randint(9999999, 100000000)   # 最后八位数字
        return "1{}{}{}".format(second, third, suffix)   # 拼接返回
