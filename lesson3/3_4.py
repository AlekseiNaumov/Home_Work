# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


x = 1.1
y = -4

result = pow(x, y)


def my_func(number, degree):
    result_2 = number ** degree
    return result_2


def my_func2(number, degree):
    result_3 = 1
    for i in range(abs(degree)):
        result_3 = result_3 / number
    return result_3


result2 = my_func(x, y)
result3 = my_func2(x, y)

print(result)
print(result2)
print(result3)

