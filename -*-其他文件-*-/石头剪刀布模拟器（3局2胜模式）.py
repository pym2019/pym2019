import os
import random
import time

print("-----3局2胜模式-----")
num = 0
yin_num = 0
shu_num = 0
while num <= 3:
    if shu_num == 2 or yin_num == 2:
        break
    user = int(input('  1.石头\n  2.剪刀\n  3.布\n   请出拳:'))
    if user > 3 or user <= 0:
        print('不能出大于3或小于1的值!')
        time.sleep(2)
        os.system("clear")
    else:
        data = ['', '石头', '剪刀', '布']
        com = random.randint(1, 3)
        print("   您: -- {} -- \n   电脑: -- {} -- ".format(data[user], data[com]))
        if user == com:
            print('\n ~~~~~平局~~~~~ ')
            time.sleep(2)
            os.system("clear")
            continue
        elif (user == 1 and com == 2) or (user == 2 and com == 3) or (user == 3 and com == 1):
            print('\n -----你赢了!----- ')
            time.sleep(2)
            os.system("clear")
            yin_num += 1
        else:
            print('\n 你输了... ')
            time.sleep(2)
            os.system("clear")
            shu_num += 1
    num += 1
