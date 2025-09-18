# OOP - object oriented programming (obyectga yo'nalitirilgan dasturlash)
# Vazifasi: code larni takrorlanishini oldini olish va
# ma'lumotlarni takrorlanishi, himoyalanishini taminlash

# OOP - tamoillari 4 turga bo'linadi
# 1. Meros olish (inheritence)
# 2. Incapsulation
# 3. Polimorfizm
# 4. Abtsraction

# Abstraction - bufunction qaytaradigan function

# Polimorfizm
# Vazifa: Turli xil class larda bir xil nomli methodlarning bir xil vazifa bajarishi.
# class Parrot:
#     def __init__(self):
#         self.voice = "Salom"
#         self.name = "Ozod"
#
#     def speak(self):
#         return f"{self.voice} {self.name} dovdur"
#
#
# class Dog:
#     def __init__(self):
#         self.voice = "Gaf Gaf"
#
#     def speak(self):
#         return f"it shunday gapiradi {self.voice}"
#
#
# bird = Parrot()
# print(bird.speak())
# dog = Dog()
# print(dog.speak())

# Incapsulation - skritnis (yashirish)
# __ - 100% blocklandi
# _ - 50% keyinchalik block lanadi
#
# class Parrot:
#     def __init__(self):
#         self.__voice = "Salom"
#         self.name = "Ozod"
#
#     def speak(self):
#         return self.__voice
#
#     def check_info(self):
#         return self.speak()
#
#
# obj = Parrot()
# print(obj.speak())

# 1. Meros olish (inheritence)
# # Vazifasi: Bir class dan 2 class ga ma'lumot uzatish
# class Car:
#     def __init__(self):
#         self.world = "world"
#
# #
# class Ferrari(Car):
#     def __init__(self):
#         super().__init__()
#
#     def hello (self):
#         return f"hello {self.world}"
#
# obj = Ferrari()
# print(obj.hello("Ziyobek", 17))


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name} {self.age} yosh")


talaba = Student("Ziyobek", 17)

talaba.introduce()

