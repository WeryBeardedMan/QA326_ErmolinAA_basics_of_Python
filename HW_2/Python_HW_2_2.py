# Дано число. Напечатать, если число делится на 3, “ok”, в противном случае - ‘:(’
#
print("Введите целое число, если число делится на 3 - выйдет сообщение “ok”, в противном случае - ':('")
num = int(input())
if num % 3 == 0:
    print("ok")
else:
    print(":(")
