# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hJekNRNviZUH6GagfkRXeCKgiSy4cUTO
"""

#1
a = 5
b_str = input('b:')
b = int(b_str)
s = a*b
print(s)
#работает, отвечаю

#2
b_str = input('b:')
b = int(b_str)
a_str = input('a:')
a = int(a_str)
s = (a+b)**2
print(s)
#работает, отвечаю

#3
a = 15
b = 10
c_str =input('C:')
c = int(c_str)
r = (a+b)/c
print(r)
#работает, отвечаю

#4
a = int(input('Введите a:'))
b = int(input('Введите b:'))
s = (a**2)+(2*a*b)+(b**2)
print(f"({a}**2)+(2*{a}*{b})+({b}^2)")
#работает, отвечаю

#5
a = float(input("Введите длину первой стороны треугольника: "))
b = float(input("Введите длину второй стороны треугольника: "))
c = float(input("Введите длину третьей стороны треугольника: "))
pe = a + b + c
s = pe/ 2
ar = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Площадь треугольника:", ar)
print("Периметр треугольника:", pe)
#работает, отвечаю

#6
a = float(input())
b = float(input())
x = ((a**3 + 14)/ 5)* b
print(x)
#работает, отвечаю

#7
a = float(input('Введите a:'))
n = float(input('Введите n:'))
a2 = a**2
r = a2 // n
print(r)

# 8.1) Деление дробных чисел без остатка
a = int(input('Введите a:'))
b = int(input('Введите b: '))
print(a//b)

# 8.2) Умножениe двух натуральных чисел
a = int(input('Введите a:'))
b = int(input('Введите b: '))
if ((a<=0) or (b<=0)) :
    print("миша все фигня , переделывай")
else:
    print(a*b)

# 8.3 Получение остатка от деления двух натуральных чисел
a = int(input('Введите a:'))
b = int(input('Введите b: '))
if ((a<=0) or (b<=0)) :
    print("миша все фигня , переделывай")
else:
    print(a % b)

"""сложный уровень

"""

#1
sec = int (input ('Введите кол-во секунд: '))
h = sec // 3600
m = (sec-h*3600) // 60
s = sec % 60
print (h,'час.', m,'мин.', s,'сек.')

"""из 5000 сек
1ч 23м 20с

"""



"""Введите число n: 6
Результат равен: 738


"""