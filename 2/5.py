# Задание 5 (необязательное)
# Имеется список с транспортными номерами. Необходимо написать код, который проверит каждый номер на валидность (1 буква, 3 цифры, 2 буквы, 2-3 цифры). Обратите внимание, что не все буквы кириллического алфавита используются в транспортных номерах.

# Если номер валиден, то вывести его в нужном формавте (пример ниже), а если не валиден — вывести текст. При решении помогут регулярные выражения, с которыми будет знакомство на практике.

# Примеры работы программы:

# car_ids = ['А222ВС96', 'АБ22ВВ193']

# Результат:

# Номер А222ВС валиден. Регион: 96
# Номер АБ22ВВ193 не валиден

import re 
car_ids = ['А222ВС96', 'АБ22ВВ193']
for car_id in car_ids:
   number = r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}"
   if (re.match(number, car_id)):
     print('Номер', car_id[0:6], 'валиден. Регион:', car_id[6:len(car_id)])
   else:
     print('Номер', car_id,'не валиден')