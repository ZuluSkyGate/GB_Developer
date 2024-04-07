/*
 Задание №3
Дан массив nums = [3,2,2,3] и число val = 3.
Если в массиве есть числа, равные заданному, нужно перенести
эти элементы в конец массива.
Таким образом, первые несколько (или все) элементов массива
должны быть отличны от заданного, а остальные - равны ему.
 */
import java.util.Arrays;

public class MoveValToEnd {

    public static void moveValToEnd(int[] nums, int val) {
        int begin = 0;
        int end = nums.length - 1;

        while (begin < end) {
            if (nums[begin] == val) {
                swap(nums, begin, end);
                end--;
            } else {
                begin++;
            }
        }
    }

    private static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public static void main(String[] args) {
        int[] nums = {3, 2, 2, 3};
        int val = 3;
        moveValToEnd(nums, val);
        System.out.println(Arrays.toString(nums));
    }
}