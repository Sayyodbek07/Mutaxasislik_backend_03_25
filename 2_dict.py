# dict - key=value, yani lugat

phone_book = {
    "Ali": 53464566575,
    "Vali": 54354546,
    "Ozod aka": "Quloqsiz"
}
# get key orqali olib keladi
# print(phone_book.get("Ali"))

# dictdan hamma malumotlarni olib keladi
# print(phone_book.items())
# print(phone_book)

# phone_book.update({"Hasan": 456476765})
# print(phone_book)

# kesish korastilgan key orqali
# removed = phone_book.pop("Vali")
# print(removed)
#
# oxirgi malumotni kesish
# last = phone_book.popitem()
# print(last)
#
# # malmotni borib qoshib keladi
# # Malumot bosa ochirib keladi
# phone_book.setdefault("Vali", 43666666666666)
# print(phone_book)
#
# copy_book = phone_book.copy()
# print(copy_book)
