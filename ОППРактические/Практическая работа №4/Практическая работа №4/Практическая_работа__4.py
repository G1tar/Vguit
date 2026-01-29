# Практическая работа №4

# №1 Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно. 

from binascii import b2a_base64


def atob(a:int,b:int):
    for i in range(a, b + 1):
        print (i)

# №2 Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания в противном случае.

def atob_biggerorsmaller(a:int,b:int):
    if a<b :
        for i in range(a, b + 1):
            print (i)
    else :
        for i in range(a, b-1, -1):
            print (i)

# №3 Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания. 

def atob_even(a:int,b:int):
    for i in range(a, b - 1, -1):
        if i % 2 != 0:
            print(i)

# №4 Дано несколько чисел. Вычислите их сумму. Сначала вводите количество чисел N, затем вводится ровно N целых чисел. Постройте решение так, чтобы использовалось минимальное количество переменных.

def sum_min(n):
    summ = 0
    for i in range(0,n):
        summ += int(input(f'Введите число {i+1}: '))
    print (summ)

# №5 По данному натуральному n вычислите сумму 1^3+2^3+3^3+...+n^3.

def sum_degree(n:int):
    summ = 0
    for i in range (1,n+1):
        summ += i**3
    print (summ)

# №6 Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!. По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.

def factorial(n:int):
    factor = 1
    for i in range (1,n+1):
        factor *= i
    print (factor)

# №7 По данному натуральном n вычислите сумму 1!+2!+3!+...+n!. В решении этой задачи можно использовать только один цикл. Пользоваться математической библиотекой math в этой задаче запрещено. 

def sum_factorial_one_cycle(n:int):
    summ = 0
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        summ += factorial
    print(summ)

# №8 По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.

def ladder(n:int):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

# №9 Пользователь вводит число N с клавиатуры - количество чисел из ряда Фибоначчи. Посчитайте сумму этих чисел.

def fibonachi(n:int):
    fib_prev = 0
    fib_curr = 1
    summ = fib_prev;
    n -= 1
    while n > 0:
        summ+=fib_curr
        c = fib_prev
        fib_prev = fib_curr
        fib_curr += c
        n -= 1
    print (summ)

# №10 Пользователь вводит два числа N и K с клавиатуры. N - количество чисел из ряда Фибоначчи, K - порядковый номер в ряду, с которого нужно начать. Посчитайте сумму этих чисел. В решении этой задачи можно использовать только один цикл.

def fibonachi_num(n:int, k:int):
    fib_prev = 0
    fib_curr = 1
    summ = fib_prev
    position = 0
    k -= 1
    while n > 0:
        if position >= k:
            summ+=fib_prev
        c = fib_prev
        fib_prev = fib_curr
        fib_curr += c
        n -= 1
        position += 1
    print (summ)

