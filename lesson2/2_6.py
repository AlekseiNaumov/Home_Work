# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара
# и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
# goods = [(1, {'название': 'комп', 'цена': 5000, 'количество': 3, 'eд': 'шт'}),
#          (2, {'название': 'фотокамера', 'цена': 10000, 'количество': 1, 'eд': 'шт'}),
#          (3, {'название': 'жидкость для монитора', 'цена': 100, 'количество': 100, 'eд': 'мл'}),
#          (4, {'название': 'сканер', 'цена': 3000, 'количество': 10, 'eд': 'шт'})]

goods = []
character_goods = {'название': None, 'цена': None, 'количество': None, 'eд': None}
count_goods = 1

while True:
    print(f'Будут вводится данные товара под номером {count_goods}')
    character_goods2 = character_goods.copy()
    for key in character_goods2:
        character_goods2[key] = input(f'Введите данные в поле {key}: ')
        try:
            character_goods2[key] = int(character_goods2[key])
        except ValueError:
            character_goods2[key] = character_goods2[key]
    unit_goods = [count_goods, character_goods2]
    unit_goods = tuple(unit_goods)
    goods.append(unit_goods)
    count_goods += 1
    finish = input('Если хотите выйти наберите Q или нажмите любую клавишу,'
                   ' чтобы заполнить форму следующего товара.')
    if finish == 'Q':
        break

print(goods)

name = []
cost = []
numbers = []
dimension = []
analitic_doods = {}

for i in goods:
    for key, val in i[1].items():
        if key == 'название':
            name.append(val)
            analitic_doods[key] = name
        elif key == 'цена':
            cost.append(val)
            analitic_doods[key] = cost
        elif key == 'количество':
            numbers.append(val)
            analitic_doods[key] = numbers
        else:
            dimension.append(val)
            analitic_doods[key] = dimension

# print(name)
# print(cost)
# print(numbers)
# print(dimension)
print(analitic_doods)
