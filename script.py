import os
import sys
import vk_api
import dbm
from time import sleep
from datetime import datetime
from random import randint
from colorama import init, Fore, Back, Style

init(autoreset=True)
# 144098420
# 88266800
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print("Made by None\ntg: @YourDeath_pls")


msg_file = open("./message.txt", "r")
msg = msg_file.read()
msg_file.close()

def dbm_base():
    file = dbm.open('api.dbm', 'c')
    try:
        file['number']
    except:
        file['number'] = input("Введите номер: ")
        file['passwd'] = input("Введите пароль: ")
    file.close()
    return dbm.open('api.dbm', 'r')
file = dbm_base()
login = file['number'].decode()
passw = file['passwd'].decode()

vk_session = vk_api.VkApi(login, passw)
vk_session.auth()
vk = vk_session.get_api()


    
def choose():
    data = "0"
    res = int(input("Запустить спам - 1 \nДобавить чаты - 2 \nВыйти - 0\n\nВыбери интересующее и введи нужную цифру:  "))
    clear()
    if res == 2:
        f = open("./spamchats.txt", "r")
        soup = f.readlines()
        x = 1
        for i in soup:
            print(Fore.YELLOW+f"{x}. ", i.replace("\n", ""))
            x += 1
        f.close()
        data = 1
        f = open("./spamchats.txt", "a")
        while data != "0":
            data = input("Введи ссылку, для добавления в спам-лист:  ")
            if data == "0":
                clear()
                f.close()
                choose()
                
            else:
                name = data.split("/")[-1]
                group_id = (vk.utils.resolveScreenName(screen_name=name))['object_id']
                f.write(name+" "+str(group_id)+"\n")
                print(Fore.GREEN+"Группа ", name, "успешно добавленна, ее id: ", group_id)
    elif res == 1:
        time_start = int(input("введите стартовое время сна (в минутах): "))
        time_end = int(input("введите конечное время сна (в минутах): "))
        file = open("./spamchats.txt", "r")
        soup = file.readlines()
        ids = []
        for i in soup:
            group_id = i.split(" ")[-1]
            ids.append(group_id)
        rounds = 0
        while True:
            rounds += 1
            print(Fore.GREEN+f"{str(datetime.now())[10:][:6]}. Круг {rounds}")
            for i in ids:
                try:
                    vk.wall.post(owner_id=-int(i), message=msg)
                except Exception as e:
                    print(Fore.RED+f"     При отправке сообщения в группу #{i} возникла ошибка {e}")
            sleep(randint(time_start, time_end)*60)
    elif res == 0:
        for i in range(0,6):
            print(Fore.BLUE+"Скрипт автоматически закроется через", 5-i, "сек.", end="\r")
            sleep(1)
            
        sys.exit()

if __name__ == "__main__":
    choose()
