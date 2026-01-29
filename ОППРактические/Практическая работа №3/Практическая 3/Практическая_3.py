# Практическая работа #3

# №1

from tkinter import END


def compare_numbers(a, b):
    if a > b:
        return "Наибольшее число:a" + a
    elif b > a:
        return "Наибольшее число:" + b
    else:
        return "Числа равны"


# №2
def check_even_odd(number):
    if number % 2 == 0:
        return "Число "+number+" четное"
    else:
        return "Число "+number+" нечетное"

# №3
def split_even_odd_digits(number):
    num_str = str(abs(number))
    even_digits = []
    odd_digits = []
    
    for digit in num_str:
        if int(digit) % 2 == 0:
            even_digits.append(digit)
        else:
            odd_digits.append(digit)
    
    return "число"+ str(number) + "\nчетные_цифры"+ str(even_digits) + "\nнечетные_цифры"+ str(odd_digits)

# №4
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    
    return True

# №5
def calculate_average(a, b, c):
    average = (a + b + c) / 3
    return f"Среднее арифметическое чисел {a}, {b}, {c} = {average:.2f}"

# №6

def check_multiple_of_7(number):
    if number % 7 == 0:
        return f"Число {number} кратно 7"
    else:
        return f"Число {number} не кратно 7. Остаток: {number % 7}"

# №7

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} год - високосный"
    else:
        return f"{year} год - не високосный"

# №8

def days_in_month(month, year=None):
    months_31 = [1, 3, 5, 7, 8, 10, 12] 
    months_30 = [4, 6, 9, 11]  
    
    if month == 2: #29 февраля
        if year:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29
        return 28
    elif month in months_31:
        return 31
    elif month in months_30:
        return 30
    else:
        return "Некорректный номер месяца"

# №9

def triangle_area_heron(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return f"Площадь треугольника: {round(area,2)}"
    else:
        return "Треугольник с такими сторонами не существует"

# №10

def check_three_numbers_equal(a, b, c):
    if a == b == c:
        return f"Все три числа ({a}, {b}, {c}) равны"
    else:
        return f"Числа ({a}, {b}, {c}) не равны"

# №11

def check_age(age):
    if age < 0:
        return "Возраст не может быть отрицательным!"
    elif age < 13:
        return "Ребенок"
    elif age < 18:
        return "Подросток"
    elif age < 65:
        return "Взрослый"
    else:
        return "Пенсионер"

# №12

def check_number_sign(number):
    if number > 0:
        return f"Число {number} положительное"
    elif number < 0:
        return f"Число {number} отрицательное"
    else:
        return "Число равно нулю"

# №13

def february_days(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"Год {year} високосный. В феврале 29 дней"
    else:
        return f"Год {year} не високосный. В феврале 28 дней"

# №14

def point_in_square(x, y):
    if 0 <= x <= 5 and 0 <= y <= 5:
        return f"Точка ({x}, {y}) принадлежит квадрату"
    else:
        return f"Точка ({x}, {y}) не принадлежит квадрату"

# №15

def sum_and_difference(a, b):
    sum_result = a + b
    diff_result = abs(a - b)
    return "сумма" + sum_result +  "\nразность" + diff_result + "описание\n" + f"Сумма: {a} + {b} = {sum_result}, Разность: |{a} - {b}| = {diff_result}"

# №16

def check_multiple_3_5(number):
    message = f"Число {number}: "
    
    if number % 3 == 0 and number % 5 == 0:
        message += "кратно и 3, и 5"
    elif number % 3 == 0:
        message += "кратно 3"
    elif number % 5 == 0:
        message += "кратно 5"
    else:
        message += "не кратно ни 3, ни 5"
    
    return message

# №17
def is_century_year(year):
    if year % 100 == 0:
        return f"Год {year} является вековым"
    else:
        return f"Год {year} не является вековым"

# №18

def check_integer_float(number):
    if isinstance(number, int) or number.is_integer():
        return f"Число {number} является целым"
    else:
        return f"Число {number} является дробным"
