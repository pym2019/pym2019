#   -*- coding:utf-8 -*-
#  作者:Phillip
#  微信:dd15386491595
#  QQ:1022125131

import os
import time

a = input("2023你是什么年份？（12生肖）(必须答对)")
if a == "兔" or a == "兔年":
    os.system("clear")
    b = input("月亮和我谁跟靓？")
    if b == "我":
        os.system("clear")
        c = input("你的妈妈叫什么？")
        if c == "妈妈":
            os.system("clear")
            d = input("你是不是出身在垃圾桶里的？")
            if d == "是":
                os.system("clear")
                print("OK,I know!I know!")
                time.sleep(2)
                print("So,one last question.")
                e = input("想不想退出？")
                if e == "想":
                    os.system('clear')
                    print("OK呀OK!")
                    time.sleep(1)
                    print('So?')
                    time.sleep(2)
                    f = input('我是不是你爸爸?')
                    if f == "是":
                        os.system('clear')
                        print('   Great!My son!Come on here!')
                        time.sleep(2)
                        print('Come on here and answering question!!!')
                        g = input("你是否听过鸡你太美？")
                        if g == "是":
                            os.system('clear')
                            h = input('歌曲原名叫什么？（要加书名号）')
                            if h == "《只因你太美》":
                                os.system('clear')
                                print('OK,Byb!')
                                time.sleep(3)
