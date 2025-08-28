# iteratsiya - bu for sikl orqali ololadigan ma'lumotlarimizga aytiladi
# (list, string, dict, tuple, set va h.k)

# functional programming - bumap, filter, reduce va lambda
# shu 3 tasi functional programming.

# map() - buni arifmetik amallar bilan ishlatiladi.
# o'ziga 2 ta ma'lumot qabul qiladi
# 1. doimo funksiya (lambda)
# 2. iteratsiya bo'ladigan ma'lumotlar

# map - o'ziga qabul qilgan iteratsiya bo'ladigan ma'lumotlarni o'zgartirish.
#
# lst = [1,2,3,4,5,6,7,8,9,10]
# new_numbers = list(map(lambda x: x + 1, lst))
# print(new_numbers)

# filter - ma'lumotlarni saralash
# o'ziga 2 ta argument
# 1. doimo funksiya (lambda)
# 2. iteratsiya bo'ladigan ma'lumotlar

# filterni vazifasi iteratsiya bo'ladigan ma'lumotlarni saralash
# lst = [1,2,3,4,5,6,7,8,9,10]
# new_filter = list(filter(lambda x: x % 2 == 0, lst))
# print(new_filter)

# from functools import reduce
#
# # list ni ichidagi ma'lumotlarni jami qiymatini chiqarish
# lst = [1,2,3,4,5,6,7,8,9,10]
# total_answer = reduce(lambda x, y: x + y, lst)
# print(total_answer)

# from datetime import datetime

# birth_year = int(input("Tug'ilgan yilingizni kiriting: "))
# today = datetime.now()
# age = birth_year - today.year
# print("Sizning yoshingiz", age)


import random
# random raqam chiqarish
print(random.randint(1, 100))
# fruits = ["Olma", "Anor", "Olcha", "Giloz"]
# # qayerdan tanlashni korsatish
# print(random.choice(fruits))
