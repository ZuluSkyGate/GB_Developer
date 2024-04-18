import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        String s1 = "hello";

        String s2 = new String("hello");

        String s3 = s1;

        String s4 = "h" + "e" + "l" + "l" + "o";

        String s5 = new String("hello");

        String s6 = new String(new char[]{'h', 'e', 'l', 'l', 'o'});

        System.out.println(s1 == s2);
        System.out.println(s1 == s3);
        System.out.println(s1 == s4);
        System.out.println(s1 == s5);
        System.out.println(s1 == s6);
        System.out.println("//////////////");
        System.out.println(s1.equals(s2));
        System.out.println(s1.equals(s3));
        System.out.println(s1.equals(s4));
        System.out.println(s1.equals(s5));
        System.out.println(s1.equals(s6));
        Object[] objects = {"fjkaj", 490, true};
        Object object = new Object();
        object = "8";
        System.out.println(object);
        Random random = new Random();
        for (int i = 0; i < 100; i++) {
            System.out.println(random.nextInt(0,5));
        }


        ArrayList<String> arrayList = new ArrayList<>();


        arrayList.add("true");
        arrayList.add("Hello");
        arrayList.add("hjkhg");
        arrayList.remove(0);
        arrayList.remove("true");
        Collections.sort(arrayList);


    }
}