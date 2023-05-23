# Задание 3
# Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек.
# Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки! Но мы не будем никого знакомить, если кто-то может остаться без пары:

# Примеры работы программы:

# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# Результат:

# Идеальные пары:  
# Alex и Emma  
# Arthur и Kate  
# John и Kira  
# Peter и Liza  
# Richard и Trisha 
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# Результат:
# Внимание, кто-то может остаться без пары!

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Tom']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys_sort = sorted(boys)
girls_sort = sorted(girls)

if len(boys_sort) != len(girls_sort):
  print('Внимание, кто-то может остаться без пары!')
else: 
    print('Идеальные пары')
    for B, G in zip(boys_sort, girls_sort):
        print(B,G)