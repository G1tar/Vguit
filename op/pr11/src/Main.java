import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {

        List<Integer> numbers = Arrays.asList(1, -2, 3, -4, 5);

        // Обработка с помощью Stream API
        List<Integer> result = numbers.stream()
                .filter(n -> n > 0)           // Фильтруем только положительные числа
                .map(n -> n * n)              // Возводим их в квадрат
                .collect(Collectors.toList());       // Собираем результат в новый список


        System.out.println("Исходный список: " + numbers);
        System.out.println("Результирующий список (положительные числа в квадрате): " + result);
    }
}