List<int> mergeSort(List<int> elements) {
  mergeSortRecursive(elements, 0, elements.length);
  return elements;
}

mergeSortRecursive(List<int> elements, int start, int end) {
  if (start >= end - 1) return;
  int middle = (start + (end - start) / 2).floor();

  mergeSortRecursive(elements, start, middle);
  mergeSortRecursive(elements, middle, end);
  merge(elements, start, middle, end);
}

void merge(List<int> elements, int start, int middle, int end) {
  List<int> leftArray = elements.sublist(start, middle);
  List<int> rightArray = elements.sublist(middle, end);

  int left_size = leftArray.length;
  int right_size = rightArray.length;

  int left_i = 0;
  int right_i = 0;
  int merged_i = start;

  while (left_i < left_size && right_i < right_size) {
    if (leftArray[left_i] < rightArray[right_i]) {
      elements[merged_i] = leftArray[left_i];
      left_i++;
    } else {
      elements[merged_i] = rightArray[right_i];
      right_i++;
    }
    merged_i++;
  }

  while (left_i < left_size) {
    elements[merged_i] = leftArray[left_i];
    left_i++;
    merged_i++;
  }

  while (right_i < right_size) {
    elements[merged_i] = rightArray[right_i];
    right_i++;
    merged_i++;
  }
}

void main() {
  List<int> input = [3, 19, 8, 2, 5, 1];
  print(input);
  print("mergeSort ${mergeSort(List<int>.from(input))}");
}
