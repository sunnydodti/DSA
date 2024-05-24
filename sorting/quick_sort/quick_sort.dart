void main(List<String> args) {
  List<int> input = [4, 7, 9, 0, 3, 1, 5, 8, 5, 3, 5, 7, 8, 9, 2];
  print(input);
  print("quickSort: ${quickSort(input, 0, input.length - 1)}");
}

quickSort(List<int> elements, int start, int end) {
  if (start < end) {
    int pivot = partition(elements, start, end);
    quickSort(elements, start, pivot - 1);
    quickSort(elements, pivot + 1, end);
  }
  return elements;
}

int partition(List<int> elements, int start, int end) {
  int pivot = elements[end];
  int swapIndex = start - 1;

  for (int i = start; i < end; i++) {
    if (elements[i] <= pivot) {
      swapIndex++;
      swap(elements, swapIndex, i);
    }
  }
  swapIndex++;
  swap(elements, swapIndex, end);

  print("pivot: $pivot");
  print("elements: $elements");

  return swapIndex;
}

void swap(List<int> list, int index1, int index2) {
  int temp = list[index1];
  list[index1] = list[index2];
  list[index2] = temp;
}
