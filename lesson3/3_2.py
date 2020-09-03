# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def data_user1(name, surname, birthday_year, city, email, number_phone):
    print(f'Имя: {name} Фамилия: {surname} Год рождения {birthday_year} Город проживания: {city} Почта: {email} '
          f'Номер телефона: {number_phone}')


data_user1(name='Alex', surname='Naumov', birthday_year=2020, city='Moscow', email='alex@mail.com', number_phone=892371)


def data_user2(**kwargs):
    print(kwargs)


data_user2(name='Alex', surname='Naumov', birthday_year=2020, city='Moscow', email='alex@mail.com', number_phone=892371)
