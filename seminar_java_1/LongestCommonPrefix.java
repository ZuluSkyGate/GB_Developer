/*
 Задание №4
Напишите метод, который находит самую длинную строку общего
префикса среди массива строк.
Если общего префикса нет, вернуть пустую строку "".
 */
public class LongestCommonPrefix {

    public static void main(String[] args) {
        String[] test1 = {"flower", "flow", "flight"};
        String[] test2 = {"dog", "racecar", "car"};
        final String[] test3 = {"ab", "abc", "abcd"};
        String[] test4 = {"a"};
        String[] test5 = {};

        System.out.println(findLongestCommonPrefix(test1));
        System.out.println(findLongestCommonPrefix(test2));
        System.out.println(findLongestCommonPrefix(test3));
        System.out.println(findLongestCommonPrefix(test4));
        System.out.println(findLongestCommonPrefix(test5));
    }

    public static String findLongestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";

        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++) {
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) return "";
            }
        }

        return prefix;
    }
}

