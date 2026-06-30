import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    private static final String FILE_NAME = "students.txt";

    public static void main(String[] args) {
        // 1. Создаём список имён студентов
        List<String> students = Arrays.asList(
                "Анна Иванова",
                "Пётр Петров",
                "Мария Сидорова",
                "Иван Смирнов",
                "Елена Козлова"
        );

        System.out.println("=== Сохранение списка студентов ===");
        students.forEach(name -> System.out.println("  • " + name));
        System.out.println();

        try {
            // 2. Записываем список в файл
            saveStudentsToFile(students);
            System.out.println("✓ Список успешно сохранён в файл: " + FILE_NAME);
            System.out.println();

            // 3. Читаем файл и выводим имена
            System.out.println("=== Загрузка списка студентов ===");
            List<String> loadedStudents = loadStudentsFromFile();

            if (loadedStudents.isEmpty()) {
                System.out.println("Файл пуст или не содержит данных.");
            } else {
                System.out.println("Загружено студентов: " + loadedStudents.size());
                for (int i = 0; i < loadedStudents.size(); i++) {
                    System.out.println((i + 1) + ". " + loadedStudents.get(i));
                }
            }

        } catch (IOException e) {
            // 4. Обработка IOException
            System.err.println("✗ Ошибка при работе с файлом:");
            System.err.println("  Тип ошибки: " + e.getClass().getSimpleName());
            System.err.println("  Сообщение: " + e.getMessage());

            // Дополнительная диагностика
            if (e.getMessage().contains("Permission denied")) {
                System.err.println("  Решение: Проверьте права доступа к файлу.");
            } else if (e.getMessage().contains("No such file or directory")) {
                System.err.println("  Решение: Файл будет создан автоматически при записи.");
            } else if (e.getMessage().contains("The system cannot find the path specified")) {
                System.err.println("  Решение: Проверьте путь к файлу.");
            }

            e.printStackTrace();
        }
    }

    // Сохраняет список студентов в файл

    public static void saveStudentsToFile(List<String> students) throws IOException {
        // Используем try-with-resources для автоматического закрытия
        try (FileWriter writer = new FileWriter(FILE_NAME)) {
            for (String student : students) {
                if (student != null && !student.trim().isEmpty()) {
                    writer.write(student.trim() + System.lineSeparator());
                }
            }
        }
    }


    // Загружает список студентов из файла

    public static List<String> loadStudentsFromFile() throws IOException {
        List<String> students = new ArrayList<>();

        // Проверяем существование файла
        if (!Files.exists(Paths.get(FILE_NAME))) {
            System.out.println("Файл " + FILE_NAME + " не существует. Будет создан новый.");
            return students; // возвращаем пустой список
        }

        // Читаем файл построчно
        try (BufferedReader reader = new BufferedReader(new FileReader(FILE_NAME))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String trimmedLine = line.trim();
                if (!trimmedLine.isEmpty()) {
                    students.add(trimmedLine);
                }
            }
        }

        return students;
    }
}