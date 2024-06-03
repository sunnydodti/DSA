import java.util.Arrays;

public class QuickSort {
    public static void main(String[] args) {
        int[] input = { 1, 3, 5, 0, 8, 4, 2 };
        print(input, "Input array:");
        print(quickSort(input.clone(), 0, input.length - 1), "quickSort:");
    }

    public static int[] quickSort(int[] elements, int start, int end) {
        if (start < end) {
            int pivot = partition(elements, start, end);
            quickSort(elements, start, pivot - 1);
            quickSort(elements, pivot + 1, end);
        }
        return elements;
    }

    private static int partition(int[] elements, int start, int end) {
        int pivot = elements[end];
        int swapIndex = start - 1;
        int temp;
        for (int i = start; i < end; i++) {
            if (elements[i] < pivot) {
                swapIndex++;

                temp = elements[swapIndex];
                elements[swapIndex] = elements[i];
                elements[i] = temp;

            }
        }

        swapIndex++;
        temp = elements[swapIndex];
        elements[swapIndex] = elements[end];
        elements[end] = temp;

        return swapIndex;
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