# Дан список элементов 1, 3, 22, 7, 12, 8, 2 (могут быть какие-то другие значения, ввод данных делать не нужно)
# 1. показать каждый элемент, последняя цифра которого 2
# 2. показать произведение чисел, последняя цифра которого 2

product_of_numbers = 1
for i in 1, 3, 22, 7, 12, 8, 2:
    if i % 10 == 2:
        print(f"Число {i} заканчивается на 2")
        product_of_numbers = product_of_numbers * i
print(f"Произведение чисел, заканчивающихся на 2: {product_of_numbers}")
