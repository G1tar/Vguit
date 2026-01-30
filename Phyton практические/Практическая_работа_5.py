# Практическая работа №5

# №1 Дана строка, содержащая русскоязычный текст. Найти количество слов, начинающихся с буквы "е". 

def n1(text:str):
    words = text.split()
    count  = 0
    for word in words:
         cleaned_word = word.strip(".,!?;:-()\"' ")
         if cleaned_word and cleaned_word[0].lower() == 'е':
            count += 1
    print(count)

# №2 В строке заменить все двоеточия (:) знаком процента (%). Подсчитать количество замен.

def n2(text:str):
    counte = 0
    text2 = ""
    for i in range(0,len(text)):
        if text[i] == ":":
            text2 += "%"
            counte += 1
        else:
            text2+=text[i]
    print(f"{text2} \nКолличество замен: {counte}")

# №3 В строке удалить символ точку (.) и подсчитать количество удаленных символов.

def n3(text:str):
    counte = 0
    text2 = ""
    for i in range(0,len(text)):
        if text[i] == ".":
            text2 += ""
            counte += 1
        else:
            text2+=text[i]
    print(f"{text2} \nКолличество удаленных символов: {counte}")

# №4 В строке заменить букву(а) буквой (о). Подсчитать количество замен. Подсчитать, сколько символов в строке.

def n4(text:str):
    counte = 0
    text2 = ""
    for i in range(0,len(text)):
        if text[i] == "а":
            text2 += "о"
            counte += 1
        else:
            text2+=text[i]
    print(f"{text2} \nКолличество замен: {counte}\nКолличество символов в строке: {len(text2)}")

# №5 В строке заменить все заглавные буквы строчными.

def n5(text:str):
    print(text.lower())

# №6 В строке удалить все буквы "а"  и подсчитать количество удаленных символов.

def n6(text:str):
    counte = 0
    text2 = ""
    for i in range(0,len(text)):
        if text[i] == "а":
            text2 += ""
            counte += 1
        else:
            text2+=text[i]
    print(f"{text2} \nКолличество удаленных символов: {counte}")

# №7 Дана строка. Преобразовать ее, заменив звездочками все буквы "п", встречающиеся среди первых n/2 символов. Здесь n - длина строки. 
def n7(text:str):
    n = round(len(text)/2)
    text2=""
    for i in range(0,len(text)):
        if i<=n:
            if text[i] == "п":
                text2 += "*"
            else:
                text2+=text[i]
        else:
            text2+=text[i]
    print(text2)

# №8 Дана строка, заканчивающаяся точкой. Подсчитать, сколько слов в строке. 
def n8(text:str):
    prev_sym = ""
    count = 1
    for i in range(0,len(text)):
        if prev_sym == " " and text[i] != " ":
            a = prev_sym
            b = text[i]
            count += 1
        prev_sym = text[i]
    print(count)

# №9 Определить, сколько раз в тексте встречается заданное слово. 

def n9(text:str,s:str):
    print(text.count(s))

# №10 Дана строка-предложение на английском языке. Преобразовать строку так, чтобы каждое слово начиналось с заглавной буквы.

def n10(text:str):
    text2 = ""
    text2 += text[0].upper()
    prev_char=""
    for i in range(1,len(text)):
        if prev_char == " " and text[i] != " ":
            text2 += text[i].upper()
        else:
            text2 += text[i]
        prev_char = text[i]
    print(text2)

# №11 Дана строка. Подсчитать самую длинную последовательность подряд идущих букв «н». Преобразовать ее, заменив  точками все восклицательные знаки. 

def n11(text:str):
    text2 =""
    count=0
    countn=0
    prev_char=""
    for i in range(0,len(text)):
        if prev_char == "н" and text[i] == "н" :
            count += 1
        if (prev_char != " " and text[i] == " ") and countn < count :
            countn = count 
            count = 0
        if text[i] == "!":
            text2 += "."
        else:
            text2 += text[i]
        prev_char = text[i]
    print(f"Колличество самой длинной последовательности подряд идущих букв «н»: {countn+1}\nПолучившаяся строка : {text2}")

# №12 Дана строка. Вывести все слова, оканчивающиеся на букву "я".

def n12(text:str):
    words = text.split()
    count  = 0
    for word in words:
         if word[len(word)-1] == "я":
             print(word)

# №13  Дана строка символов, среди которых есть одна открывающаяся и одна закрывающаяся скобки. Вывести на экран все символы, расположенные внутри этих скобок. 

def n13(text:str):
    first_bracket = 0
    second_bracket = 0
    for i in range(0,len(text)):
        if text[i] == "(":
            first_bracket = i
        if text[i] == ")":
            second_bracket = i
    print(text[first_bracket:second_bracket+1])

# №14  Дана строка. Вывести все слова, начинающиеся на букву "а" и слова оканчивающиеся на букву "я". 

def n14(text:str):
    words = text.split()
    count  = 0
    for word in words:
         if word[len(word)-1] == "я" or word[0] == "а":
             print(word)

# №15 Дана строка текста. Подсчитать количество букв «т» в строке.

def n15(text:str):
    count = 0
    for i in range(0,len(text)):
        if text[i] == "т":
            counte += 1
    print(f"Колличество букв т : {count}")
