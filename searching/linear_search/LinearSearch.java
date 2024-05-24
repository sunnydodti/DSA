public class LinearSearch {
    public static void main(String[] args) {
        int[] input = { 4, 3, 9, 0, 3, 6, 5, 8, 5, 3, 5, 7, 8, 4, 2 };
        int key = 2;
        print(input, "input:");
        System.out.println("key: " + key);
        System.out.println("linearSearch: " + linearSearch(input, key));
        System.out.println("linearSearchV2: " + linearSearchV2(input, key));

    }

    static int linearSearch(int[] input, int key) {
        for (int i = 0; i < input.length; i++) {
            if (input[i] == key)
                return i;
        }
        return -1;
    }

    static int linearSearchV2(int[] input, int key) {
        int count = 0;
        for (int number : input) {
            if (number == key)
                return count;
            count++;
        }
        return -1;
    }

    static void print(int[] array, String text) {
        System.out.print(text + " ");
        for (int num : array) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    static void print(int[] array) {
        for (int num : array) {
            System.out.print(num + " ");
        }
        System.out.println();

    }
}