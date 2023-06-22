import time
import os


def tb_time():
    print("\n  ----- 中国 China 北京时间 GMT+8 -----")
    print(time.strftime("     %Y-%m-%d   %H:%M:%S"))
    time.sleep(0.00001)
    os.system("clear")


while True:
    tb_time()
