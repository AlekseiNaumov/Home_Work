# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

print('Программа выводит сумму чисел n + nn + nnn.')
user_number = input('Введите любое число (n): ')

# user_number2 = user_number + user_number
user_number2 = int(user_number * 2)
user_number3 = int(user_number * 3)
user_number = int(user_number)  # нельзя преобразовывать в число раньше

# print(user_number, user_number2, user_number3)

numbers_sum = user_number + user_number2 + user_number3

print(numbers_sum)
