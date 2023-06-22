#   -*- coding:utf-8 -*-
#  作者:Phillip
#  微信:dd15386491595

import random
import os


def die_nom():
    die_1 = random.randint(1, 6)
    print(f"    {die_1}")


while True:
    os.system("clear")
    die_nom()
    q = int(input('''\n   again?
           1.again     2.exit...'''))
    if q == 2:
        break
exit()
