# Практическая работа №7
import math
from re import match
# 1
# №1 Составить программу для вычисления площади разных геометрических фигур.

def n1():
    shape = input('Введите фигуру: ')
    if shape == 'circle':
        radius = input('Введите радиус: ')
        return 3.14159 * radius ** 2
    elif shape == 'rectangle':
        length = input('Введите длину: ')
        width = input('Введите высоту: ')
        return length * width
    elif shape == 'triangle':
        base = input('Введите основание: ')
        height = input('Введите высоту: ')
        return 0.5 * base * height
    else:
        return "Неизвестная фигура. Используйте 'circle', 'rectangle' или 'triangle'."



# №2 Вычислить площадь правильного шестиугольника со стороной а, используя подпрограмму вычисления площади треугольника. 

def triangle_area(a):
    return (math.sqrt(3) / 4) * a ** 2

def n2(a):
    return 6 * triangle_area(a)

# №3 Даны катеты двух прямоугольных треугольников. Написать функцию вычисления длины гипотенузы этих треугольников. Сравнить и вывести какая из гипотенуз больше, а какая меньше. 

def n3(a1, b1, a2, b2):
    hyp1 = math.sqrt(a1**2 + b1**2)
    hyp2 = math.sqrt(a2**2 + b2**2)
    print(f"Гипотенуза первого треугольника: {hyp1}")
    print(f"Гипотенуза второго треугольника: {hyp2}")
    if hyp1 > hyp2:
        print("Гипотенуза первого треугольника больше.")
    elif hyp1 < hyp2:
        print("Гипотенуза второго треугольника больше.")
    else:
        print("Гипотенузы равны.")
    return hyp1, hyp2

# №4 Даны две дроби A/B и C/D (А, В, С, D — натуральные числа). Составить программу деления дроби на дробь. Ответ должен быть несократимой дробью. Использовать подпрограмму алгоритма Евклида для определения НОД. 

def gcd(a, b):
    #Алгоритм Евклида для нахождения НОД
    while b != 0:
        a, b = b, a % b
    return a

def n4(A, B, C, D):
    numerator = A * D
    denominator = B * C
    
    divisor = gcd(numerator, denominator)
    
    numerator //= divisor
    denominator //= divisor
    
    return numerator, denominator

# №5 Даны две дроби A/B и C/D (А, В, С, D — натуральные числа). Составить программу вычитания из первой дроби второй. Ответ должен быть несократимой дробью. Использовать подпрограмму алгоритма вклида для определения НОД. 

def gcd(a, b):
    #Алгоритм Евклида для нахождения НОД
    while b != 0:
        a, b = b, a % b
    return a

def n5(A, B, C, D):
    numerator = A * D - C * B
    denominator = B * D
    divisor = gcd(abs(numerator), denominator)
    numerator //= divisor
    denominator //= divisor
    
    return numerator, denominator

# №6 Составить программу нахождения наибольшего общего делителя (НОД) и наименьшего общего кратного (НОК) двух натуральных чисел НОК(А, В) = (A*B)/НОД(A,B). Использовать подпрограмму алгоритма вклида для определения НОД. 

def gcd(a, b):
    #Алгоритм Евклида для нахождения НОД
    while b != 0:
        a, b = b, a % b
    return a

def n6(a,b):
     return abs(a * b) // gcd(a, b)

# №7 Даны числа X, Y, Z, Т — длины сторон четырехугольника. Вычислить его площадь, если угол между сторонами длиной X и У — прямой. Использовать две подпрограммы для вычисления площадей: рямоугольного треугольника и прямоугольника. 

def right_triangle_area(leg1, leg2):
    #Площадь прямоугольного треугольника по катетам
    return 0.5 * leg1 * leg2

def rectangle_area(side1, side2):
    return side1 * side2

def n7(X, Y, Z, T):
    area = right_triangle_area(X, Y) + rectangle_area(Z, T)
    return area

# №8  Найти все натуральные числа, не превосходящие заданного n, которые делятся на каждую из своих цифр.

