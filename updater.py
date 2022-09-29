import os
import shutil

print("Начинаю обновление...")

files = os.listdir("./")
ignore = ['message.txt', 'spamchats.txt', 'api.dbm.bak', 'api.dbm.dat', 'api.dbm.dir', 'api.dbm']
saved = []

for file in files:
    if file not in ignore:
        try:
            os.remove("./"+file)
        except Exception:
            shutil.rmtree("./"+file)
    else:
        os.system(f"cp {file} ..")
        saved.append(file)

os.chdir("..")
os.rmdir("./spamvk_release")
os.system("git clone https://github.com/None-TM/spamvk_release")
for file in saved:
    shutil.move("$HOME/"+file, "./")
os.chdir("./spamvk_release")

print("Обновление завершено")