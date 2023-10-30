# Создайте словарь всех покупателей и стоимости покупок (для каждого покупателя: стоимость покупки).
# Найти для такого словаря:
# ●	максимальную стоимость покупки и кто совершил эту покупку
# ●	кол-во сделанных продаж.

purchases = {"Иванов":	1500,
             "Петров":	12000,
             "Сидоров":	1489,
             "Никоноров":	235,
             "Пупкин":	45876,
             "Васильков":	245,
             "Сталин":	21,
             "Брежнев":	256,
             "Хрущев":	6555,
             "Цветаева":	456,
             "Полозкова":	9832,
             "Миладзе":	214,
             "Лепс":	411
             }
print(f"Максимальную покупку совершил '{max(purchases, key=purchases.get)}' на сумму: {purchases[max(purchases, key=purchases.get)]}")
print(f"Количество сделанных продаж: {len(purchases)}")