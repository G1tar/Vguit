# Практическая работа №1
#1

# №1 Дана матрица B[N, М]. Найти в каждой строке матрицы максимальный и минимальный элементы и поменять их с первым и последним элементами строки соответственно.

def n1(matrix):
    N = len(matrix)
    M = len(matrix[0])
    for i in range(N):
        row = matrix[i]
        min_val = min(row)
        max_val = max(row)
        min_idx = row.index(min_val)
        max_idx = row.index(max_val)
        row[0], row[min_idx] = row[min_idx], row[0]
        if max_idx == 0:
            max_idx = min_idx
        elif max_idx == min_idx:
            max_idx = 0
        row[-1], row[max_idx] = row[max_idx], row[-1]
    return matrix

# №2 Дана прямоугольная матрица A[N, N]. Переставить первый и последний столбцы местами и вывести на экран. 

def n2(matrix):
    N = len(matrix)
    for i in range(N):
        matrix[i][0], matrix[i][-1] = matrix[i][-1], matrix[i][0]
    return matrix

# №3 Дана вещественная матрица размером n х m. Переставляя ее строки и столбцы, добиться того, чтобы наибольший элемент (или один из них) оказался в верхнем левом углу. 

def n3(matrix):
    n = len(matrix)
    m = len(matrix[0])
    max_val = matrix[0][0]
    max_i, max_j = 0, 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_i, max_j = i, j
    matrix[0], matrix[max_i] = matrix[max_i], matrix[0]
    for i in range(n):
        matrix[i][0], matrix[i][max_j] = matrix[i][max_j], matrix[i][0]
    return matrix

# №4 Дана квадратная матрица A[N, N], Записать на место отрицательных элементов матрицы нули, а на место положительных — единицы. Вывести на печать нижнюю треугольную матрицу в общепринятом виде. 

def n4(matrix):
    N = len(matrix)
    for i in range(N):
        for j in range(N):
            matrix[i][j] = 1 if matrix[i][j] > 0 else 0 if matrix[i][j] == 0 else 0
    # Печать нижней треугольной
    for i in range(N):
        print("  " * i + " ".join(str(matrix[i][j]) for j in range(i, N)))
    return matrix

# №5 Дана действительная матрица размером n х m, все элементы которой различны. В каждой строке выбирается элемент с наименьшим значением. Если число четное, то заменяется нулем, нечетное - единицей. Вывести на экран новую матрицу. 

