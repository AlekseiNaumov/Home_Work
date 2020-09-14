# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться
# только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный
# метод.
from itertools import cycle
from time import sleep


class TrafficLight:
    __colors = ['red', 'yellow', 'green']

    def running(self):
        colors = TrafficLight.__colors
        for color in cycle(colors):
            if color == 'red':
                print(color)
                sleep(7)
            if color == 'yellow':
                print(color)
                sleep(2)
            if color == 'green':
                print(color)
                sleep(5)
        # while True:
        #     print(colors[0])
        #     sleep(7)
        #     print(colors[1])
        #     sleep(2)
        #     print(colors[2])
        #     sleep(5)


color_l = TrafficLight()
color_l.running()
