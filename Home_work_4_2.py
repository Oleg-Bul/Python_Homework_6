# Задайте список из n чисел последовательности (1+1/n)^n и 
# выведите на экран их сумму.
# Пример:
# Для n = 6:
# [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.521626371742]

# Старое решение
# n = int(input('Введите число '))
# numbers = []
# sum = 0
# for i in range(1, n+1):
#     sum = (1+1/i)**i
#     numbers.append(sum)
# print(numbers)

# n = int(input('Введите число '))
# sum = 0
# numbers = [i in range(1, n+1)]


# Упращенное решение
n = int(input('Введите число '))


def f(x):
    return (1+1/x)**x


print([f(i) for i in range(1, n+1)])
