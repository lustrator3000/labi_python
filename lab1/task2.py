# TODO Найдите количество книг, которое можно разместить на дискете

size = 1.44 #Мб - объём дискеты
pages = 100
str_in_page = 50
symbols_in_str = 25
cost = 4 #байт на символ
books = round(size * 1024 ** 2) // (pages * str_in_page * symbols_in_str * cost)

print("Количество книг, помещающихся на дискету:", books)
