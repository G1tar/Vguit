// Студет зит-353 Иванов Артем. Зачетная книжка № 257475
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        //Считываем число
        System.out.print("Введите число: ");
        int number = scanner.nextInt();

        // Находим квадратный корень
        double sqrt = Math.sqrt(number);

        // Округляем вниз и вверх
        int floor = (int) Math.floor(sqrt);
        int ceil = (int) Math.ceil(sqrt);

        // Вычисляем квадраты
        int floorSquare = floor * floor;
        int ceilSquare = ceil * ceil;

        // Определяем, какой квадрат ближе
        int closestSquare;
        int closestRoot;

        if (Math.abs(number - floorSquare) <= Math.abs(number - ceilSquare)) {
            closestSquare = floorSquare;
            closestRoot = floor;
        } else {
            closestSquare = ceilSquare;
            closestRoot = ceil;
        }

        System.out.println("Ближайший квадрат: " + closestSquare);
        System.out.println("Корень числа: " + closestRoot);
    }
}
