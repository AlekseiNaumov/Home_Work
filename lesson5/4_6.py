# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('text_file_4_6.txt') as f:
    content = f.readlines()

hours_lesson = {}

for words in content:
    words = words.split()
    hours_lesson.setdefault(words[0])
    try:
        hours_lec = int(words[1].replace('(л)', ''))
    except ValueError:
        hours_lec = 0
    try:
        hours_pr = int(words[2].replace('(пр)', ''))
    except ValueError:
        hours_pr = 0
    try:
        hours_lab = int(words[3].replace('(лаб)', ''))
    except ValueError:
        hours_lab = 0
    hours_lesson[words[0]] = hours_lec + hours_pr + hours_lab

print(hours_lesson)
