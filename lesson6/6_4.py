# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.show_speed()

    def go(self):
        print(f'{self.name} поехала.')

    def stop(self):
        print(f'{self.name} остановилась.')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}.')

    def show_speed(self):
        print(f'Текущая скорость автомобиля = {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышена разрешенная скорость (60), скорость = {self.speed}')
        else:
            print(f'Текущая скорость автомобиля = {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышена разрешенная скорость (40), скорость = {self.speed}')
        else:
            print(f'Текущая скорость автомобиля = {self.speed}')


class PoliceCar(Car):
    pass


car1 = TownCar(70, 'Black', 'Town Car', False)
car1.go()
car1.stop()
car1.turn('налево')
print(car1.speed)
print(car1.color)
print(car1.name)
print('Является полецейской машиной - ', car1.is_police, "\n")

car2 = SportCar(270, 'Red', 'Sport Car', False)
car2.go()
car2.stop()
car2.turn('направо')
print(car2.speed)
print(car2.color)
print(car2.name)
print('Является полецейской машиной - ', car2.is_police, "\n")

car3 = WorkCar(50, 'White', 'Work Car', False)
car3.go()
car3.stop()
car3.turn('назад')
print(car3.speed)
print(car3.color)
print(car3.name)
print('Является полецейской машиной - ', car3.is_police, "\n")

car4 = PoliceCar(100, 'Blue', 'Police Car', True)
car4.go()
car4.stop()
car4.turn('в переулок')
print(car4.speed)
print(car4.color)
print(car4.name)
print('Является полецейской машиной - ', car4.is_police, "\n")
