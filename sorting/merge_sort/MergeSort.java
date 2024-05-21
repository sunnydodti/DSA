import java.util.Arrays;

public class MergeSort {
    public static void main(String[] args) {
        int[] input = { 1, 3, 5, 0, 8, 4, 2 };
        print(input);
        print(mergeSort(input.clone()), "mergeSort");
    }

    static int[] mergeSort(int[] elements) {

        mergeSortRecursive(elements, 0, elements.length);

        return elements;
    }

    static void mergeSortRecursive(int[] elements, int start, int end) {
        if (start >= end - 1)
            return;
        int middle = start + (end - start) / 2;
        mergeSortRecursive(elements, start, middle);
        mergeSortRecursive(elements, middle, end);
        merge(elements, start, middle, end);
    }

    static void merge(int[] elements, int start, int middle, int end) {
        int[] leftArray = Arrays.copyOfRange(elements, start, middle);
        int[] rightArray = Arrays.copyOfRange(elements, middle, end);

        int leftSize = leftArray.length;
        int rightSize = rightArray.length;

        int left_i = 0;
        int right_i = 0;
        int merged_i = start;

        while (left_i < leftSize && right_i < rightSize) {
            if (leftArray[left_i] < rightArray[right_i]) {
                elements[merged_i] = leftArray[left_i];
                left_i++;
            } else {
                elements[merged_i] = rightArray[right_i];
                right_i++;
            }
            merged_i++;
        }

        while (left_i < leftSize) {
            elements[merged_i] = leftArray[left_i];
            left_i++;
            merged_i++;
        }
        while (right_i < rightSize) {
            elements[merged_i] = rightArray[right_i];
            right_i++;
            merged_i++;
        }
    }

    private static void print(int[] array, String text) {
        System.out.print(text + " ");
        for (int num : array) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    private static void print(int[] array) {
        for (int num : array) {
            System.out.print(num + " ");
        }
        System.out.println();

    }
}