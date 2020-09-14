# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
        self.draw()

    def draw(self):
        print('Запус отрисовки. ', self.title)


class Pen(Stationery):
    def draw(self):
        print(self.title, 'пишет письмо.')


class Pencil(Stationery):
    def draw(self):
        print(self.title, 'рисует картину.')


class Handle(Stationery):
    def draw(self):
        print(self.title, 'подчеркивае предложение.')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
