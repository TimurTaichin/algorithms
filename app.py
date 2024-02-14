
extentions = [".py", ".exe", ".txt"]

name_of_file = "Введите имя файла"
result = ''

for ext in extentions:
    if ext in name_of_file:
        result = ext
        break
if len(result) == 0:
    print('error')
else:
    print(ext)























