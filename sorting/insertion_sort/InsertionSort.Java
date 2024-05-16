public class InsertionSort {
    public static void main(String[] args) {
        int[] input = { 1, 3, 5, 0, 8, 4, 2 };
        print(input);
        print(insertionSort(input.clone()), "insertionSort");
    }

    static int[] insertionSort(int[] elements) {
        for (int i = 1; i < elements.length; i++) {
            int current = elements[i];
            int j = i - 1;
            while (j >= 0 && current < elements[j]) {
                elements[j + 1] = elements[j];
                j--;
            }
            elements[j + 1] = current;

        }
        return elements;
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