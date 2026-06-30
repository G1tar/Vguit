public class Main {
    public static void main(String[] args) {
        System.out.println("=== Параллельное выполнение задач ===");
        System.out.println("Главный поток: " + Thread.currentThread().getName());
        System.out.println("Запуск потоков...");
        System.out.println("=".repeat(50));
        System.out.println();

        // 3. Создаем и запускаем обе задачи в отдельных потоках
        Thread numberThread = new Thread(new NumberTask(), "NumberThread");
        Thread letterThread = new Thread(new LetterTask(), "LetterThread");

        // Запускаем потоки
        numberThread.start();
        letterThread.start();

        // Демонстрация состояния потоков
        System.out.println("Статус потоков после запуска:");
        System.out.println("NumberThread: " + numberThread.getState());
        System.out.println("LetterThread: " + letterThread.getState());
        System.out.println();

        // Ожидаем завершения потоков
        try {
            numberThread.join();
            letterThread.join();
        } catch (InterruptedException e) {
            System.err.println("Главный поток был прерван: " + e.getMessage());
        }

        System.out.println();
        System.out.println("=".repeat(50));
        System.out.println("Все задачи завершены!");
    }
}

// 1. Класс NumberTask - выводит числа от 1 до 5 с задержкой 500 мс

class NumberTask implements Runnable {
    @Override
    public void run() {
        String threadName = Thread.currentThread().getName();
        System.out.println("[Номерной поток] " + threadName + " - запущен");

        try {
            for (int i = 1; i <= 5; i++) {
                System.out.println("[ЧИСЛО] " + i + " (поток: " + threadName + ")");
                Thread.sleep(500); // Задержка 500 мс
            }
        } catch (InterruptedException e) {
            System.err.println("[Номерной поток] Был прерван!");
            Thread.currentThread().interrupt();
        }

        System.out.println("[Номерной поток] " + threadName + " - завершен");
    }
}

// 2. Класс LetterTask - выводит буквы от 'A' до 'E' с задержкой 700 мс

class LetterTask implements Runnable {
    @Override
    public void run() {
        String threadName = Thread.currentThread().getName();
        System.out.println("[Буквенный поток] " + threadName + " - запущен");

        try {
            for (char c = 'A'; c <= 'E'; c++) {
                System.out.println("[БУКВА] " + c + " (поток: " + threadName + ")");
                Thread.sleep(700); // Задержка 700 мс
            }
        } catch (InterruptedException e) {
            System.err.println("[Буквенный поток] Был прерван!");
            Thread.currentThread().interrupt();
        }

        System.out.println("[Буквенный поток] " + threadName + " - завершен");
    }
}