def is_divisible_by_its_digits(n):
    #Проверяет, делится ли число на каждую из своих цифр
    original_n = n
    while n > 0:
        digit = n % 10
        if digit == 0 or original_n % digit != 0:
            return False
        n //= 10
    return True

def n8(n):
    result = []
    for i in range(1, n + 1):
        if is_divisible_by_its_digits(i):
            result.append(i)
    return result

# №9 Из заданного числа вычли сумму его цифр. Из результата вновь вычли сумму его цифр и т. д. Через сколько таких действий получится нуль? 

def n9(num):
    count = 0
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    while n > 0:
        n -= total
        count += 1
    return count

# №10 На отрезке [100, N] (210 < N < 231) найти количество чисел, составленных из цифр а, b, с. 

def is_composed_of_digits(num, a, b, c):
    #Проверяет, состоит ли число только из цифр a, b, c
    digits = {a, b, c}
    str_num = str(num)
    return all(int(digit) in digits for digit in str_num)

def n10(start, end, a, b, c):
    count = 0
    for num in range(start, end + 1):
        if is_composed_of_digits(num, a, b, c):
            count += 1
    return count

# №11 Два простых числа называются «близнецами», если они отличаются друг от друга на 2 (например, 41 и 43). Напечатать все пары «близнецов» из отрезка [n, 2n], где n — заданное натуральное число, большее 2.. 

def is_prime(n):
    #Проверяет, является ли число простым
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def n11(n):
    if n <= 2:
        n = 3
    twins = []
    for i in range(n, 2*n - 1):
        if is_prime(i) and is_prime(i + 2):
            twins.append((i, i + 2))
    return twins\

# №12 Два натуральных числа называются «дружественными», если каждое из них равно сумме всех делителей (кроме его самого) другого (например, числа 220 и 284). Найти все пары «дружественных» чисел, которые не больше данного числа N.

def sum_of_divisors(n):
    #Возвращает сумму всех делителей числа n, кроме самого n
    if n == 1:
        return 0
    total = 1  # 1 всегда является делителем
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # избегаем повторения для квадратов
                total += n // i
    return total

def n12(N):
    amicable_pairs = []
    for a in range(2, N + 1):
        b = sum_of_divisors(a)
        # Проверяем условия дружественности: b <= N, a < b, sum_of_divisors(b) == a
        if b <= N and a < b and sum_of_divisors(b) == a:
            amicable_pairs.append((a, b))
    return amicable_pairs

# №13 Натуральное число, в записи которого n цифр, называется числом Армстронга, если сумма его цифр, возведенная в степень n, равна самому числу. Найти все числа Армстронга от 1 до к. 
def is_armstrong_number(n):
    #Проверяет, является ли число числом Армстронга
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def n13(k):
    armstrong_numbers = []
    for i in range(1, k + 1):
        if is_armstrong_number(i):
            armstrong_numbers.append(i)
    return armstrong_numbers

# №14 Составить программу для нахождения чисел из интервала [М, N], имеющих наибольшее количество делителей. 

def count_divisors(n):
    #Возвращает количество делителей числа n
    if n == 1:
        return 1
    
    count = 2  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def n14(M, N):
    max_div_count = 0
    result_numbers = []
    for num in range(M, N + 1):
        div_count = count_divisors(num)
        
        if div_count > max_div_count:
            max_div_count = div_count
            result_numbers = [num]
        elif div_count == max_div_count:
            result_numbers.append(num)
    return result_numbers, max_div_count

# №15 Найти все простые натуральные числа, не превосходящие n, двоичная запись которых представляет собой палиндром, т. е. читается одинаково слева направо и справа налево.
def is_prime(n):
    #Проверяет, является ли число простым
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_binary_palindrome(n):
    #Проверяет, является ли двоичная запись числа палиндромом
    binary = bin(n)[2:]  
    return binary == binary[::-1]

def n15(n):
    result = []
    for i in range(2, n + 1):
        if is_prime(i) and is_binary_palindrome(i):
            result.append((i, bin(i)[2:]))
    return result