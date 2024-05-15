package sorting.bubble_sort;

public class BubbleSort {
    public static void main(String[] args) {
        int[] input = { 1, 3, 5, 0, 8, 4, 2 };
        print(input);
        print(bubbleSort(input.clone()), "bubbleSort");
        print(bubbleSort(input.clone()), "bubbleSortOptimized");

    }

    static int[] bubbleSort(int[] elements) {
        int i, j, temp;
        boolean swapped;

        for (i = 0; i < elements.length; i++) {
            swapped = false;
            for (j = 0; j < elements.length - 1; j++) {
                if (elements[j] > elements[j + 1]) {
                    temp = elements[j];
                    elements[j] = elements[j + 1];
                    elements[j + 1] = temp;
                    swapped = true;
                }
            }

            if (!swapped)
                break;
        }
        return elements;
    }

    static int[] bubbleSortOptimized(int[] elements) {
        int i, j, temp;
        boolean swapped;
        final int length = elements.length;
        for (i = 0; i < length - 1; i++) {
            swapped = false;
            for (j = 0; j < length - 1 - i; j++) {

                if (elements[j] > elements[j + 1]) {
                    temp = elements[j];
                    elements[j] = elements[j + 1];
                    elements[j + 1] = temp;
                }
            }

            if (!swapped)
                break;
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