# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]
from math import sqrt

numbers2=[]

numbers=[2, -5, 8, 9, -25, 25, 4]

for number in numbers:

    if number>=0 and sqrt(number)%1 == 0:

        numbers2.append(int(sqrt(number)))

       

print(numbers2)
