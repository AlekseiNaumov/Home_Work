# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('user_text_file.txt', 'w', encoding='utf-8') as f:
    while True:
        user_line = input('Your string: ')
        f.write(user_line + '\n')
        if user_line == '':
            break
