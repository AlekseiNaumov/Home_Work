# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_seconds = int(input('Введите количество секунд, которые нужно перевести в формат чч:мм:сс: '))

hours = user_seconds // 3600
seconds_after_hours = user_seconds - 3600 * hours
minutes = seconds_after_hours // 60
seconds = seconds_after_hours - 60 * minutes

# print(hours)
# print(seconds_after_hours)
# print(minutes)
# print(seconds)

print(f'Введенные секунды в формате чч:мм:сс: {hours}:{minutes}:{seconds}')
