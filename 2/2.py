# Задание 2
# Напишите программу, которая последовательно запрашивает у пользователя числа (по одному за раз) и после первого нуля выводит сумму всех ранее введенных чисел.
# Примеры работы программы:
# Введите число:  
# 1
# Введите число:  
# 4
# Введите число:  
# 6
# Введите число:  
# 0
# Результат:
# 11
# Введите число:  
# 0
# Результат:

number = int(input("Enter number: "))
list_ = []
while number != 0:
      list_.append(number)
      number = int(input("Enter number: "))
else:
        print(sum(list_))