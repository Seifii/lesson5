# class Human:
#     height = 170
#     satiety = 50
# class Student(Human):
#     safety = 0
# class Worker(Human):
#     satiety = 100
# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 60
# class Parent(Grandparent):
#     age = 40
# class Child(Parent):
#     height = 50
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)
#
#
# nick = Child()

# nick = Student()
# ann = Worker()
# print(nick.satiety)
# print(ann.satiety)


#
# class Hello_world:
#     hello = "Hello"
#     _hello = "_Hello"
#     __hello = "__Hello"
#     def __init__(self):
#         self.world = "World"
#         self._world = "_World"
#         self.__world = "__World"
#     def printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
# class Hi(Hello_world):
#     def hi_print(self):
#         print(self.hello)
#         print(self.world)
#         print(self._hello)
#         print(self._world)
#         print(self.__hello)
#         print(self.__world)
#
# hello = Hello_world()
# hello.printer()
# hi = Hi()
# hi.hi_print

#
# class Hello:
#     def __init__(self):
#         print("Hello!")
# class Hello_World(Hello):
#     def __init__(self):
#         super().__init__()
#         print("World!")
#
# hello_world = Hello_World()


# class Class1:
#     var = 20
#     def __init__(self):
#         self.var = 10
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
# hello_world = Class2()

class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128
class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "4k"
class SmartPhone(Display, Computer):
    def print_info(self):
        print(self.model)
        print(self.resolution)
        print(self.memory)
iphone = SmartPhone(model = "Last")
iphone.print_info()