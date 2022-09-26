import os
os.system("pip install vk_api")
os.system("pip install colorama")
f_list = os.listdir()
if not 'message.txt' in f_list:
    fil = open('./message.txt', "w+")
    fil.close()
if not 'spamchats.txt' in f_list:
    fil = open('./spamchats.txt', "w+")
    fil.close()
