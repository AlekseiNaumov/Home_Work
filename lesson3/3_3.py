# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func(num1, num2, num3):
    min_num = min(num1, num2, num3)
    result = (num1 + num2 + num3) - min_num
    return result


print('Программа принимает три числа, и возвращает сумму двух максимальных.')

while True:
    try:
        user_number = int(input('Введите первое число:'))
        user_number2 = int(input('Введите второе число:'))
        user_number3 = int(input('Введите третье число:'))
        break
    except ValueError:
        print('Все три числа должны быть числами! Попробуйте еще!')

answer = my_func(user_number, user_number2, user_number3)
print(answer)
