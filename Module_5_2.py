# Домашняя работа по уроку "Специальные методы классов"
# ***************************************************************************************
#   Цель: понять как работают базовые магические методы на практике.
#
# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче
# "Атрибуты и методы объекта".
#
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку:
# "Название: <название>, кол-во этажей: <этажи>".
#****************************************************************************************

class House:
    def __init__(self, name, numb_floors):
        self.__name = name
        self.__number_of_floors = numb_floors

    def go_to(self, numb_floor):
        if numb_floor > 0 and numb_floor <= self.__number_of_floors:
            i = 1
            while i <= numb_floor:
                print("Тек. этаж:", i)
                i += 1
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.__number_of_floors

    def __str__(self) :
        return f'Название: {self.__name}, кол-во этажей: {self.__number_of_floors}'

def start():
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    # __str__
    # print(str(h1))
    # print(str(h2))
    print(h1)
    print(h2)

    # __len__
    print(len(h1))
    print(len(h2))

if __name__ == '__main__':
    start()