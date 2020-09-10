# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('text_file_4_2.txt') as f:
    print(f.read())
    f.seek(0)
    content = f.readlines()
    print(f'Количество строк в файле: {len(content)}')
    i = 1
    for word in content:
        print(f'Количество слов в строке номер {i}: {len(word.split())}')
        i += 1

