# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

sum = 0
input_num = input('Введите число: ')

for a in input_num:
    if a.isdigit():
        sum += int(a)

print(sum)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


input_num = int(input('Введите число: '))
list = [1]

for i in range (1,input_num):
    list.append ((i+1) * list [i-1])

print(list)


#либо чеез переменную а не список
temp_num = 1
for i in range (input_num):
    temp_num *= i+1
    print(temp_num, end=' ')

print ()

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

from fractions import Fraction


input_num = int(input('Введите число: '))

list = []
sum = 0
for n in range(1,input_num+1):
    a = (1 + Fraction (1,n))**n
    sum += a #я не стал сумму делать отдельно, это будет просто пробегание по списку
    list.append (a)
print (sum)

print ('\nили')
list = [[],[]]
for n in range(1,input_num+1): #создание списка
    x = 1
    y = n
    x = x+1*y
    x = x**n
    y = y**n
    list[0].append(x)
    list[1].append(y)

for i in range(input_num): #сложение
    if i == 0:
        sum_x = list[0][i]
        sum_y = list[1][i]
    else:
        sum_x = sum_x * list[1][i] + sum_y * list[0][i]
        sum_y *= list[1][i]

print (sum_x,'/',sum_y)

print ('\nили')
sum = 0
for n in range(1,input_num+1):
    sum += (1+1/n)**n
print(sum)

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

from fractions import Fraction


input_num = int(input('Введите число: '))

list = []
sum = 0
for n in range(1,input_num+1):
    a = (1 + Fraction (1,n))**n
    sum += a #я не стал сумму делать отдельно, это будет просто пробегание по списку
    list.append (a)
print (sum)

print ('\nили')
list = [[],[]]
for n in range(1,input_num+1): #создание списка
    x = 1
    y = n
    x = x+1*y
    x = x**n
    y = y**n
    list[0].append(x)
    list[1].append(y)

for i in range(input_num): #сложение
    if i == 0:
        sum_x = list[0][i]
        sum_y = list[1][i]
    else:
        sum_x = sum_x * list[1][i] + sum_y * list[0][i]
        sum_y *= list[1][i]

print (sum_x,'/',sum_y)

print ('\nили')
sum = 0
for n in range(1,input_num+1):
    sum += (1+1/n)**n
print(sum)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


import random

f = open("file.txt")

input_num = 10
# input_num = int(f.readline(1))
# input_num = int(input('Введите число: '))
list = []

for i in range(input_num):
    list.append(random.randint(input_num*-1, input_num))

print(list)
result = 1

for line in f:
    print (list[int(line)], ' * ' , end='' )
    result = result * list[int(line)]

print('= ', result)

# Реализуйте алгоритм перемешивания списка

import random


lenght = 20
list = [i for i in range (lenght)]

print(list, '<-- not mixed')

for i in range(len(list)):
    r = random.randint(i,lenght-1)
    m = list[i]
    list[i] = list[r]
    list[r] = m

print(list, '<-- mixed')

#Функция
random.shuffle(list)
print(list, '<-- shuffle')

