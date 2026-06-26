import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;

public class Main {

    // Русский алфавит (строчные буквы)
    private static final String ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя";
    private static final int ALPHABET_SIZE = ALPHABET.length();

    public static void main(String[] args) throws Exception {
        // 1. Скачиваем эталонный текст
        String referenceText = downloadText(10000);
        if (referenceText == null || referenceText.isEmpty()) {
            System.out.println("Не удалось загрузить эталонный текст.");
            return;
        }
        Map<Character, Double> referenceFreq = buildFrequencyProfile(referenceText);

        // 3. Вводим зашифрованный текст (для примера)
        String encrypted = "хжуюфсш ььуфв"; // замените на свой
        System.out.println("Зашифрованный текст: " + encrypted);

        // 4. Расшифровываем
        String decrypted = decryptCaesar(encrypted, referenceFreq);
        System.out.println("Расшифрованный текст: " + decrypted);
    }

    private static String downloadText(int length) throws Exception {
        URL url = new URL("https://fish-text.ru/api/get?format=text&number=" + length);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        conn.setConnectTimeout(5000);
        conn.setReadTimeout(5000);

        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(conn.getInputStream(), "UTF-8"))) {
            StringBuilder result = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                result.append(line).append("\n");
            }
            // Обрезаем до нужной длины (или чуть больше)
            String full = result.toString();
            return full.length() > length ? full.substring(0, length) : full;
        }
    }

    private static Map<Character, Double> buildFrequencyProfile(String text) {
        Map<Character, Integer> counts = new HashMap<>();
        // Инициализируем нулями
        for (char c : ALPHABET.toCharArray()) {
            counts.put(c, 0);
        }

        int totalLetters = 0;
        for (char c : text.toLowerCase().toCharArray()) {
            if (counts.containsKey(c)) {
                counts.put(c, counts.get(c) + 1);
                totalLetters++;
            }
        }

        // Преобразуем в частоты
        Map<Character, Double> frequencies = new HashMap<>();
        if (totalLetters == 0) return frequencies;
        for (Map.Entry<Character, Integer> entry : counts.entrySet()) {
            frequencies.put(entry.getKey(), (double) entry.getValue() / totalLetters);
        }
        return frequencies;
    }

    private static String decryptCaesar(String encrypted, Map<Character, Double> referenceFreq) {
        String bestText = null;
        double bestScore = Double.NEGATIVE_INFINITY;
        int bestShift = 0;

        for (int shift = 0; shift < ALPHABET_SIZE; shift++) {
            String candidate = shiftText(encrypted, -shift);
            Map<Character, Double> candidateFreq = buildFrequencyProfile(candidate);
            double score = compareFrequencies(referenceFreq, candidateFreq);
            if (score > bestScore) {
                bestScore = score;
                bestShift = shift;
                bestText = candidate;
            }
        }

        System.out.println("Подобранный сдвиг: " + bestShift + " (ключ " + ALPHABET.charAt(bestShift) + ")");
        return bestText;
    }

    // Сдвигает текст на заданное количество позиций (отрицательное значение для расшифровки)

    private static String shiftText(String text, int shift) {
        StringBuilder result = new StringBuilder();
        shift = ((shift % ALPHABET_SIZE) + ALPHABET_SIZE) % ALPHABET_SIZE;

        for (char c : text.toCharArray()) {
            char lower = Character.toLowerCase(c);
            int index = ALPHABET.indexOf(lower);
            if (index != -1) {
                int newIndex = (index + shift) % ALPHABET_SIZE;
                char newChar = ALPHABET.charAt(newIndex);
                result.append(Character.isUpperCase(c) ? Character.toUpperCase(newChar) : newChar);
            } else {
                result.append(c); // не буква — оставляем
            }
        }
        return result.toString();
    }


    private static double compareFrequencies(Map<Character, Double> f1, Map<Character, Double> f2) {
        double dotProduct = 0.0;
        for (char c : ALPHABET.toCharArray()) {
            double v1 = f1.getOrDefault(c, 0.0);
            double v2 = f2.getOrDefault(c, 0.0);
            dotProduct += v1 * v2;
        }
        return dotProduct; // максимум при совпадении профилей
    }
}