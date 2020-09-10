# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# {"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json

with open('text_file_4_7.txt') as f:
    content = f.readlines()

firm_list = []
firm_dict = {}
average_profdict = {}
average_profit = 0
count_firm = 0
for words in content:
    words = words.split()
    profit = int(words[2]) - int(words[3])
    if profit > 0:
        average_profit += profit
        count_firm += 1
    firm_dict[words[0]] = profit

average_profdict['average_profit'] = round(average_profit/count_firm, 2)
firm_list.append(firm_dict)
firm_list.append(average_profdict)
print(firm_list)

with open('firm_list.json', 'w', encoding='utf-8') as f:
    json.dump(firm_list, f)
