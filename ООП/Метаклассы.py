class ObjectCreator(object):
    pass
my_object = ObjectCreator()
print(my_object)
print(ObjectCreator)
#Присваиваем  объект переменной
# Копируем его,
# добавляем или изменяем атрибуты,
# передача значения функции,
def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar
MyClass = choose_class('foo')
print(MyClass)
#Метакласс - создание класса для автоматического
#Изменения атрибутов класса в момент создания
#Используется в работе с API, когда нужно
#создавать класс, исходя из данных контекста
# вызываются в момент создания элементов
# __metaclass__
def upper_attr(future_class_name, future_param_class, furure_class_parents):
    #Берем любой атрибут, не начинающийся на "__"
    attrs = ((name,value) for name, value in future_param_class.items() if not name.startswith("__"))
    uppercase_attr = dict((name.upper(), value) for name, value in attrs) #Перевод в верхний регистр
    return type(future_class_name, furure_class_parents, uppercase_attr) #Создаем класс с помощью type

class Foo(object):
    bar = 'bip'
    __metaclass__ = upper_attr
    # Метод __new__ вызывается перед __init__
    #Этот метод создает объект и возращает его,
    #В то время, как __init__ просто инициализует объект, переданный
    #В качестве аргумента.
    #Обычно, мы с вами не используем __new__, если только не хотим проконтролировать
    # процесс создания объектов класса.

print(hasattr(Foo,'bar'))
print(hasattr(Foo,"BAR"))
f = Foo()
print(f.bar)

class Person:
    __type = "Person"
   #@staticmethod #Вызов функции, вне зависимости от объекта от этого класса
    def print_type(self):
        print(Person.__type)
Person().print_type()

person = Person()
person.print_type()
