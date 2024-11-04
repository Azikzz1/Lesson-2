# декомпозиция проекта в отдельные файлы и директории
# From & import это инструменты для работы с модулями, директориями, классами и файлами

# import lesson1
# arzy = lesson1.Person("Арзы", 25, "Бишкек")
# arzy.introduce()
#
# from lesson1 import Person
# arzy = Person("Арзы", 25, "Бишкек")
# arzy.introduce()


# Принципы ООП
# Объектно-ориентированное программирование (ООП) — это парадигма программирования, которая основывается на
#    представлении программы как совокупности объектов, взаимодействующих между собой. Основные принципы ООП включают:

# Наследование: позволяет одному классу (производному) унаследовать свойства и методы другого класса (базового),
#    расширяя или изменяя их. Наследование способствует повторному использованию кода и созданию иерархии классов.

# Полиморфизм: предоставляет возможность объектам разных классов обрабатывать одно и то же сообщение по-разному.
#   С помощью полиморфизма можно создавать гибкие интерфейсы, работающие с разными типами объектов,
#    что повышает гибкость и масштабируемость кода.

# Инкапсуляция: предполагает объединение данных и методов, работающих с этими данными, в единое целое — объект.
#   Это позволяет скрыть внутреннее устройство объекта и защитить данные от прямого доступа и изменений извне.

# Абстракция: этот принцип позволяет выделить ключевые характеристики объектов, скрывая детали их реализации.
#    Благодаря абстракции, можно сосредоточиться на общих свойствах и поведении объектов, игнорируя излишние детали.

# Базовый\Супер\Родительский\
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def introduce(self):
        return f"Я {self.name}, мой уровень здоровья: {self.health}"

    def rest(self):
        self.health += 10
        return f"{self.name} отдыхает и восстанавливает здоровье. Новое здоровье: {self.health}"

    def action(self):
        return f"{self.name} выполняет базовое действие.\n"


# Класс Mage, наследующийся от Hero
class Mage(Hero):
    def __init__(self, name, health, mana=100):
        super().__init__(name, health)
        self.mana = mana

    def cast_spell(self):
        if self.mana >= 10:
            self.mana -= 10
            return f"{self.name} использует заклинание! Оставшаяся мана: {self.mana}"
        else:
            return f"{self.name} недостаточно маны для заклинания!"

    def action(self):
        base_action = super().action()
        spell_result = self.cast_spell()  # Вызов метода внутри другого метода
        return f"{base_action} {spell_result}"


def hero_action(hero):
    print(hero.introduce())
    print(hero.rest())
    print(hero.action())


mage = Mage("Гэндальф", 100, 50)

hero_action(mage)


class Tank(Hero):
    def __init__(self, name, health, power=100, hit=20):
        super().__init__(name, health)
        self.power = power
        self.hit = hit

    def cast_spell(self):
        if self.power >= 100:
            self.hit += 10
            return f"{self.name} делает удар! Если урон равен 10, то здоровье понижается: {self.hit}"
        else:
            return f"{self.name} недостаточно доровья, чтоб нанести полноценный урон!"

    def action(self):
        action_1 = super().action()
        spell_result_1 = self.cast_spell()
        return f"{action_1} {spell_result_1}"


def hero_action(hero):
    print(hero.introduce())
    print(hero.rest())
    print(hero.action())


tank = Tank("Chica", 100)

hero_action(tank)
