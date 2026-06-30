import java.util.InputMismatchException;
import java.util.Scanner;

void main(String[] args) {

    Scanner scanner = null;
    try {

        scanner = new Scanner(System.in);

        IO.println(String.format("Введите первое число:"));
        int a = scanner.nextInt();
        IO.println(String.format("Введите второе число:"));
        int b = scanner.nextInt();

        int result = a / b;
        IO.println(String.format("Результат деления: " + result));
    } catch (InputMismatchException e) {
        IO.println(String.format("Ошибка: введено не число"));
    } catch (ArithmeticException e) {
        IO.println(String.format("Ошибка: деление на ноль"));
    } finally {
        IO.println(String.format("Завершение программы"));
        scanner.close();
    }
}