import os
import sys
import vk_api
from vk_api import exceptions
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
    print(Fore.RED+"Made by None\ntg: @YourDeath_pls")

print(Fore.RED+"Made by None\ntg: @YourDeath_pls\n")
msg_file = open("./message.txt", "r", encoding="utf-8")
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
        groups_change()
    elif res == 1:
        sender()
    elif res == 0:
        for i in range(0,6):
            print(Fore.BLUE+"Скрипт автоматически закроется через", 5-i, "сек.", end="\r")
            sleep(1)
            
        sys.exit()


def groups_change():
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


def sender():
    time_start = int(input("введите стартовое время сна (в минутах): "))
    time_end = int(input("введите конечное время сна (в минутах): "))
    time_all = randint(time_start*60, time_end*60)
    file = open("./spamchats.txt", "r")
    soup = file.readlines()
    ids = []
    for i in soup:
        group_id = i.split(" ")[-1]
        ids.append(group_id)
    rounds = 0
    while True:
        print("                                                            ", end="\r")
        chats = 0
        rounds += 1
        print(Fore.GREEN+f"{str(datetime.now())[10:][:6]}. Круг {rounds}")
        for i in ids:
            chats += 1
            chatnum = str(i).replace("\n", "")
            try:
                vk.wall.post(owner_id=-int(i), message=msg)
                print(Fore.GREEN+f"     {chats}. Отправлено в группу #{chatnum}")
            except exceptions.ApiError as e:
                print(Fore.RED+f"     {chats}. Вы были заблокированны в группе #{chatnum}")
        for i in range(0, time_all+1):
            endtime = time_all-i
            mins = endtime//60
            secs = endtime%60
            print(Fore.CYAN+f"Следующий круг через {mins} мин. {secs} сек.", end="\r")
            sleep(1)

if __name__ == "__main__":
    choose()
