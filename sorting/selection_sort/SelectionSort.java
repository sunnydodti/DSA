class SelectionSort {
    public static void main(String[] args) {
        int[] input = { 1, 3, 5, 0, 8, 4, 2 };
        print(input);
        print(selectionSort(input.clone()), "selectionSort");
    }

    static int[] selectionSort(int[] elements) {
        int i, j, minElementIndex, temp;
        int length = elements.length;
        for (i = 0; i < length - 1; i++) {
            minElementIndex = i;
            for (j = i + 1; j < length; j++) {
                if (elements[j] < elements[minElementIndex]) {
                    minElementIndex = j;
                }
            }

            temp = elements[i];
            elements[i] = elements[minElementIndex];
            elements[minElementIndex] = temp;

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