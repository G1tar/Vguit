import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;

public class Main {
    public static void main(String[] args) {
        // 1. Получаем текущую дату
        LocalDate currentDate = LocalDate.now();

        // 2. Создаем дату рождения (15 марта 1995 года)
        LocalDate birthDate = LocalDate.of(1995, 3, 15);

        // 3. Рассчитываем возраст человека в годах
        Period age = Period.between(birthDate, currentDate);
        int years = age.getYears();

        // 4. Определяем, сколько дней осталось до следующего дня рождения
        LocalDate nextBirthday = getNextBirthday(birthDate, currentDate);
        long daysUntilNextBirthday = java.time.temporal.ChronoUnit.DAYS.between(currentDate, nextBirthday);

        // 5. Выводим все данные в формате dd.MM.yyyy
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd.MM.yyyy");

        System.out.println("=== Анализ даты рождения ===");
        System.out.println("Текущая дата:          " + currentDate.format(formatter));
        System.out.println("Дата рождения:         " + birthDate.format(formatter));
        System.out.println("Возраст:               " + years + " лет");
        System.out.println("Следующий день рождения: " + nextBirthday.format(formatter));
        System.out.println("Дней до дня рождения:  " + daysUntilNextBirthday);

        // Дополнительная информация
        printAdditionalInfo(birthDate, currentDate, age);
    }

    // Вычисляет дату следующего дня рождения

    private static LocalDate getNextBirthday(LocalDate birthDate, LocalDate currentDate) {
        LocalDate thisYearBirthday = birthDate.withYear(currentDate.getYear());

        // Если день рождения в этом году уже прошел, берем следующий год
        if (thisYearBirthday.isBefore(currentDate) || thisYearBirthday.isEqual(currentDate)) {
            return thisYearBirthday.plusYears(1);
        } else {
            return thisYearBirthday;
        }
    }

    // Выводит дополнительную информацию

    private static void printAdditionalInfo(LocalDate birthDate, LocalDate currentDate, Period age) {
        System.out.println("\n=== Дополнительная информация ===");

        // Детали возраста
        System.out.println("Возраст (полный): " + age.getYears() + " лет, " +
                age.getMonths() + " месяцев, " + age.getDays() + " дней");

        // День недели рождения
        String dayOfWeek = birthDate.getDayOfWeek().getDisplayName(
                java.time.format.TextStyle.FULL, java.util.Locale.forLanguageTag("ru"));
        System.out.println("День недели рождения: " + dayOfWeek);

        // Знак зодиака
        String zodiacSign = getZodiacSign(birthDate);
        System.out.println("Знак зодиака: " + zodiacSign);

        // Время до следующего дня рождения в месяцах и днях
        LocalDate nextBirthday = getNextBirthday(birthDate, currentDate);
        Period untilNext = Period.between(currentDate, nextBirthday);
        System.out.println("До следующего дня рождения: " +
                untilNext.getMonths() + " месяцев, " + untilNext.getDays() + " дней");

        // Проверка, является ли сегодня днем рождения
        if (isBirthdayToday(birthDate, currentDate)) {
            System.out.println("🎉 СЕГОДНЯ ДЕНЬ РОЖДЕНИЯ! Поздравляем! 🎉");
        }
    }

    // Определяет знак зодиака по дате рождения

    private static String getZodiacSign(LocalDate date) {
        int day = date.getDayOfMonth();
        int month = date.getMonthValue();

        if ((month == 3 && day >= 21) || (month == 4 && day <= 19)) return "Овен";
        if ((month == 4 && day >= 20) || (month == 5 && day <= 20)) return "Телец";
        if ((month == 5 && day >= 21) || (month == 6 && day <= 20)) return "Близнецы";
        if ((month == 6 && day >= 21) || (month == 7 && day <= 22)) return "Рак";
        if ((month == 7 && day >= 23) || (month == 8 && day <= 22)) return "Лев";
        if ((month == 8 && day >= 23) || (month == 9 && day <= 22)) return "Дева";
        if ((month == 9 && day >= 23) || (month == 10 && day <= 22)) return "Весы";
        if ((month == 10 && day >= 23) || (month == 11 && day <= 21)) return "Скорпион";
        if ((month == 11 && day >= 22) || (month == 12 && day <= 21)) return "Стрелец";
        if ((month == 12 && day >= 22) || (month == 1 && day <= 19)) return "Козерог";
        if ((month == 1 && day >= 20) || (month == 2 && day <= 18)) return "Водолей";
        return "Рыбы";
    }

    // Проверяет, является ли сегодня днем рождения

    private static boolean isBirthdayToday(LocalDate birthDate, LocalDate currentDate) {
        return birthDate.getMonth() == currentDate.getMonth() &&
                birthDate.getDayOfMonth() == currentDate.getDayOfMonth();
    }
}
