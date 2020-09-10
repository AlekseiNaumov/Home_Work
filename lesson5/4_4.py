# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

with open('text_file_4_4.txt') as f:
    print(f.read())
    f.seek(0)
    content = f.readlines()

new_content = []
for number in content:
    number = number.split()
    number[0] = 'Один' if number[0] == 'One' else number[0]
    number[0] = 'Два' if number[0] == 'Two' else number[0]
    number[0] = 'Три' if number[0] == 'Three' else number[0]
    number[0] = 'Четыре' if number[0] == 'Four' else number[0]
    number = ' '.join(number) + '\n'
    new_content.append(number)

with open('new_text_file_4_4.txt', 'w+', encoding='utf-8') as new_f:
    new_f.writelines(new_content)
    new_f.seek(0)
    print(new_f.read())