def n5(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        min_val = min(matrix[i])
        min_idx = matrix[i].index(min_val)
        matrix[i][min_idx] = 0 if min_val % 2 == 0 else 1
    return matrix

# №6 Дана действительная квадратная матрица порядка N (N — нечетное), все элементы которой различны. Найти наибольший элемент среди стоящих на главной и побочной диагоналях и поменять его местами с элементом, стоящим на пересечении этих диагоналей. 

def n6(matrix):
    N = len(matrix)
    center = N // 2
    max_val = matrix[0][0]
    max_i, max_j = 0, 0
    for i in range(N):
        if matrix[i][i] > max_val:
            max_val = matrix[i][i]
            max_i, max_j = i, i
        if matrix[i][N-1-i] > max_val:
            max_val = matrix[i][N-1-i]
            max_i, max_j = i, N-1-i
    matrix[center][center], matrix[max_i][max_j] = matrix[max_i][max_j], matrix[center][center]
    return matrix

# №7 Для заданной квадратной матрицы сформировать одномерный массив из ее диагональных элементов. Найти след матрицы, просуммировав элементы одномерного массива. Преобразовать исходную матрицу по правилу: четные строки разделить на полученное значение, нечетные оставить без изменения. 

def n7(matrix):
    N = len(matrix)
    diag = [matrix[i][i] for i in range(N)]
    trace_val = sum(diag)
    if trace_val == 0:
        return matrix
    for i in range(N):
        if i % 2 == 0: 
            for j in range(N):
                matrix[i][j] /= trace_val
    return matrix

# №8 Задана квадратная матрица. Получить транспонированную матрицу (перевернутую относительно главной диагонали) и вывести на экран. 

def n8(matrix):
    N = len(matrix)
    transposed = [[matrix[j][i] for j in range(N)] for i in range(N)]
    return transposed

# №9 В данной действительной квадратной матрице порядка n найти наибольший по модулю элемент. Получить квадратную матрицу порядка n — 1 путем отбрасывания из исходной матрицы строки и столбца, на пересечении которых расположен элемент с найденным значением. 

def n9(matrix):
    n = len(matrix)
    max_abs = abs(matrix[0][0])
    max_i, max_j = 0, 0
    for i in range(n):
        for j in range(n):
            if abs(matrix[i][j]) > max_abs:
                max_abs = abs(matrix[i][j])
                max_i, max_j = i, j
    new_matrix = []
    for i in range(n):
        if i == max_i:
            continue
        row = []
        for j in range(n):
            if j == max_j:
                continue
            row.append(matrix[i][j])
        new_matrix.append(row)
    return new_matrix

# №10 Расположить столбцы матрицы D[M, N] в порядке возрастания элементов k-й строки (1 <= k <= М).

def n10(matrix, k):
    M = len(matrix)
    N = len(matrix[0])
    row_k = matrix[k-1]
    sorted_indices = sorted(range(N), key=lambda idx: row_k[idx])
    new_matrix = [[matrix[i][j] for j in sorted_indices] for i in range(M)]
    return new_matrix

# №11 Среди столбцов заданной целочисленной матрицы, содержащих только такие элементы, которые по модулю не больше 10, найти столбец с минимальным произведением элементов и поменять местами с соседним. 

def n11(matrix):
    N = len(matrix)
    M = len(matrix[0])
    min_prod = float('inf')
    min_col = -1
    for j in range(M):
        prod = 1
        valid = True
        for i in range(N):
            if abs(matrix[i][j]) > 10:
                valid = False
                break
            prod *= matrix[i][j]
        if valid and prod < min_prod:
            min_prod = prod
            min_col = j
    if min_col != -1 and min_col + 1 < M:
        for i in range(N):
            matrix[i][min_col], matrix[i][min_col+1] = matrix[i][min_col+1], matrix[i][min_col]
    return matrix

# №12 Дана действительная матрица размером n х m. Требуется преобразовать матрицу: поэлементно вычесть последнюю строку из всех строк, кроме последней. 

def n12(matrix):
    n = len(matrix)
    m = len(matrix[0])
    last_row = matrix[-1]
    for i in range(n-1):
        for j in range(m):
            matrix[i][j] -= last_row[j]
    return matrix

# №13 Найти наибольший и наименьший элементы прямоугольной матрицы и поменять их местами. 

def n13(matrix):
    n = len(matrix)
    m = len(matrix[0])
    min_val = matrix[0][0]
    max_val = matrix[0][0]
    min_i, min_j = 0, 0
    max_i, max_j = 0, 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_i, min_j = i, j
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_i, max_j = i, j
    matrix[min_i][min_j], matrix[max_i][max_j] = matrix[max_i][max_j], matrix[min_i][min_j]
    return matrix

# №14 Составить программу, которая заполняет квадратную матрицу порядка п натуральными числами 1, 2, 3, ..., n2, записывая их в нее «по спирали».  

def n14(n):
    matrix = [[0]*n for _ in range(n)]
    top, bottom = 0, n-1
    left, right = 0, n-1
    num = 1
    while num <= n*n:
        for j in range(left, right+1):
            matrix[top][j] = num
            num += 1
        top += 1
        for i in range(top, bottom+1):
            matrix[i][right] = num
            num += 1
        right -= 1
        for j in range(right, left-1, -1):
            matrix[bottom][j] = num
            num += 1
        bottom -= 1
        for i in range(bottom, top-1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    return matrix

# №15 Среди тех строк целочисленной матрицы, которые содержат только нечетные элементы, найти строку с максимальной суммой модулей элементов. 

def n15(matrix):
    max_sum = -1
    result_row = []
    for row in matrix:
        all_odd = True
        for val in row:
            if val % 2 == 0:
                all_odd = False
                break
        if all_odd:
            row_sum = sum(abs(v) for v in row)
            if row_sum > max_sum:
                max_sum = row_sum
                result_row = row
    return result_row, max_sum

