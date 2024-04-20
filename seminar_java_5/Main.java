// import java.util.Comparator;
// import java.util.HashMap;
// import java.util.Map;
// import java.util.TreeMap;

// public class MapDemo {
//     public static void main(String[] args) {
//         Map<String, Integer> map = new HashMap<>();
//         map.put("alice", 20);//добавление
//         map.put("bob", 19);
//         map.put("charlie", 25);

//         int a = map.get("bob");//получение

//         boolean bool = map.containsKey("bob");
//         System.out.println("присутсвует ли боб: " + bool);
//         map.remove("alice");
//         System.out.println(map);

//         for (Map.Entry<String, Integer> entry : map.entrySet()) {
//             System.out.println("name " + entry.getKey() + "  age is "
//                     + entry.getValue());
//         }
//         System.out.println("///////////////");
//         System.out.println(map.getOrDefault("bob", 4210));
//         System.out.println(map.get("alice"));

//         TreeMap<String, Integer> treeMap = new TreeMap<>();
//         treeMap.put("zoey", 30);
//         treeMap.put("peter", 26);
//         treeMap.put("alice", 20);
//         System.out.println(treeMap);

//     }
// }

// Создать структуру для хранения Номеров паспортов и Фамилий сотрудников организации.

// 123456 Иванов

// 321456 Васильев

// 234561 Петрова

// 234432 Иванов

// 654321 Петрова

// 345678 Иванов

// Вывести данные по сотрудникам с фамилией Иванов.
import java.util.HashMap;
import java.util.Map;

package seminar_java_5;

public class Main {
    public static void main(String[] args)
//     Map<Integer, String> map = HashMap.newHashMap();

//     map.put(key:123456, value:"Иванов")
//     map.put(key:321456, value:"Васильев")
//     map.put(key:234561, value:"Петрова")
//     map.put(key:234432, value:"Иванов")
//     map.put(key:654321, value:"Петрова")
//     map.put(key:345678, value:"Иванов")

//     for (Map.Entry<Integer, String> entry: map.entrySet()) {
//         System.out.println("name" + entry.getKey() + " age is " + entry.getValue(););
//     }
// }


// public static Map<Integer, String> getDateBySurname(Map<Integer, String> date, String surname) {
//     Map<Integer, String> response = new HashMap<>();
//     for (Map.Entry<Integer, String> entry : date.entrySet()) {
//         if (surname.equals(entry.getValue())) {
//             response.put(entry.getKey(), entry.getValue());
//         }
//     }
//     return response;
// }

// Напишите программу, которая считывает текст из файла и подсчитывает, сколько раз каждое слово встречается в тексте. Используйте HashMap для хранения слов и их частоты.

/**
    Map<String, Integer> repeat = new HashMap<>();
    for (String s : stringList) {
        System.out.println("s= " + s);
        if (s != null && !s.isEmpty()) {
            if (repeat.get(s) == null) {
                repeat.put(s, 1);
            } else {
                int count = repeat.get(s);
                repeat.put(s, ++count);
            }
        }
    }
    return repeat;
}
*/


/**
public class WordCounter {
    public static void main(String[] args) {
        // Путь к файлу с текстом
        String filePath = "Lorem_ipsum.txt";

        // Создаем HashMap для хранения слов и их частот
        Map<String, Integer> wordCount = new HashMap<>();

        // Читаем текст из файла
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                // Разбиваем текст на слова
                String[] words = line.split("\\s+");
                for (String word : words) {
                    // Удаляем знаки препинания и переводим в нижний регистр
                    word = word.replaceAll("[^a-zA-Zа-яА-Я]", "").toLowerCase();
                    // Если слово уже есть в HashMap, увеличиваем его частоту
                    if (wordCount.containsKey(word)) {
                        wordCount.put(word, wordCount.get(word) + 1);
                    } else {
                        // Иначе добавляем новое слово со значением 1
                        wordCount.put(word, 1);
                    }
                }
            }
        } catch (IOException e) {
            System.err.println("Ошибка при чтении файла: " + e.getMessage());
        }

        // Выводим результаты
        System.out.println("Статистика по словам:");
        for (Map.Entry<String, Integer> entry : wordCount.entrySet()) {
            System.out.printf("%s - %d раз(а)%n", entry.getKey(), entry.getValue());
        }
    }
}
*/
/**
List<String> lines = null;
        try {
            lines = Files.readAllLines(new File("input.txt").toPath(), StandardCharsets.UTF_8);
        } catch (IOException e) {
            e.printStackTrace();
        }
        StringBuilder textBuilder = new StringBuilder();
        for (String line : lines) {
            textBuilder.append(line).append(" ");
        }
        String text = textBuilder.toString();
        System.out.println("Len Text: " + text.length());
        // Разделяем текст на слова
        String[] words = text.split("\\s+");
        List<String> stringList = Arrays.asList(words);
        System.out.println("String List" + stringList);
        System.out.printf("Повторы: %s\n", getRepeatText(stringList));

*/

/**
Создайте программу для хранения реестра контактов. Используйте HashMap, где ключами будут имена контактов, а значениями - их номера телефонов. Реализуйте добавление новых контактов, поиск по имени и удаление контактов.
*/

HashMap<String, String> map = new HashMap<>();

Boolean flag = true;
Scanner scanner = new Scanner(System.in);
while(flag){
    System.out.println("Укажете действие");
    String action = scanner.next(); 

    if (action.equals("1")){
        System.out.println("Укажете имя контакта");
        String contName = scanner.next(); 
        System.out.println("Укажете номер телефона");
        String numPhone = scanner.next();
        map.put(contName, numPhone);


    }else if(action.equals("2")){
        System.out.println("Укажете имя контакта");
        String searchName = scanner.next(); 
        System.out.println(map.getOrDefault(searchName, "Нет контакта"));
    }else if(action.equals("3")){
        System.out.println("Укажете имя контакта");
        String delName = scanner.next();
        System.out.println("Удаление контакта: " + map.remove(delName));
    }else if(action.equals("4")){
        flag = false;
          
    }else{
        break;
    }

}