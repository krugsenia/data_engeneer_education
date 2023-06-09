# Задание 4
# У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах за произвольный период по странам (структура данных в примере). Необходимо написать код, который рассчитает среднюю температуру за период в Цельсиях(!) для каждой страны.

# Пример работы программы:

# countries_temperature = [
#     ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
#     ['Германия', [57.2, 55.4, 59, 59, 53.6]],
#     ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
#     ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
# ]
# Результат:

# Средняя температура в странах:
# Таиланд  -  23.9 С
# Германия  -  13.8 С
# Россия  -  3.7 С
# Польша  -  12.0 С

countries_temperature = [
  ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
  ['Germany', [57.2, 55.4, 59, 59, 53.6]],
  ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
  ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
print ('Средняя температура в странах:')
for T in countries_temperature:
  print(T[0],round(((sum(T[1])/len(T[1]))-32)/1.8,1),'C')
