#Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.

# Вывести на экран сумму всех положительных элементов кратных двум.

 

# TODO: your code here
numbers=[1,7,-3,99,16,-65]
summ=0

for number in numbers:

    if number>0 and number % 2 == 0:

        summ=summ+number

print(summ)

 
