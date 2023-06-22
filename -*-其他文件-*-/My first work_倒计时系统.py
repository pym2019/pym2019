import os
import time

stime = int(input("请输入你想倒计时的秒数:"))
while stime <= 0:
    os.system("clear")
    print("   不支持非整数!")
    stime = int(input("请输入你想倒计时的秒数:"))
    if stime > 0:
        os.system("clear")
        break

for ada in range(stime, 0, -1):
    print(f"  {ada}")
    time.sleep(1)
    os.system("clear")
print("-----OVER!-----")
time.sleep(1)
os.system("clear")
time.sleep(3)
