# buitins methods - bu interpretator bilan birga o'rnatilgan kutubxonalarga aytiladi
# functionalniy programming - map, reduce, filter har doim lambda funksiya
# orqali bajariladigan amallarga aytiladi
# map - bu

grades = [3, 4, 5, 2]
new_grades = list(map(lambda x: x + 1, grades))
print(new_grades)
# [4, 5, 6, 3]