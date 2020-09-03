# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division_two_numbers(user_number1, user_number2):
    try:
        division = user_number1 / user_number2
        return division
    except ZeroDivisionError:
        print('Деление на ноль!')  # Чтобы не было деление на ноль проверка производится в цикле запроса


while True:
    try:
        number1 = int(input('Введите делимое:'))
        number2 = int(input('Введите делитель:'))
        if number2 == 0:
            print('Делитель не может быть равен нулю! Попробуйте еще раз!')
            continue
        break
    except ValueError:
        print('Делимое и делитель должны быть числами! Попробуйте еще!')


result = round(division_two_numbers(number1, number2), 2)
print(f'Результат деления {number1} на {number2} равен {result}')
