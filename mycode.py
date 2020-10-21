print("Задание №1")
#Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. (Для ожидания нескольких секунд можно использовать метод стандартной библиотеки time.sleep())

from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зелёный']
    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n'
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(2)
            i += 1
TrafficLight = TrafficLight()
TrafficLight.running()

print("Задание №2")
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
    def massa(self):
        return self._length * self._width
class MassaCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume
r = MassaCount(64, 25786, 57)
print(r.massa())

print("Задание №3")
# на вебинаре разобрали, условие не буду копировать))
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus,
        }

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(self, name, surname, position, wage, bonus)
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

a = Position('Ivan', 'Petrov', 'programmer', 10000, 5000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

print("Задание №4")
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} is gone'
    def stop(self):
        return f'{self.name} is stopped'
    def turn_right(self):
        return f'{self.name} is turned right'
    def turn_left(self):
        return f'{self.name} is turned left'
    def show_speed(self):
        return f'Current speed is {self.speed}.'
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}.')
        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for town car.'
        else:
            return f'Speed of {self.name} is normal for town car.'
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')
        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for work car.'
        else:
            return f'Speed of {self.name} is normal for work car.'
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police(self):
        if self.is_police:
            return f'{self.name} is from police department.'
        else:
            return f'{self.name} is not from police department.'
audi = SportCar(100, 'red', 'Audi', False)
hundai = TownCar(60, 'white', 'Salaris', False)
lada = WorkCar(30, 'grey', 'Priora', True)
ford = PoliceCar(110, 'blue', 'Ford', True)
print(lada.turn_left())
print(f'When {hundai.turn_right()} then {hundai.stop()}')
print(f'{lada.go()} with speed exactly {lada.show_speed()}')
print(f'{lada.name} is {lada.color}')
print(f'Is {audi.name} a police car? {audi.is_police}')
print(f'Is {lada.name} a police car? {lada.is_police}')
print(audi.show_speed())
print(hundai.show_speed())
print(ford.police())
print(ford.show_speed())

print("Задание №5")
# про карандаш, ручку и маркер
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Запуск отрисовки {self.title}'
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Вы взяли: {self.title}. Запуск отрисовки ручкой.'
class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Вы взяли: {self.title}. Запуск отрисовки карандашом.'
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Вы взяли: {self.title}. Запуск отрисовки маркером.'
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())

