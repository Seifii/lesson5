# class Human:
#     height = 170
#     satiety = 50
# class Student(Human):
#     safety = 0
# class Worker(Human):
#     satiety = 100
class Grandparent:
    height = 170
    satiety = 100
    age = 60
class Parent(Grandparent):
    age = 40
class Child(Parent):
    height = 50
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)


nick = Child()

nick = Student()
ann = Worker()
print(nick.satiety)
print(ann.satiety)