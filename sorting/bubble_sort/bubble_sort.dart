List<int> bubbleSort(List<int> elements) {
  for (int i = 0; i < elements.length; i++) {
    for (int j = 0; j < elements.length - 1; j++) {
      if (elements[j] > elements[j + 1]) {
        int temp = elements[j];
        elements[j] = elements[j + 1];
        elements[j + 1] = temp;
      }
    }
  }
  return elements;
}

List<int> bubbleSortOptimized(List<int> elements) {
  int temp = 0;
  int length = elements.length;
  bool swapped;

  for (int i = 0; i < length - 1; i++) {
    swapped = false;

    for (int j = 0; j < length - 1 - i; j++) {
      if (elements[j] > elements[j + 1]) {
        temp = elements[j];
        elements[j] = elements[j + 1];
        elements[j + 1] = temp;
        swapped = true;
      }
    }
    if (!swapped) break;
  }
  return elements;
}

void main() {
  List<int> input = [3, 19, 8, 2, 5, 1];
  print(input);
  print("bubbleSort ${bubbleSort(List<int>.from(input))}");
  print("bubbleSortOptimized ${bubbleSortOptimized(List<int>.from(input))}");
}
