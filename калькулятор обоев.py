import math
print("добро пожаловать в калькулятор обоев")
a = input("Введите длинну комнаты ")
b = input("Введите ширину комнаты ")
c = input("Введите высоту комнаты ")



d = int(input("Введите ширину рулона обоев "))
f = int(input("Введите длину рулона обоев "))

z = math.ceil(((a + b) * 2) / d)

x = math.ceil(f / c)

u = z / x
print(math.ceil(u))

input(...)