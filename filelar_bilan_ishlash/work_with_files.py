# enumarate - indekslab beradi
# pythonni ozi bilan ornatilgan kutubxonalar yani methodlar bular builtinga methods deyiladi.
lst = [2, 1, 4, 3, 5, 6, 9, 7, 8, 10]
print(lst)
m = sorted(lst)
print(m)
# tartiblangan royxatni teskari qilish
# n = sorted(lst, reverse=True)
# print(n)

# x mode faylni ochsak 1marta run bersa xato bermidi keyingi martasida xato beradi va ichiga malumot yozib bermidi
# file = open("my_first_file.txt", "x")


# w mode faylni ochsak run bersak keyinchalik hato bermidi va ichida malumot yozsak boladi
# file = open("my_first_file", "w")
# file.write("Hello world")


# a mode ochadi yozadi qoshadi orqasidan keyin run bersak hato bermidi
# file1 = open("my_first_file1.txt", mode="a")
# file1.write("Sayyodbek aqlli bola")


# r mode fileni oqiydi
# read = open("my_first_file1.txt", "r")
# m = read.read()
# print(m)


# file ochishni 2xil usuli bor
# 1. file1 = open("my_first_file2.txt", mode="a")
# 2. with open ("Ziyobek.docs", "a") as Ziyobek:


with open("sayyodbek.doc", "a") as sayyodbek:
     sayyodbek.write("Sayyodbek aqlli")
     sayyodbek.close()


import os
os.remove()