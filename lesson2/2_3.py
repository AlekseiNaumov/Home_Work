# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

year = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень',
        10: 'Осень', 11: 'Осень', 12: 'Зима'}
seasons = ['Зима', 'Весна', 'Лето', 'Осень']

while True:
    try:
        user_number = int(input('Введите месяц от 1 до 12: '))
        if 0 < user_number < 13:
            break
        else:
            print('Число должно быть от 1 до 12')
    except ValueError:
        print('Это не число! Попробуйте еще раз!')

if 3 <= user_number <= 5:
    answer = seasons[1]
elif 6 <= user_number <= 8:
    answer = seasons[2]
elif 9 <= user_number <= 11:
    answer = seasons[3]
else:
    answer = seasons[0]

print(f'Введеный месяц: {user_number} отосится к времени году {answer}!')

print(f'Введеный месяц: {user_number} отосится к времени году {year.get(user_number)}!')
