# 8.1 "Try и Except"
# Задание "Программистам всё можно":

def add_everything_up (a, b):   # может быть как числа(int, float), так и строки(str)
    try:
        # i=a+b # почему много после запятой?
       i = round((a + b), 3)
    except TypeError:
        i = str(a) + str(b)
    return i

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

print(add_everything_up('ОбеДве ', 'строки'))
