# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип экземпляра (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.
# тогда на выходе два модуля отдельных - первый со всеми классами с семинара + класс ФАБРИКА, второй - класс по сериализации данных например


# Класс "фабрика" возвращающий информацию о животных
class FactoryAnimal:
    # метод возвращающий информацию о переданном в него объекте
    def get_animal_info(self, animal):
        return animal.__str__()


# Класс фабрика, возвращающий объект переданого имени класса
class FactoryClassAnimal:
    def __init__(self, name_class_animal):
        self.name_class_animal = name_class_animal

    # Метод возвращающий объект переданного класса
    def get_new_animal(self, *args):
        return self.name_class_animal(*args)