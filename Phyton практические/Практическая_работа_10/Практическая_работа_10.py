
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Настройка основного окна
        self.title("Иванов Артём Романович")  # Замените на ваше ФИО
        self.geometry("800x600")
        self.minsize(600, 400)
        
        # Создание вкладок
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Создание и настройка стиля
        self.style = ttk.Style()
    
        # Ключевая настройка: растягиваем вкладки по ширине
        self.style.configure("TNotebook", tabposition='nsew')
        self.style.configure("TNotebook.Tab", 
                         padding=[20, 3],  # Отступы внутри вкладки
                         width=0,  # Автоматическая ширина
                         stretch=True)  # Растягиваем

        # Создание трех вкладок
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab1, text="Калькулятор")
        self.notebook.add(self.tab2, text="Чекбоксы")
        self.notebook.add(self.tab3, text="Работа с текстом")
        
        # Инициализация вкладок
        self.init_calculator_tab()
        self.init_checkboxes_tab()
        self.init_text_tab()
        
        # Создание меню
        self.create_menu()
        
    def init_calculator_tab(self):
        """Инициализация вкладки калькулятора"""
        # Заголовок
        title_label = tk.Label(self.tab1, text="Простой калькулятор", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=(30, 30))
        
        # Фрейм для ввода чисел
        input_frame = tk.Frame(self.tab1)
        input_frame.pack(pady=10)
        
        # Первое число
        self.num1_var = tk.StringVar()
        num1_label = tk.Label(input_frame, text="Первое число:", font=("Arial", 12))
        num1_label.grid(row=0, column=0, padx=5, pady=10)
        
        self.num1_entry = tk.Entry(input_frame, textvariable=self.num1_var, 
                                   font=("Arial", 12), width=15)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=10)
        
        # Выпадающий список операций
        self.operation_var = tk.StringVar(value="+")
        operations = ["+", "-", "*", "/"]
        
        operation_label = tk.Label(input_frame, text="Операция:", font=("Arial", 12))
        operation_label.grid(row=0, column=2, padx=5, pady=10)
        
        self.operation_menu = ttk.Combobox(input_frame, textvariable=self.operation_var,
                                           values=operations, state="readonly", width=5)
        self.operation_menu.grid(row=0, column=3, padx=5, pady=10)
        
        # Второе число
        self.num2_var = tk.StringVar()
        num2_label = tk.Label(input_frame, text="Второе число:", font=("Arial", 12))
        num2_label.grid(row=0, column=4, padx=5, pady=10)
        
        self.num2_entry = tk.Entry(input_frame, textvariable=self.num2_var,
                                   font=("Arial", 12), width=15)
        self.num2_entry.grid(row=0, column=5, padx=5, pady=10)
        
        # Кнопка вычисления
        calc_button = tk.Button(self.tab1, text="Вычислить", 
                                command=self.calculate, font=("Arial", 12),
                                bg="#4CAF50", fg="white", padx=20, pady=10)
        calc_button.pack(pady=20)
        
        # Поле для результата
        result_frame = tk.Frame(self.tab1, relief=tk.SUNKEN, borderwidth=2)
        result_frame.pack(pady=20, padx=50, fill=tk.X)
        
        result_label = tk.Label(result_frame, text="Результат:", 
                                font=("Arial", 12, "bold"))
        result_label.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.result_var = tk.StringVar(value="0")
        self.result_display = tk.Label(result_frame, textvariable=self.result_var,
                                       font=("Arial", 14), fg="black")
        self.result_display.pack(side=tk.LEFT, padx=10, pady=10)
        
    def calculate(self):
        """Выполнение вычисления"""
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            operation = self.operation_var.get()
            
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Деление на ноль невозможно")
                result = num1 / num2
            else:
                result = 0
                
            self.result_var.set(f"{result:.2f}")
            
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа")
        except ZeroDivisionError as e:
            messagebox.showerror("Ошибка", str(e))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
    
    def init_checkboxes_tab(self):
        """Инициализация вкладки с чекбоксами"""
        # Заголовок
        title_label = tk.Label(self.tab2, text="Выбор варианта", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=(20, 40))
        
        # Фрейм для чекбоксов
        checkboxes_frame = tk.Frame(self.tab2)
        checkboxes_frame.pack(pady=20)
        
        # Переменные для чекбоксов
        self.checkbox1_var = tk.BooleanVar()
        self.checkbox2_var = tk.BooleanVar()
        self.checkbox3_var = tk.BooleanVar()
        
        # Чекбоксы
        self.checkbox1 = tk.Checkbutton(checkboxes_frame, text="Первый", 
                                        variable=self.checkbox1_var,
                                        font=("Arial", 12), padx=20, pady=10)
        self.checkbox1.grid(row=0, column=0, padx=20, pady=10)
        
        self.checkbox2 = tk.Checkbutton(checkboxes_frame, text="Второй", 
                                        variable=self.checkbox2_var,
                                        font=("Arial", 12), padx=20, pady=10)
        self.checkbox2.grid(row=1, column=0, padx=20, pady=10)
        
        self.checkbox3 = tk.Checkbutton(checkboxes_frame, text="Третий", 
                                        variable=self.checkbox3_var,
                                        font=("Arial", 12), padx=20, pady=10)
        self.checkbox3.grid(row=2, column=0, padx=20, pady=10)
        
        # Кнопка для отображения выбора
        show_button = tk.Button(self.tab2, text="Показать выбор", 
                                command=self.show_selection, font=("Arial", 12),
                                bg="#2196F3", fg="white", padx=20, pady=10)
        show_button.pack(pady=30)
        
        # Подпись с инструкцией
        instruction_label = tk.Label(self.tab2, 
                                     text="Выберите один или несколько вариантов, затем нажмите кнопку",
                                     font=("Arial", 10), fg="gray")
        instruction_label.pack(pady=10)
    
    def show_selection(self):
        """Отображение выбранных вариантов"""
        selected = []
        
        if self.checkbox1_var.get():
            selected.append("первый")
        if self.checkbox2_var.get():
            selected.append("второй")
        if self.checkbox3_var.get():
            selected.append("третий")
        
        if not selected:
            messagebox.showinfo("Выбор", "Вы не выбрали ни одного варианта")
        else:
            if len(selected) == 1:
                message = f"Вы выбрали {selected[0]} вариант"
            else:
                message = f"Вы выбрали варианты: {', '.join(selected)}"
            messagebox.showinfo("Выбор", message)
    
    def init_text_tab(self):
        """Инициализация вкладки работы с текстом"""
        # Заголовок
        title_label = tk.Label(self.tab3, text="Работа с текстом", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=(10, 20))
        
        # Текстовое поле с полосами прокрутки
        text_frame = tk.Frame(self.tab3)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Вертикальная полоса прокрутки
        scrollbar_y = tk.Scrollbar(text_frame)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Горизонтальная полоса прокрутки
        scrollbar_x = tk.Scrollbar(text_frame, orient=tk.HORIZONTAL)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Текстовое поле
        self.text_area = tk.Text(text_frame, wrap=tk.NONE,
                                 yscrollcommand=scrollbar_y.set,
                                 xscrollcommand=scrollbar_x.set,
                                 font=("Arial", 11), height=15)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Настройка полос прокрутки
        scrollbar_y.config(command=self.text_area.yview)
        scrollbar_x.config(command=self.text_area.xview)
        
        # Фрейм для кнопок
        button_frame = tk.Frame(self.tab3)
        button_frame.pack(pady=10)
        
        # Кнопка очистки текста
        clear_button = tk.Button(button_frame, text="Очистить", 
                                 command=self.clear_text, font=("Arial", 10),
                                 padx=15, pady=5)
        clear_button.grid(row=0, column=0, padx=10)
        
        # Кнопка сохранения текста
        save_button = tk.Button(button_frame, text="Сохранить как...", 
                                command=self.save_text, font=("Arial", 10),
                                padx=15, pady=5)
        save_button.grid(row=0, column=1, padx=10)
        
        # Информационная метка
        self.file_label = tk.Label(self.tab3, text="Файл не загружен", 
                                   font=("Arial", 10), fg="gray")
        self.file_label.pack(pady=5)
    
    def create_menu(self):
        """Создание меню приложения"""
        menubar = tk.Menu(self)
        
        # Меню "Файл"
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Загрузить текст из файла", 
                              command=self.load_text_file, accelerator="Ctrl+O")
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.quit)
        
        # Меню "Помощь"
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="О программе", command=self.show_about)
        
        # Добавление меню в строку меню
        menubar.add_cascade(label="Файл", menu=file_menu)
        menubar.add_cascade(label="Помощь", menu=help_menu)
        
        self.config(menu=menubar)
        
        # Привязка горячих клавиш
        self.bind('<Control-o>', lambda e: self.load_text_file())
    
    def load_text_file(self):
        """Загрузка текста из файла"""
        filetypes = (
            ("Текстовые файлы", "*.txt"),
            ("Все файлы", "*.*")
        )
        
        filename = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=filetypes
        )
        
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, content)
                    
                # Обновление метки с именем файла
                self.file_label.config(text=f"Загружен файл: {os.path.basename(filename)}")
                
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {str(e)}")
    
    def save_text(self):
        """Сохранение текста в файл"""
        filetypes = (
            ("Текстовые файлы", "*.txt"),
            ("Все файлы", "*.*")
        )
        
        filename = filedialog.asksaveasfilename(
            title="Сохранить как",
            defaultextension=".txt",
            filetypes=filetypes
        )
        
        if filename:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(content)
                    
                messagebox.showinfo("Успех", f"Файл сохранен: {filename}")
                
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {str(e)}")
    
    def clear_text(self):
        """Очистка текстового поля"""
        self.text_area.delete(1.0, tk.END)
        self.file_label.config(text="Файл не загружен")
    
    def show_about(self):
        """Отображение информации о программе"""
        about_text = """Приложение с графическим интерфейсом
Версия 1.0
        
Функции:
1. Калькулятор для двух чисел
2. Выбор вариантов с помощью чекбоксов
3. Работа с текстом (загрузка, редактирование, сохранение)
        
Разработчик: Иванов Артём Романович"""
        
        messagebox.showinfo("О программе", about_text)

if __name__ == "__main__":
    app = Application()
    app.mainloop()