# вывести кол-во дней в зависимости от года. Год определяет пользователь
# год, номер которого кратен 400, — високосный;
# остальные годы, номер которых кратен 100, — невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300);
# остальные годы, номер которых кратен 4, — високосные[5];
# все остальные годы — невисокосные
#
print("Введите интересующий вас год, чтобы узнать количество дней в этом году:")
year = int(input())
if year % 400 == 0:
    print('Количество дней в этом году: 366')
elif year % 100 == 0:
    print('Количество дней в этом году: 365')
elif year % 4 == 0:
    print('Количество дней в этом году: 366')
else:
    print('Количество дней в этом году: 365')
