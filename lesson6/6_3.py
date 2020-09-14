# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f'Worker full name: {self.surname} {self.name}')

    def get_total_income(self):
        result = self._income["wage"] + self._income["bonus"]
        print('Full income = ', result)


worker1 = Position('Sergei', 'Syroezhkin', 'CEO', {"wage": 105, "bonus": 40})
print(worker1.name)
print(worker1.surname)
print(worker1.position)
print(worker1._income)
worker1.get_full_name()
worker1.get_total_income()

worker2 = Position('Vasilii', 'Pupkin', 'Bookkeeper', {"wage": 55, "bonus": 35})
print(worker2.name)
print(worker2.surname)
print(worker2.position)
print(worker2._income)
worker2.get_full_name()
worker2.get_total_income()
