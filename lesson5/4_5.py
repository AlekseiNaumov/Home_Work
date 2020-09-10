# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

with open('text_file_4_5.txt', 'w', encoding='utf-8') as f:
    elem = [(str(randint(1, 10)) + ' ') for num in range(1, 11)]
    f.writelines(elem)

with open('text_file_4_5.txt') as new_f:
    number = new_f.read()
    numbers = [int(number) for number in number.split()]
    sum_el = sum(numbers)

print(sum_el)
