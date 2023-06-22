import time
import os
import random
import string

count = 0
while count < 3:
    car_l = []
    for i in range(20):
        n1 = random.choice(string.ascii_uppercase)
        n2 = "".join(random.sample(string.ascii_uppercase + string.digits, 5))
        car_n2 = f"湘{n1}-{n2}"
        car_l.append(car_n2)
        print(car_n2)

    print("输入你喜欢的牌号:")
    choice = input("").strip()
    if choice in car_l:
        os.system("clear")
        print(f"\n恭喜获得新车牌: {choice}")
        print("祝你好运!")
        time.sleep(5)
        exit()
    else:
        print(f"----- {choice} 不合法!-----")
        time.sleep(3)
        os.system("clear")

    count += 1
