import os

print("Начинаю обновление...")

files = os.listdir("./")
ignore = ['message.txt', 'spamchats.txt', 'api.dbm.bak', 'api.dbm.dat', 'api.dbm.dir', 'api.dbm']
saved = []

for file in files:
    if file not in ignore:
        try:
            os.remove("./"+file)
        except Exception:
            files_in_dir = os.listdir("./"+file)
            for i in files_in_dir:
                os.remove("./"+file+"/"+i)
            os.rmdir("./"+file)
    else:
        os.system(f"cp {file} ..")
        saved.append(file)

os.system("cd")
os.rmdir("./spamvk_release")
os.system("git clone https://github.com/None-TM/spamvk_release")
for file in saved:
    os.system(f"cp {file} ./spamvk_release")
    os.remove("./"+file)
os.chdir("./spamvk_release")

print("Обновление завершено")