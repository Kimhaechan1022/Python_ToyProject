from playsound import playsound
from threading import Thread
import time

list1=('/root/song/Yerin.mp3')
list2=('/root/song/day2.mp3')
list3=('/root/song/grboy.mp3')
list4=('/root/song/jang.mp3')

def str1_thread(val):
    str1 = "< list 1 , Yerin >\n Artist : Yerin Baek\n Album : Every letter I sent you\n 2019.12.10 R&B\n"
    for i in range(len(str1)):
         print(str1[i], end='', flush = True)
         time.sleep(0.5)
t1 = Thread(target = str1_thread, args=(1,))


def str2_thread(val):
    str2 = "< list 2 , day6 >\n Artist : Day6\n Album : unknown\n unknown Rock"
    for i in range(len(str2)):
         print(str2[i], end='', flush = True)
         time.sleep(0.5)
t2 = Thread(target = str2_thread, args=(1,))


def str3_thread(val):
    str3 = "< list 3 , GiRi Boy >\n Artist : GiRiBoy\n Album : unknown\n Hip Hop"
    for i in range(len(str3)):
         print(str3[i], end='', flush = True)
         time.sleep(0.5)
t3 = Thread(target = str3_thread, args=(1,))


def str4_thread(val):
    str4 = "< list 4 , Jang beomjun >\n Artist : Jang beomjun\n song : youtube\n k pop"
    for i in range(len(str4)):
         print(str4[i], end='', flush = True)
         time.sleep(0.5)
t4 = Thread(target = str4_thread, args=(1,))




s = "\nplease wait..."
for i in range(len(s)):
        print(s[i], end='', flush = True)
        time.sleep(0.5)




print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("*********** welcome to simple musicplayer of terminal ***********")
time.sleep(1)
print("\n\n")
print("         which playlist do you want?")
print("\n\n            <playlist>\n")
print("         list 1 : Yerin")
print("         list 2 : day6")
print("         list 3 : GiRi Boy")
print("         list 4 : Jang beomjun\n\n")

num = int(input("       list number : ")) 
print(num)

if num==1:
    print("\n******** You chose list number 1 *********\n    ")
    t1.start()
    playsound(list1)
    t1.join()

elif num == 2:
    print("\n******** You chose list number 2 *********\n    ")
    t2.start()
    playsound(list2)
    t2.join()

elif num == 3:
    print("\n******** You chose list number 3 *********\n    ")
    t3.start()
    playsound(list3)
    t3.join()

elif num == 4:
    print("\n******** You chose list number 4 *********\n    ")
    t4.start()
    playsound(list4)
    t4.join()

