# Практическая работа №9
# Вариант 5
#



def n5(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        min_val = min(matrix[i])
        min_idx = matrix[i].index(min_val)
        matrix[i][min_idx] = 0 if min_val % 2 == 0 else 1
    return matrix

def write_array_to_file(filename, array,):

    with open(filename, 'w', encoding='utf-8') as file:
        for item in array:
            file.write(str(item))

def read_array_from_file(filename,):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.readlines()
            
            if not content:
                return []
            
            items = content

            return items
    
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

M = [[5, 2, 9],[4, 7, 1],[8, 3, 6]]

#A = read_array_from_file("ИАР_ЗИТ252_vvod.txt")
n5(M)
write_array_to_file("ИАР_ЗИТ252_vvod.txt",M)