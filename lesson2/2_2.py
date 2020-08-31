# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_list = []
new_list = []

while True:
    user_elem = input('Введите что хотите и сколько хотите, захотите выйте наберите Q: ')
    if user_elem == 'Q':
        break
    else:
        user_list.append(user_elem)

print("Ваш список: ", user_list)

if len(user_list) % 2 != 0:
    last_index = user_list.pop()

for i in range(0, len(user_list)):  # без использования range можно было перебрать по элементам
    # и взять индекс каждого элемента
    new_list.insert(i + 1, user_list[i]) if i % 2 == 0 else new_list.insert(i - 1, user_list[i])

try:
    new_list.append(last_index)
    print('New список: ', new_list)
except NameError:
    print('New список: ', new_list)


