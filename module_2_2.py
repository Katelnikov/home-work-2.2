#  На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
name = ('Введите числа 3 целых: ')
print(name)
first = int(input())
second = int(input())
third = int(input())
# Если все числа равны между собой, то вывести 3
if first == second == third:
    print(3)
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
elif first == second or second == third or first == third:
    print(2)
# Если равных чисел среди 3-х вообще нет, то вывести 0
elif first != second != third:
    print(0)