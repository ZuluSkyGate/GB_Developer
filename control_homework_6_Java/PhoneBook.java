// Реализуйте структуру телефонной книги с помощью HashMap.
// Программа также должна учитывать, что в во входной структуре будут повторяющиеся имена с разными телефонами,
// их необходимо считать, как одного человека с разными телефонами. Вывод должен быть отсортирован по убыванию числа телефонов.

import java.util.*;
package homework_lesson_6_java;

public class PhoneBook {
    public static void main(String[] args) {
        // Создание HashMap для хранения телефонной книги
        Map<String, Set<String>> phoneBook = new HashMap<>();

        // Пример данных телефонной книги 
        String[][] entries = {
                {"Иванов", "111-111"},
                {"Петров", "222-222"},
                {"Сидоров", "333-333"},
                {"Иванов", "444-444"},
                {"Петров", "555-555"}
        };

        // Заполнение телефонной книги
        for (String[] entry : entries) {
            String name = entry[0];
            String phoneNumber = entry[1];
            
            // Проверка, есть ли уже такое имя в книге
            if (!phoneBook.containsKey(name)) {
                phoneBook.put(name, new HashSet<>());
            }
            
            // Добавление номера телефона к соответствующему имени
            phoneBook.get(name).add(phoneNumber);
        }

        // Создание списка для сортировки по числу телефонов
        List<Map.Entry<String, Set<String>>> sortedEntries = new ArrayList<>(phoneBook.entrySet());

        // Сортировка списка по убыванию числа телефонов
        sortedEntries.sort((entry1, entry2) -> Integer.compare(entry2.getValue().size(), entry1.getValue().size()));

        // Вывод отсортированной телефонной книги
        for (Map.Entry<String, Set<String>> entry : sortedEntries) {
            String name = entry.getKey();
            Set<String> phoneNumbers = entry.getValue();
            System.out.println(name + ": " + phoneNumbers);
        }
    }

    @Override
    public String toString() {
        return "PhoneBook []";
    }
}    

