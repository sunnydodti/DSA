public class BinarySearch {
    public static void main(String[] args) {
        int[] input = { 0, 2, 3, 6, 7, 9 };
        int key = 9;
        print(input, "Input array:");
        System.out.println("key: " + key);
        System.out.println("binarySearch: " + binarySearch(input.clone(), key));

        key = 0;
        System.out.println("key: " + key);
        System.out.println("binarySearch: " + binarySearch(input.clone(), key));

        key = 10;
        System.out.println("key: " + key);
        System.out.println("binarySearch: " + binarySearch(input.clone(), key));

    }

    public static int binarySearch(int[] elements, int key) {
        int left = 0;
        int right = elements.length - 1;
        int middle;
        while (left <= right) {
            middle = left + (right - left) / 2;
            if (key == elements[middle])
                return middle;

            if (key < elements[middle]) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
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