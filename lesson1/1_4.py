# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

print('Программа находит самую большую цифру в числе.')
user_number = input("Введите целое положительное число: ")
index_number = 1
max_number = int(user_number[0])

while index_number < len(user_number):
    if max_number >= int(user_number[index_number]):
        index_number += 1
    elif max_number < int(user_number[index_number]):
        max_number = int(user_number[index_number])
        index_number += 1

print(max_number)
