import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=".repeat(60));
        System.out.println("ЖУРНАЛ УСПЕВАЕМОСТИ");
        System.out.println("=".repeat(60));
        System.out.println();

        // 1. Создаем коллекцию HashMap<String, Integer>
        Map<String, Integer> journal = new HashMap<>();

        // 2. Заполняем журнал данными пяти студентов
        addStudents(journal);

        // Выводим весь журнал
        printJournal(journal);

        System.out.println("=".repeat(60));
        System.out.println();

        // 3. Выводим оценку конкретного студента
        demonstrateGetOperation(journal, scanner);

        System.out.println();
        System.out.println("=".repeat(60));
        System.out.println();

        // 4. Проверяем наличие студента
        demonstrateContainsKeyOperation(journal, scanner);

        System.out.println();
        System.out.println("=".repeat(60));
        System.out.println();

        // 5. Удаляем студента и выводим обновленный список
        demonstrateRemoveOperation(journal, scanner);

        scanner.close();
    }


     // 2. Заполняет журнал данными студентов

    private static void addStudents(Map<String, Integer> journal) {
        System.out.println(" Добавление студентов в журнал:");
        System.out.println("-".repeat(40));

        // Используем метод put() для добавления студентов
        journal.put("Анна Иванова", 95);
        journal.put("Петр Петров", 78);
        journal.put("Мария Сидорова", 88);
        journal.put("Иван Смирнов", 92);
        journal.put("Елена Козлова", 85);

        System.out.println(" Добавлено 5 студентов:");
        for (Map.Entry<String, Integer> entry : journal.entrySet()) {
            System.out.printf("  • %-15s : %d баллов%n", entry.getKey(), entry.getValue());
        }
        System.out.println();
    }


    // Выводит весь журнал в виде таблицы

    private static void printJournal(Map<String, Integer> journal) {
        System.out.println("ТЕКУЩИЙ ЖУРНАЛ");
        System.out.println("-".repeat(40));
        System.out.println("Количество студентов: " + journal.size());
        System.out.println();

        if (journal.isEmpty()) {
            System.out.println("Журнал пуст!");
            return;
        }

        System.out.println("┌──────────────────────────┬──────────┬─────────┐");
        System.out.println("│ Имя студента             │ Балл     │ Оценка  │");
        System.out.println("├──────────────────────────┼──────────┼─────────┤");

        // Сортируем по имени для удобства
        journal.entrySet().stream()
                .sorted(Map.Entry.comparingByKey())
                .forEach(entry -> {
                    String name = entry.getKey();
                    int score = entry.getValue();
                    String grade = getGrade(score);
                    System.out.printf("│ %-24s │ %-8d │ %-7s │\n", name, score, grade);
                });

        System.out.println("└──────────────────────────┴──────────┴─────────┘");
        System.out.println();

        // Дополнительная статистика
        printStatistics(journal);
    }


    // Определяет оценку по 5-балльной шкале

    private static String getGrade(int score) {
        if (score >= 90) return "Отлично";
        if (score >= 75) return "Хорошо";
        if (score >= 60) return "Удовл.";
        return "Неудовл.";
    }


    // Выводит статистику по журналу

    private static void printStatistics(Map<String, Integer> journal) {
        if (journal.isEmpty()) return;

        int sum = journal.values().stream().mapToInt(Integer::intValue).sum();
        double average = (double) sum / journal.size();
        int max = journal.values().stream().max(Integer::compareTo).orElse(0);
        int min = journal.values().stream().min(Integer::compareTo).orElse(0);

        System.out.println(" Статистика:");
        System.out.printf("  • Средний балл: %.2f%n", average);
        System.out.printf("  • Максимальный балл: %d%n", max);
        System.out.printf("  • Минимальный балл: %d%n", min);
        System.out.println();
    }


    // 3. Демонстрирует метод get() - получение оценки по имени
    private static void demonstrateGetOperation(Map<String, Integer> journal, Scanner scanner) {
        System.out.println(" ПОИСК ОЦЕНКИ СТУДЕНТА");
        System.out.println("-".repeat(40));

        // Вариант 1: Предопределенный поиск
        String predefinedName = "Анна Иванова";
        System.out.println("Пример 1 (предопределенный):");
        System.out.println("  Поиск студента: " + predefinedName);

        Integer score = journal.get(predefinedName);
        if (score != null) {
            System.out.println(" Оценка: " + score + " баллов (" + getGrade(score) + ")");
        } else {
            System.out.println(" Студент не найден в журнале");
        }
        System.out.println();

        // Вариант 2: Поиск по вводу пользователя
        System.out.println("Пример 2 (интерактивный):");
        System.out.print("  Введите имя студента для поиска оценки: ");
        String inputName = scanner.nextLine().trim();

        // Проверяем, есть ли такой студент
        if (journal.containsKey(inputName)) {
            int studentScore = journal.get(inputName);
            System.out.printf(" Студент '%s' имеет оценку: %d баллов (%s)%n",
                    inputName, studentScore, getGrade(studentScore));
        } else {
            System.out.println(" Студент '" + inputName + "' не найден в журнале");
            System.out.println(" Совет: Проверьте правильность написания имени");
        }
    }


    // 4. Демонстрирует метод containsKey() - проверка наличия студента

    private static void demonstrateContainsKeyOperation(Map<String, Integer> journal, Scanner scanner) {
        System.out.println("ПРОВЕРКА НАЛИЧИЯ СТУДЕНТА");
        System.out.println("-".repeat(40));

        // Вариант 1: Предопределенная проверка
        String predefinedName = "Иван";
        System.out.println("Пример 1 (предопределенный):");
        System.out.println("  Проверка студента: " + predefinedName);

        boolean contains = journal.containsKey(predefinedName);
        System.out.println("  Результат: " + (contains ? "Есть в журнале" : "Нет в журнале"));

        // Дополнительная информация
        if (contains) {
            System.out.println("  Оценка: " + journal.get(predefinedName) + " баллов");
        }
        System.out.println();

        // Вариант 2: Интерактивная проверка
        System.out.println("Пример 2 (интерактивный):");
        System.out.print("  Введите имя студента для проверки: ");
        String inputName = scanner.nextLine().trim();

        if (journal.containsKey(inputName)) {
            System.out.println(" Студент '" + inputName + "' присутствует в журнале");
            System.out.println(" Oценка: " + journal.get(inputName) + " баллов");
        } else {
            System.out.println(" Студент '" + inputName + "' отсутствует в журнале");

            // Предлагаем похожие имена
            findSimilarNames(journal, inputName);
        }
    }


    // Ищет похожие имена в журнале
    private static void findSimilarNames(Map<String, Integer> journal, String inputName) {
        System.out.println("\n  Возможно, вы искали:");
        boolean found = false;
        for (String name : journal.keySet()) {
            if (name.toLowerCase().contains(inputName.toLowerCase()) ||
                    inputName.toLowerCase().contains(name.toLowerCase())) {
                System.out.println("    • " + name);
                found = true;
            }
        }
        if (!found) {
            System.out.println("    • Похожих имен не найдено");
        }
    }


    // 5. Демонстрирует метод remove() - удаление студента

    private static void demonstrateRemoveOperation(Map<String, Integer> journal, Scanner scanner) {
        System.out.println("УДАЛЕНИЕ СТУДЕНТА");
        System.out.println("-".repeat(40));

        // Показываем текущий список
        System.out.println("Текущий журнал (" + journal.size() + " студентов):");
        journal.entrySet().stream()
                .sorted(Map.Entry.comparingByKey())
                .forEach(entry -> System.out.printf("  • %s : %d%n", entry.getKey(), entry.getValue()));
        System.out.println();

        // Удаляем одного студента (заранее определенного)
        String studentToRemove = "Мария Сидорова";
        System.out.println("Удаление студента: " + studentToRemove);

        Integer removedScore = journal.remove(studentToRemove);

        if (removedScore != null) {
            System.out.println(" Студент '" + studentToRemove + "' удален (оценка: " + removedScore + ")");
        } else {
            System.out.println(" Студент '" + studentToRemove + "' не найден");
        }
        System.out.println();

        // Выводим обновленный список
        System.out.println("ОБНОВЛЕННЫЙ ЖУРНАЛ (" + journal.size() + " студентов):");
        System.out.println("-".repeat(40));

        if (journal.isEmpty()) {
            System.out.println("Журнал пуст!");
        } else {
            System.out.println("┌──────────────────────────┬──────────┬─────────┐");
            System.out.println("│ Имя студента             │ Балл     │ Оценка  │");
            System.out.println("├──────────────────────────┼──────────┼─────────┤");

            journal.entrySet().stream()
                    .sorted(Map.Entry.comparingByKey())
                    .forEach(entry -> {
                        String name = entry.getKey();
                        int score = entry.getValue();
                        String grade = getGrade(score);
                        System.out.printf("│ %-24s │ %-8d │ %-7s │\n", name, score, grade);
                    });

            System.out.println("└──────────────────────────┴──────────┴─────────┘");
        }
    }
}