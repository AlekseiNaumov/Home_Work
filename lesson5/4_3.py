# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('text_file_4_3.txt') as f:
    print(f.read())
    f.seek(0)
    content = f.readlines()

average = 0
count_name = 0
for salary in content:
    pay = float(salary.split()[1])
    average += pay
    name = salary.split()[0]
    count_name += 1
    if pay < 20000:
        print(f'{name} получает з.п. меньше 20 000')
print(f'Средняя з.п. всех сотрудников {average/count_name}')
