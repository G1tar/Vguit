import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите строку: ");
        String input = scanner.nextLine();
        
        String result = convertCase(input);
        System.out.println("Результат: " + result);
        
        scanner.close();
    }
    
    public static String convertCase(String str) {
        if (str == null || str.isEmpty()) {
            return str;
        }
        
        int uppercaseCount = 0;
        int lowercaseCount = 0;
        
        // Подсчет заглавных и строчных букв
        for (char c : str.toCharArray()) {
            if (Character.isUpperCase(c)) {
                uppercaseCount++;
            } else if (Character.isLowerCase(c)) {
                lowercaseCount++;
            }
        }
        
        // Преобразование строки
        if (uppercaseCount > lowercaseCount) {
            return str.toUpperCase();
        } else {
            // Если заглавных меньше или равно строчным - преобразуем к строчным
            return str.toLowerCase();
        }
    }
}