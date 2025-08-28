# Malumot turlari 2 xil turga bolinadi
# 1. Ozgaruvchan  - qoshimcha ozgaruvchi ochilmasdan ozgartiriladigan malumot turlari aytiladi
# 2. Ozgarmas - ozgaruvchi ochilib ozgartiriladigan  malumotlar aytiladii

# Ozgaruvchan
# List
# Dict
# set

# Ozgarmas
# string
# int - float(kasr sonlar) va integer(butun sonlar)
# bool
# tuple

# tuple = ()
# tuples = (2, "String", True, 5.4, [1, 2, 3, 4, 5], {"Name": "Ziyobek"}, (1, 2, 3))
# n = tuples.count(2)
# print(n)

# 1-MISOL
numbers = (12, 45, 3, 22, 5, 89, 1)
print("Eng kichik:", min(numbers))
print("Eng katta:", max(numbers))


fruits = ("apple", "banana", "apple", "orange", "banana", "apple")
print("'apple' soni:", fruits.count("apple"))


cities = ("Toshkent", "Samarqand", "Buxoro", "Xiva")
print("'Buxoro' indeksi:", cities.index("Buxoro"))


a = (1, 2, 3)
b = (4, 5, 6)
new_tuple = a + b
print("Yangi tuple:", new_tuple)


data = (10, 20, 30, 40, 50, 60)
middle_three = data[1:4]  # 20, 30, 40
print("O‘rtadagi 3 element:", middle_three)


# 2-MISOL

text = "python dasturlash tili"
print(text.upper())


text = "HELLO WORLD"
print(text.lower())


text = "   Salom dunyo   "
print(text.strip())


text = "Men Python o‘rganayapman"
print(text.split())


text = "Men Java o‘rganayapman"
print(text.replace("Java", "Python"))
