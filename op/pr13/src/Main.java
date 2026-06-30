import java.util.ArrayList;
import java.util.HashSet;
import java.util.HashMap;
import java.util.List;
import java.util.Set;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        // 1. Создаем список (ArrayList) имен студентов с повторяющимся именем
        List<String> studentList = new ArrayList<>();
        studentList.add("Анна Иванова");
        studentList.add("Петр Петров");
        studentList.add("Мария Сидорова");
        studentList.add("Анна Иванова"); // Повторяющееся имя
        studentList.add("Иван Смирнов");

        // 2. Выводим список на экран
        System.out.println("=== 1. Список студентов (ArrayList) ===");
        System.out.println("Количество студентов: " + studentList.size());
        for (int i = 0; i < studentList.size(); i++) {
            System.out.println((i + 1) + ". " + studentList.get(i));
        }
        System.out.println();

        // 3. Передаем все элементы из ArrayList в множество (HashSet)
        Set<String> uniqueStudents = new HashSet<>(studentList);

        System.out.println("=== 2. Множество студентов (HashSet) ===");
        System.out.println("Количество уникальных студентов: " + uniqueStudents.size());
        System.out.println("Дубликаты автоматически удалены!");
        int index = 1;
        for (String student : uniqueStudents) {
            System.out.println(index++ + ". " + student);
        }
        System.out.println();

        // 4. Создаем словарь (HashMap) с оценками
        Map<String, Integer> studentScores = new HashMap<>();

        // 5. Заполняем словарь оценками
        // Используем уникальные имена из множества
        studentScores.put("Анна Иванова", 95);
        studentScores.put("Петр Петров", 78);
        studentScores.put("Мария Сидорова", 88);
        studentScores.put("Иван Смирнов", 92);

        System.out.println("=== 3. Оценки студентов (HashMap) ===");
        System.out.println("Количество записей: " + studentScores.size());
        System.out.println();

        // Выводим результаты в виде таблицы
        printScoreTable(studentScores);
    }

    // Выводит таблицу с оценками студентов

    private static void printScoreTable(Map<String, Integer> scores) {
        System.out.println("┌──────────────────────────┬──────────┐");
        System.out.println("│ Имя студента             │ Балл     │");
        System.out.println("├──────────────────────────┼──────────┤");

        for (Map.Entry<String, Integer> entry : scores.entrySet()) {
            String name = entry.getKey();
            Integer score = entry.getValue();
            System.out.printf("│ %-24s │ %-8d │\n", name, score);
        }

        System.out.println("└──────────────────────────┴──────────┘");
        System.out.println();

        // Дополнительная статистика
        printStatistics(scores);
    }

    // Выводит статистику по оценкам

    private static void printStatistics(Map<String, Integer> scores) {
        System.out.println("=== Статистика ===");

        // Сумма и количество
        int sum = 0;
        int minScore = Integer.MAX_VALUE;
        int maxScore = Integer.MIN_VALUE;
        String minStudent = "";
        String maxStudent = "";

        for (Map.Entry<String, Integer> entry : scores.entrySet()) {
            String name = entry.getKey();
            Integer score = entry.getValue();

            sum += score;

            if (score < minScore) {
                minScore = score;
                minStudent = name;
            }

            if (score > maxScore) {
                maxScore = score;
                maxStudent = name;
            }
        }

        double average = (double) sum / scores.size();

        System.out.printf("Средний балл: %.2f\n", average);
        System.out.printf("Максимальный балл: %d (%s)\n", maxScore, maxStudent);
        System.out.printf("Минимальный балл: %d (%s)\n", minScore, minStudent);

        // Оценка успеваемости
        System.out.println("\nУспеваемость:");
        System.out.println("  Отлично (90-100): " + countByRange(scores, 90, 100));
        System.out.println("  Хорошо (75-89):  " + countByRange(scores, 75, 89));
        System.out.println("  Удовлетворительно (60-74): " + countByRange(scores, 60, 74));
        System.out.println("  Неудовлетворительно (<60): " + countByRange(scores, 0, 59));
    }

    // Подсчитывает количество студентов с баллами в заданном диапазоне

    private static int countByRange(Map<String, Integer> scores, int min, int max) {
        int count = 0;
        for (Integer score : scores.values()) {
            if (score >= min && score <= max) {
                count++;
            }
        }
        return count;
    }
}
